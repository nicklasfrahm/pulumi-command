# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *
from .random import *
_utilities.register(
    resource_modules="""
[
 {
  "pkg": "command",
  "mod": "index",
  "fqn": "pulumi_command",
  "classes": {
   "command:index:Random": "Random"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "command",
  "token": "pulumi:providers:command",
  "fqn": "pulumi_command",
  "class": "Provider"
 }
]
"""
)