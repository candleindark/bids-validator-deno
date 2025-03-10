#!/usr/bin/env python3

import platform
import sys
import os
from packaging.tags import sys_tags
from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


def get_platform_tag():
    # Get machine architecture
    arch = platform.machine()

    # Validate architecture
    if arch == "x86_64":
        arch_tag = "x86_64"
    elif arch in ("arm64", "aarch64"):
        arch_tag = "arm64"
    else:
        raise ValueError(f"Unsupported architecture: {arch}")

    # Determine OS and construct the appropriate tag
    if sys.platform.startswith("linux"):
        os_tag = f"manylinux_2_17_{arch_tag}"
    elif sys.platform == "darwin":
        os_tag = f"macosx_11_0_{arch_tag}"
    elif sys.platform.startswith("win"):
        os_tag = f"win_{arch_tag}"
    else:
        raise ValueError(f"Unsupported platform: {sys.platform}")

    # Build the final tag
    return f"py3-none-{os_tag}"



class CustomBuildHook(BuildHookInterface):
    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        build_data["pure_python"] = False
        # build_data["infer_tag"] = True
        build_data["tag"] = get_platform_tag()

# Example usage
if __name__ == "__main__":
    try:
        tag = get_platform_tag()
        print(f"The platform tag is: {tag}")
    except ValueError as e:
        print(f"Error: {e}")
