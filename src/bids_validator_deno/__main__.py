# SPDX-FileCopyrightText: 2025-present Isaac To <candleindark@gmail.com>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from bids_validator_deno.cli import bids_validator_deno

    sys.exit(bids_validator_deno())
