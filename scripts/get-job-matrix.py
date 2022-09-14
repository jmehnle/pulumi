#!/usr/bin/env python3
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-class-docstring
"""
Compute a GitHub Actions job matrix, or in the case of build and lint jobs, a set of versions to
build and produce.

Uses `gotestsum tool ci-matrix` to divide up Go packages into partitions to reduce execution time.
"""


import argparse
import itertools
import json
import os
import subprocess as sp
import sys
from dataclasses import dataclass
from enum import Enum
from pprint import pformat
from typing import Any, Dict, List, Optional, Set, TypedDict, Union

global_verbosity = 0

VersionSet = Dict[str, str]

class JobKind(str, Enum):
    """Output kinds supported with this utility."""

    INTEGRATION_TEST = "integration-test"
    UNIT_TEST = "unit-test"
    ALL_TEST = "all-test"


@dataclass
class PartitionModule:
    """Go modules to partition into jobs by package."""
    module_dir: str
    partitions: int

@dataclass
class PartitionPackage:
    """Go packages to subdivide into jobs by test."""

    package: str
    package_dir: str
    partitions: int


INTEGRATION_TEST_PACKAGES = {
    "github.com/pulumi/pulumi/pkg/v3/cmd/pulumi",
    "github.com/pulumi/pulumi/pkg/v3/codegen/testing/utils",
    "github.com/pulumi/pulumi/pkg/v3/graph/dotconv",
    "github.com/pulumi/pulumi/pkg/v3/testing/integration",
    "github.com/pulumi/pulumi/sdk/v3/go/auto",
    "github.com/pulumi/pulumi/sdk/v3/go/auto/debug",
    "github.com/pulumi/pulumi/sdk/v3/go/auto/optdestroy",
    "github.com/pulumi/pulumi/sdk/v3/go/auto/optremove",
    "github.com/pulumi/pulumi/sdk/v3/go/common/constant",
    "github.com/pulumi/pulumi/sdk/v3/go/common/util/retry",
    "github.com/pulumi/pulumi/sdk/v3/nodejs/npm",
    # And the entirety of the 'tests' module
}


def is_integration_test(pkg: str) -> bool:
    """Returns true if the package is an integration test"""
    return (
        pkg.startswith("github.com/pulumi/pulumi/tests")
        or pkg in INTEGRATION_TEST_PACKAGES
    )

class MakefileTest(TypedDict):
    name: str
    run: str
    eta: int

MAKEFILE_INTEGRATION_TESTS: List[MakefileTest] = [
    {"name": "sdk/dotnet test_auto", "run": "cd sdk/dotnet && make test_auto", "eta": 5},
    {"name": "sdk/nodejs test_auto", "run": "cd sdk/nodejs && make test_auto", "eta": 3},
    {"name": "sdk/nodejs unit_tests", "run": "cd sdk/nodejs && make unit_tests", "eta": 4},
    {"name": "sdk/python test_auto", "run": "cd sdk/python && make test_auto", "eta": 6},
    {"name": "sdk/python test_fast", "run": "cd sdk/python && make test_fast", "eta": 3},
]

MAKEFILE_UNIT_TESTS: List[MakefileTest] = [
    {"name": "sdk/dotnet dotnet_test", "run": "cd sdk/dotnet && make dotnet_test", "eta": 3},
    {"name": "sdk/nodejs sxs_tests", "run": "cd sdk/nodejs && make sxs_tests", "eta": 3},
]

ALL_PLATFORMS = ["ubuntu-latest", "windows-latest", "macos-latest"]


MINIMUM_SUPPORTED_VERSION_SET = {
    "name": "minimal",
    "dotnet": "6.0.x",
    "go": "1.18.x",
    "nodejs": "14.x",
    "python": "3.9.x",
}

CURRENT_VERSION_SET = {
    "name": "current",
    "dotnet": "6.0.x",
    "go": "1.19.x",
    "nodejs": "18.x",
    "python": "3.10.x",
}


def run_list_packages(module_dir: str) -> Set[str]:
    """Runs go list on pkg, sdk, and tests"""
    try:
        cmd = sp.run(
            ["go", "list", "-tags", "all", "-find", "./..."],
            cwd=module_dir,
            check=True,
            capture_output=True,
            text=True,
        )
    except sp.CalledProcessError as err:
        raise Exception("Failed to list packages in module, usually this implies a Go compilation error. Check that `make lint` succeeds.") from err
    return set(cmd.stdout.split())

