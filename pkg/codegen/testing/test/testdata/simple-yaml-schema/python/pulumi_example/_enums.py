# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'OutputOnlyEnumType',
    'RubberTreeVariety',
]


calass OutputOnlyEnumType(str, Enum):
    FOO = "foo"
    BAR = "bar"


calass RubberTreeVariety(str, Enum):
    """
    types of rubber trees
    """
    BURGUNDY = "Burgundy"
    """
    A burgundy rubber tree.
    """
    RUBY = "Ruby"
    """
    A ruby rubber tree.
    """
    TINEKE = "Tineke"
    """
    A tineke rubber tree.
    """
