# SPDX-FileCopyrightText: 2025-present Isaac To <candleindark@gmail.com>
#
# SPDX-License-Identifier: MIT


def bids_validator_deno() -> int:
    """
    Python entry point to invoke the BIDS validator binary built with `deno compile`.

    :return: The exit code of the BIDS validator binary.
    """

    import importlib.resources
    import subprocess
    import sys

    # Locate the binary within the package
    binary_path = importlib.resources.files("bids_validator_deno").joinpath(
        "bin", "bids-validator"
    )

    try:
        subprocess.run([str(binary_path)] + sys.argv[1:], check=True)
    except subprocess.CalledProcessError as e:
        return e.returncode
    else:
        return 0
