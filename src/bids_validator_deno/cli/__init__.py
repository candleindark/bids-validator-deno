# SPDX-FileCopyrightText: 2025-present Isaac To <candleindark@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from bids_validator_deno.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="bids-validator-deno")
def bids_validator_deno():
    click.echo("Hello world!")
