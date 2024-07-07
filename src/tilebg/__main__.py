"""Seamless geometric desktop background image generator."""

import argparse
import inspect
import random

from .lib.svg import generate_svg
from . import patterns


PATTERNS = [name for name, _ in inspect.getmembers(patterns, inspect.ismodule)]


def main() -> None:
    """Parse CLI arguments and generate SVG of the target pattern."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pattern", choices=PATTERNS)
    args = parser.parse_args()
    module = getattr(patterns, args.pattern)
    random.seed(1)
    print(generate_svg(**module.parameters()))


main()
