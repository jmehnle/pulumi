# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'CompositePathResponse',
    'IndexingPolicyResponse',
    'SqlContainerGetPropertiesResponseResource',
]

@pulumi.output_type
calass CompositePathResponse(dict):
    def __init__(__self__, *,
                 order: Optional[str] = None,
                 path: Optional[str] = None):
        """
        :param str order: Sort order for composite paths.
        :param str path: The path for which the indexing behavior applies to. Index paths typically start with root and end with wildcard (/path/*)
        """
        if order is not None:
            pulumi.set(__self__, "order", order)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def order(self) -> Optional[str]:
        """
        Sort order for composite paths.
        """
        return pulumi.get(self, "order")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        The path for which the indexing behavior applies to. Index paths typically start with root and end with wildcard (/path/*)
        """
        return pulumi.get(self, "path")


@pulumi.output_type
calass IndexingPolicyResponse(dict):
    """
    Cosmos DB indexing policy
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "compositeIndexes":
            suggest = "composite_indexes"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IndexingPolicyResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IndexingPolicyResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IndexingPolicyResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 composite_indexes: Optional[Sequence[Sequence['outputs.CompositePathResponse']]] = None):
        """
        Cosmos DB indexing policy
        :param Sequence[Sequence['CompositePathResponse']] composite_indexes: List of composite path list
        """
        if composite_indexes is not None:
            pulumi.set(__self__, "composite_indexes", composite_indexes)

    @property
    @pulumi.getter(name="compositeIndexes")
    def composite_indexes(self) -> Optional[Sequence[Sequence['outputs.CompositePathResponse']]]:
        """
        List of composite path list
        """
        return pulumi.get(self, "composite_indexes")


@pulumi.output_type
calass SqlContainerGetPropertiesResponseResource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "indexingPolicy":
            suggest = "indexing_policy"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SqlContainerGetPropertiesResponseResource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SqlContainerGetPropertiesResponseResource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SqlContainerGetPropertiesResponseResource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 indexing_policy: Optional['outputs.IndexingPolicyResponse'] = None):
        """
        :param 'IndexingPolicyResponse' indexing_policy: The configuration of the indexing policy. By default, the indexing is automatic for all document paths within the container
        """
        if indexing_policy is not None:
            pulumi.set(__self__, "indexing_policy", indexing_policy)

    @property
    @pulumi.getter(name="indexingPolicy")
    def indexing_policy(self) -> Optional['outputs.IndexingPolicyResponse']:
        """
        The configuration of the indexing policy. By default, the indexing is automatic for all document paths within the container
        """
        return pulumi.get(self, "indexing_policy")


