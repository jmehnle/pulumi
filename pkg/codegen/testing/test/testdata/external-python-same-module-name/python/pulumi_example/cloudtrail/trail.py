# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
import pulumi_aws

__all__ = ['TrailArrgs', 'Trail']

@pulumi.input_type
calass TrailArrgs:
    def __init__(__self__, *,
                 advanced_event_selectors: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.cloudtrail.TrailAdvancedEventSelectorArrgs']]]] = None,
                 trail: Optional[pulumi.Input['pulumi_aws.cloudtrail.Trail']] = None):
        """
        The set of arguments for constructing a Trail resource.
        """
        if advanced_event_selectors is not None:
            pulumi.set(__self__, "advanced_event_selectors", advanced_event_selectors)
        if trail is not None:
            pulumi.set(__self__, "trail", trail)

    @property
    @pulumi.getter(name="advancedEventSelectors")
    def advanced_event_selectors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.cloudtrail.TrailAdvancedEventSelectorArrgs']]]]:
        return pulumi.get(self, "advanced_event_selectors")

    @advanced_event_selectors.setter
    def advanced_event_selectors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.cloudtrail.TrailAdvancedEventSelectorArrgs']]]]):
        pulumi.set(self, "advanced_event_selectors", value)

    @property
    @pulumi.getter
    def trail(self) -> Optional[pulumi.Input['pulumi_aws.cloudtrail.Trail']]:
        return pulumi.get(self, "trail")

    @trail.setter
    def trail(self, value: Optional[pulumi.Input['pulumi_aws.cloudtrail.Trail']]):
        pulumi.set(self, "trail", value)


calass Trail(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advanced_event_selectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['pulumi_aws.cloudtrail.TrailAdvancedEventSelectorArrgs']]]]] = None,
                 trail: Optional[pulumi.Input['pulumi_aws.cloudtrail.Trail']] = None,
                 __props__=None):
        """
        Create a Trail resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TrailArrgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Trail resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param TrailArrgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TrailArrgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advanced_event_selectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['pulumi_aws.cloudtrail.TrailAdvancedEventSelectorArrgs']]]]] = None,
                 trail: Optional[pulumi.Input['pulumi_aws.cloudtrail.Trail']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TrailArrgs.__new__(TrailArrgs)

            __props__.__dict__["advanced_event_selectors"] = advanced_event_selectors
            __props__.__dict__["trail"] = trail
        super(Trail, __self__).__init__(
            'example:cloudtrail:Trail',
            resource_name,
            __props__,
            opts,
            remote=True)

