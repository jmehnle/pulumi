# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['FOOEncryptedBarClassArrgs', 'FOOEncryptedBarClass']

@pulumi.input_type
calass FOOEncryptedBarClassArrgs:
    def __init__(__self__):
        """
        The set of arguments for constructing a FOOEncryptedBarClass resource.
        """
        pass


calass FOOEncryptedBarClass(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 __props__=None):
        """
        Create a FOOEncryptedBarClass resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[FOOEncryptedBarClassArrgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a FOOEncryptedBarClass resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param FOOEncryptedBarClassArrgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FOOEncryptedBarClassArrgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FOOEncryptedBarClassArrgs.__new__(FOOEncryptedBarClassArrgs)

        super(FOOEncryptedBarClass, __self__).__init__(
            'foo-bar:submodule1:FOOEncryptedBarClass',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FOOEncryptedBarClass':
        """
        Get an existing FOOEncryptedBarClass resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FOOEncryptedBarClassArrgs.__new__(FOOEncryptedBarClassArrgs)

        return FOOEncryptedBarClass(resource_name, opts=opts, __props__=__props__)

