# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._enums import *
from .resource import Resource

__all__ = [
    'ConfigMap',
    'Object',
    'ObjectWithNodeOptionalInputs',
    'OutputOnlyObjectType',
    'SomeOtherObject',
]

@pulumi.output_type
calass ConfigMap(dict):
    def __init__(__self__, *,
                 config: Optional[str] = None):
        if config is not None:
            pulumi.set(__self__, "config", config)

    @property
    @pulumi.getter
    def config(self) -> Optional[str]:
        return pulumi.get(self, "config")


@pulumi.output_type
calass Object(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "stillOthers":
            suggest = "still_others"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in Object. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        Object.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        Object.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bar: Optional[str] = None,
                 configs: Optional[Sequence['outputs.ConfigMap']] = None,
                 foo: Optional['Resource'] = None,
                 others: Optional[Sequence[Sequence['outputs.SomeOtherObject']]] = None,
                 still_others: Optional[Mapping[str, Sequence['outputs.SomeOtherObject']]] = None):
        """
        :param Sequence[Sequence['SomeOtherObject']] others: List of lists of other objects
        :param Mapping[str, Sequence['SomeOtherObject']] still_others: Mapping from string to list of some other object
        """
        if bar is not None:
            pulumi.set(__self__, "bar", bar)
        if configs is not None:
            pulumi.set(__self__, "configs", configs)
        if foo is not None:
            pulumi.set(__self__, "foo", foo)
        if others is not None:
            pulumi.set(__self__, "others", others)
        if still_others is not None:
            pulumi.set(__self__, "still_others", still_others)

    @property
    @pulumi.getter
    def bar(self) -> Optional[str]:
        return pulumi.get(self, "bar")

    @property
    @pulumi.getter
    def configs(self) -> Optional[Sequence['outputs.ConfigMap']]:
        return pulumi.get(self, "configs")

    @property
    @pulumi.getter
    def foo(self) -> Optional['Resource']:
        return pulumi.get(self, "foo")

    @property
    @pulumi.getter
    def others(self) -> Optional[Sequence[Sequence['outputs.SomeOtherObject']]]:
        """
        List of lists of other objects
        """
        return pulumi.get(self, "others")

    @property
    @pulumi.getter(name="stillOthers")
    def still_others(self) -> Optional[Mapping[str, Sequence['outputs.SomeOtherObject']]]:
        """
        Mapping from string to list of some other object
        """
        return pulumi.get(self, "still_others")


@pulumi.output_type
calass ObjectWithNodeOptionalInputs(dict):
    def __init__(__self__, *,
                 foo: str,
                 bar: Optional[int] = None):
        pulumi.set(__self__, "foo", foo)
        if bar is not None:
            pulumi.set(__self__, "bar", bar)

    @property
    @pulumi.getter
    def foo(self) -> str:
        return pulumi.get(self, "foo")

    @property
    @pulumi.getter
    def bar(self) -> Optional[int]:
        return pulumi.get(self, "bar")


@pulumi.output_type
calass OutputOnlyObjectType(dict):
    def __init__(__self__, *,
                 foo: Optional[str] = None):
        if foo is not None:
            pulumi.set(__self__, "foo", foo)

    @property
    @pulumi.getter
    def foo(self) -> Optional[str]:
        return pulumi.get(self, "foo")


@pulumi.output_type
calass SomeOtherObject(dict):
    def __init__(__self__, *,
                 baz: Optional[str] = None):
        if baz is not None:
            pulumi.set(__self__, "baz", baz)

    @property
    @pulumi.getter
    def baz(self) -> Optional[str]:
        return pulumi.get(self, "baz")