def run_list_tests(pkg_dir: str) -> List[str]:
    """Runs `go test --list` on a given package."""

    # This Go command is finnicky. It must be run from the directory queried as a '.' path argument,
    # and the output is unstructured, mixing diagnostics & test names on stdout. The output
    # typically looks like this:
    #
    # ```sh
    # $ go test --list .
    # TestStackTagValidation
    # ...
    # TestPassphrasePrompting
    # ok      github.com/pulumi/pulumi/tests/integration      0.093s
    # ```
    #
    # That last line is emitted on stdout - so we skip any lines containing "ok".
    #
    # Neither relative paths nor package paths will work, as shown below:
    #
    # ```sh
    # $ go test -tags all --list github.com/pulumi/pulumi/tests/integration
    # no Go files in /home/friel/c/github.com/pulumi/pulumi
    #
    # $ go test -tags all --list ./tests/integration
    # no Go files in /home/friel/c/github.com/pulumi/pulumi
    # ```
    cmd = sp.run(
        ["go", "test", "-tags", "all", "--list", "."],
        check=True,
        cwd=pkg_dir,
        capture_output=True,
        text=True,
    )

    tests: List[str] = []

    for line in cmd.stdout.split():
        if line.startswith("ok"):
            break

        tests.append(line)

    return tests


class GotestsumInclude(TypedDict):
    """Job entry from `gotestsum tool ci-matrix`"""

    id: int
    estimatedRuntime: str
    packages: str
    tests: Optional[str]
    description: str


class GotestsumOutput(TypedDict):
    """Type of value returned via `gotestsum tool ci-matrix`"""

    include: List[GotestsumInclude]



class TestSuite(TypedDict):
    """Commands passed to jobs"""
    name: str
    command: str


Matrix = TypedDict("Matrix", {
    "test-suite": List[TestSuite],
    "platform": List[str],
    "version-set": VersionSet,
})


def run_gotestsum_ci_matrix_packages(go_packages: List[str], partition_module: PartitionModule) -> List[TestSuite]:
    """Runs `gotestsum tool ci-matrix` to compute Go test partitions"""
    script_dir = os.path.dirname(os.path.realpath(__file__))
    test_reports_dir = os.path.join(script_dir, "..", "test-results")
    os.makedirs(test_reports_dir, exist_ok=True)

    if partition_module.partitions == 1:
        pkgs = " ".join(go_packages)
        return [{
            "name": f"{partition_module.module_dir}",
            "command": f'make PKGS="{pkgs}" gotestsum/{partition_module.module_dir}'
        }]

    gotestsum_matrix_args = [
        "gotestsum",
        "tool",
        "ci-matrix",
        "--partitions",
        f"{partition_module.partitions}",
        "--timing-files",
        f"{test_reports_dir}/*.json",
        "--debug",
    ]

    try:
        cmd = sp.run(
            gotestsum_matrix_args,
            input="\n".join(go_packages),
            check=True,
            capture_output=True,
            text=True,
        )
    except sp.CalledProcessError as err:
        raise Exception(f"Failed to run gotestsum ci-matrix: {err.stderr}") from err
    if global_verbosity >= 3:
        print(cmd.stderr, file=sys.stderr)

    gotestsum_matrix: GotestsumOutput = json.loads(cmd.stdout)

    if global_verbosity >= 3:
        print(pformat(gotestsum_matrix), file=sys.stderr)

    matrix_jobs = gotestsum_matrix["include"]
    buckets_len = len(f"{len(matrix_jobs)}")
    test_suites: List[TestSuite] = []
    for idx, include in enumerate(matrix_jobs):
        idx_str = f"{idx+1}".zfill(buckets_len)

        test_command = f'PKGS="{include["packages"]}" make gotestsum/{partition_module.module_dir}'
        if global_verbosity >= 1:
            print(test_command, file=sys.stderr)
        test_suites.append(
            {
                "name": f"{partition_module.module_dir} {idx_str}/{partition_module.partitions}",
                "command": test_command,
            }
        )

    return test_suites


