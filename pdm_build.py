#!/usr/bin/env python3

import platform
import sys
from wheel.cli.tags import tags
from pathlib import Path
import shutil

from pdm.backend.hooks import Context


def get_platform_tag():
    # Get machine architecture
    arch = platform.machine()

    # Validate architecture
    if arch == "x86_64":
        arch_tag = "x86_64"
    elif arch == "AMD64":
        # seems to be the case on Windows
        arch_tag = arch.lower()
    else:
        raise ValueError(f"Unsupported architecture: {arch}")

    # Determine OS and construct the appropriate tag
    if sys.platform.startswith("linux"):
        platform_tag = f"manylinux_2_17_{arch_tag}"
    elif sys.platform == "darwin":
        if arch_tag == "arm64":
            platform_tag = f"macosx_11_0_{arch_tag}"
        else:
            platform_tag = f"macosx_10_16_{arch_tag}"
    elif sys.platform.startswith("win"):
        platform_tag = f"win_{arch_tag}"
    else:
        raise ValueError(f"Unsupported platform: {sys.platform}")

    return platform_tag


# picked up from
# https://github.com/Bing-su/pip-binary-factory/blob/main/zig/pdm_build.py


def pdm_build_hook_enabled(context: Context):
    return context.target != "sdist"


def pdm_build_initialize(context: Context) -> None:
    setting = {"--python-tag": "py3", "--py-limited-api": "none"}
    context.builder.config_settings = {**setting, **context.builder.config_settings}

    context.ensure_build_dir()
    # download(context.build_dir)


def pdm_build_finalize(context: Context, artifact: Path) -> None:
    renamed = tags(
        str(artifact),
        python_tags="py3",
        abi_tags="none",
        platform_tags=get_platform_tag(),  ## TODO transform
        remove=True,
    )
    print(renamed)

    if context.build_dir.exists():
        shutil.rmtree(context.build_dir)


if __name__ == "__main__":
    try:
        tag = get_platform_tag()
        print(f"The platform tag is: {tag}")
    except ValueError as e:
        print(f"Error: {e}")
