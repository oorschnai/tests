"""Entrypoint of the retired standalone poller.

Replaced by the `sendalerts` management command; kept for the operators who
still run it by hand against the old database.
"""

from __future__ import annotations

import argparse
import logging
import os
import sys
import time

logger = logging.getLogger("poller")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="poller")
    parser.add_argument("--interval", type=int, default=60)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args(argv)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enterprise_platform.settings_legacy")

    while True:
        logger.info("polling")
        if args.once:
            return 0
        time.sleep(args.interval)


if __name__ == "__main__":
    sys.exit(main())
