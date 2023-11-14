# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'ProviderCertmanagerArrgs',
]

@pulumi.input_type
calass ProviderCertmanagerArrgs:
    def __init__(__self__, *,
                 mtls_cert_pem: pulumi.Input[str],
                 mtls_key_pem: pulumi.Input[str]):
        pulumi.set(__self__, "mtls_cert_pem", mtls_cert_pem)
        pulumi.set(__self__, "mtls_key_pem", mtls_key_pem)

    @property
    @pulumi.getter
    def mtls_cert_pem(self) -> pulumi.Input[str]:
        return pulumi.get(self, "mtls_cert_pem")

    @mtls_cert_pem.setter
    def mtls_cert_pem(self, value: pulumi.Input[str]):
        pulumi.set(self, "mtls_cert_pem", value)

    @property
    @pulumi.getter
    def mtls_key_pem(self) -> pulumi.Input[str]:
        return pulumi.get(self, "mtls_key_pem")

    @mtls_key_pem.setter
    def mtls_key_pem(self, value: pulumi.Input[str]):
        pulumi.set(self, "mtls_key_pem", value)