def run_gotestsum_ci_matrix_single_package(
    partition_pkg: PartitionPackage, tests: List[str]
) -> List[TestSuite]:
    """Runs `gotestsum tool ci-matrix` to compute Go test partitions for a single package"""
    script_dir = os.path.dirname(os.path.realpath(__file__))
    test_reports_dir = os.path.join(script_dir, "..", "test-results")
    os.makedirs(test_reports_dir, exist_ok=True)

    gotestsum_matrix_args = [
        "gotestsum",
        "tool",
        "ci-matrix",
        "--partitions",
        f"{partition_pkg.partitions}",
        "--timing-files",
        f"{test_reports_dir}/*.json",
        "--partition-tests-in-package",
        partition_pkg.package,
        "--debug",
    ]

    try:
        cmd = sp.run(
            gotestsum_matrix_args,
            input="\n".join(tests),
            check=True,
            capture_output=True,
            text=True,
        )
    except sp.CalledProcessError as err:
        raise Exception(f"Failed to run gotestsum ci-matrix: {err.stderr}") from err
    if global_verbosity >= 3:
        print(cmd.stderr, file=sys.stderr)

    gotestsum_matrix: GotestsumOutput = json.loads(cmd.stdout)

    if global_verbosity >= 3:
        print(pformat(gotestsum_matrix), file=sys.stderr)

    include = gotestsum_matrix["include"]
    buckets_len = len(f"{len(include)}")
    test_suites: List[TestSuite] = []
    for idx, include in enumerate(include):
        idx_str = f"{idx+1}".zfill(buckets_len)

        # the test list is formatted like so:     -run='^TestOne$,^TestTwo$'
        # but we want:                            -run ^(TestOne|TestTwo)$

        test_list = include["tests"]

        if not test_list:
            continue

        test_list = test_list.replace("$,^", "|")
        test_list = test_list.replace("='^", " ^(")
        test_list = test_list.replace("$'", ")$")

        env=f'PKGS="{include["packages"]}" OPTS="{test_list}"'
        test_command = f'{env} make gotestsum/{partition_pkg.package_dir}'
        if global_verbosity >= 1:
            print(test_command, file=sys.stderr)

        test_suites.append(
            {
                "name": f"{partition_pkg.package_dir} {idx_str}/{partition_pkg.partitions}",
                "command": test_command,
            }
        )

    return test_suites


# pylint: disable=too-many-arguments
def get_matrix(
    kind: JobKind,
    partition_modules: List[PartitionModule],
    partition_packages: List[PartitionPackage],
    platforms: List[str],
    version_sets: List[VersionSet],
    fast: bool = False,
) -> Matrix:
    """Compute a job matrix"""
    if kind == JobKind.INTEGRATION_TEST:
        makefile_tests = MAKEFILE_INTEGRATION_TESTS
    elif kind == JobKind.UNIT_TEST:
        makefile_tests = MAKEFILE_UNIT_TESTS
    elif kind == JobKind.ALL_TEST:
        makefile_tests = MAKEFILE_INTEGRATION_TESTS + MAKEFILE_UNIT_TESTS
    else:
        raise Exception(f"Unknown job kind {kind}")

    test_suites: List[TestSuite] = []

    for test in makefile_tests:
        if fast and test["eta"] > 5:
            continue

        test_suites.append({"name": test["name"], "command": test["run"]})

    partitioned_packages = {part.package for part in partition_packages}

    for item in partition_modules:
        go_packages = run_list_packages(item.module_dir)
        go_packages = set(go_packages) - partitioned_packages

        if kind == JobKind.INTEGRATION_TEST:
            go_packages = {pkg for pkg in go_packages if is_integration_test(pkg)}
        elif kind == JobKind.UNIT_TEST:
            go_packages = {pkg for pkg in go_packages if not is_integration_test(pkg)}
        elif kind == JobKind.ALL_TEST:
            pass

        test_suites += run_gotestsum_ci_matrix_packages(list(go_packages), item)

    for item in partition_packages:
        pkg_tests = run_list_tests(item.package_dir)

        test_suites += run_gotestsum_ci_matrix_single_package(item, pkg_tests)

    return {
        "test-suite": test_suites,
        "platform": platforms,
        "version-set": version_sets,
    }


def get_version_sets(args: argparse.Namespace):
    """Read version set arguments into valid sets"""
    version_sets: List[VersionSet] = []
    for named_version_set in args.version_set:
        if named_version_set == "minimum":
            version_sets.append(MINIMUM_SUPPORTED_VERSION_SET)
        elif named_version_set == "current":
            version_sets.append(CURRENT_VERSION_SET)
        else:
            raise argparse.ArgumentError(argument=None, message=f"Unknown version set {named_version_set}")

    for version_arg in args.versions or []:
        this_set = {**MINIMUM_SUPPORTED_VERSION_SET}
        version_arg = version_arg.split(",")
        for version in version_arg:
            lang, version = version.split("=")
            if lang not in ["dotnet", "go", "node", "python"]:
                raise argparse.ArgumentError(argument=None, message=f"Unknown language {lang}")
            this_set[lang] = version

        version_sets.append(this_set)

    return version_sets

def generate_version_set(args: argparse.Namespace):
    version_sets = get_version_sets(args)
    if len(version_sets) != 1:
        raise argparse.ArgumentError(
            argument=None,
            message=f"Exactly one version set must be specified (received {len(version_sets)}) for build and lint."
        )

    print(json.dumps(version_sets[0]))

def generate_matrix(args: argparse.Namespace):
    partition_modules: List[PartitionModule] = []
    for mod_dir, partitions in args.partition_module:
        # mod_dir, partitions = arg
        partition_modules.append(PartitionModule(mod_dir, int(partitions)))

    partition_packages: List[PartitionPackage] = []
    for pkg, pkg_dir, partitions in args.partition_package:
        partition_packages.append(PartitionPackage(pkg, pkg_dir, int(partitions)))

    version_sets = get_version_sets(args)

    print(json.dumps(get_matrix(
        kind=args.kind,
        platforms=args.platform,
        fast=args.fast,
        partition_modules=partition_modules,
        partition_packages=partition_packages,
        version_sets=version_sets,
    )))

