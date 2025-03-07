# SPDX-FileCopyrightText: 2025-present Isaac To <candleindark@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from bids_validator_deno.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="bids-validator-deno")
def bids_validator_deno() -> int:
    """
    Python entry point to invoke the BIDS validator binary built with `deno compile`.

    :return: The exit code of the BIDS validator binary.
    """

    import importlib.resources
    import subprocess
    import sys

    # Locate the binary within the package
    binary_path = importlib.resources.files("bids_validator_deno").joinpath("bin", "bids-validator")

    try:
        subprocess.run(str(binary_path), check=True)
    except subprocess.CalledProcessError as e:
        return e.returncode
    else:
        return 0
