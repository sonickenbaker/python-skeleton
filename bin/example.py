from __future__ import unicode_literals

import argparse
import os
import subprocess

from python_skeleton import Skeleton


def parse_command_line():
    parser = argparse.ArgumentParser(description="This is just an example")
    parser.add_argument(
        "-e",
        "--example",
        dest="example",
        default="this is an example",
        help="example argument",
        required=False,
    )
    parser.add_argument(
        "--activate-example",
        dest="activate_example",
        default=False,
        action="store_true",
        help="store true argument",
        required=False,
    )
    return parser.parse_args()


def main():
    args = parse_command_line()
    print(Skeleton().say_hello())


if __name__ == "__main__":
    main()