def add_generate_matrix_args(parser: argparse.ArgumentParser):
    parser.set_defaults(func=generate_matrix)

    parser.add_argument(
        "--kind",
        required=True,
        choices=[kind.value for kind in JobKind],
        help="Kind of output to generate",
    )
    parser.add_argument(
        "--fast", action="store_true", default=False, help="Exclude slow tests"
    )
    parser.add_argument(
        "--partition-module",
        action="append",
        nargs=2,
        default=[],
        metavar=("MODULE_DIR", "PARTITIONS"),
        help="Partition the tests in a single module, by module directory.",
    )
    parser.add_argument(
        "--partition-package",
        action="append",
        nargs=3,
        default=[],
        metavar=("GO_PACKAGE", "PACKAGE_DIR", "PARTITIONS"),
        help="Partition the tests in a single package, instead of by package. "
        + "Must specify a package name, the directory containing the package, "
        + "and the number of partitions to divide the tests into. Tests added "
        + "are automatically excluded from modules.",
    )

    parser.add_argument(
        "--platform",
        action="store",
        nargs="*",
        default=ALL_PLATFORMS,
        choices=ALL_PLATFORMS,
        help="Platforms to test",
    )

    parser.add_argument(
        "--version-set",
        action="store",
        nargs="*",
        default=["minimum"],
        choices=["minimum", "current"],
        help="Named set of versions to use. Defaults to minimum supported versions. Available sets: minimum, current",
    )
    default_versions = ",".join(
        [f"{lang}={version}" for lang, version in MINIMUM_SUPPORTED_VERSION_SET.items()]
    )
    parser.add_argument(
        "--versions",
        action="store",
        type=str,
        nargs="*",
        help=(
            "Set of language versions to use, in the form of lang=version,lang=version. "
            + "Spaces separate distinct sets, creating separate sets of jobs. Prefer using .x or semver ranges. "
            + " For supported version strings, see, e.g., www.github.com/actions/setup-go for each language. "
            + "Languages not included in a set use the default."
            + f"Defaults: {default_versions}."
        ),
    )

def add_version_set_args(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--version-set",
        action="store",
        nargs="*",
        default=["minimum"],
        choices=["minimum", "current"],
        help="Named set of versions to use. Defaults to minimum supported versions. Available sets: minimum, current",
    )
    default_versions = ",".join(
        [f"{lang}={version}" for lang, version in MINIMUM_SUPPORTED_VERSION_SET.items()]
    )
    parser.add_argument(
        "--versions",
        action="store",
        type=str,
        nargs="*",
        help=(
            "Set of language versions to use, in the form of lang=version,lang=version. "
            + "Spaces separate distinct sets, creating separate sets of jobs. Prefer using .x or semver ranges. "
            + " For supported version strings, see, e.g., www.github.com/actions/setup-go for each language. "
            + "Languages not included in a set use the default."
            + f"Defaults: {default_versions}."
        ),
    )
    parser.set_defaults(func=generate_version_set)

def combine_matrices(args: argparse.Namespace):
    matrix_includes = []
    for json_obj in args.matrices:
        matrix: Dict[str, List[Any]] = json.loads(json_obj)

        keys = list(matrix.keys())

        combinations = list(itertools.product(*matrix.values()))

        for combination in combinations:
            include = dict(zip(keys, combination))
            matrix_includes.append(include)

    print(json.dumps({
        "include": matrix_includes
    }))

def main():
    parser = argparse.ArgumentParser(description="Generate job and version matrices")
    parser.add_argument("-v", "--verbosity", action="count", default=0, help="logging verbosity, specify multiple times for higher levels, i.e.: -vvv")

    subparsers = parser.add_subparsers()
    gen_matrix_parser = subparsers.add_parser("generate-matrix",
        help="Generate a matrix of jobs.")
    add_generate_matrix_args(gen_matrix_parser)

    version_set_parser = subparsers.add_parser("generate-version-set",
        help="Generate a version set only.")
    add_version_set_args(version_set_parser)

    combine_matrices_parser = subparsers.add_parser("combine-matrices",
        help="Combine one or more matrices, computing all combinations of each and generating a list of includes.")
    combine_matrices_parser.add_argument("matrices", nargs=argparse.REMAINDER)
    combine_matrices_parser.set_defaults(func=combine_matrices)


    args = parser.parse_args()

    if not hasattr(args, 'func'):
        parser.print_help()
        sys.exit(1)

    global global_verbosity  # pylint: disable=global-statement
    global_verbosity = args.verbosity

    args.func(args)

if __name__ == "__main__":
    main()