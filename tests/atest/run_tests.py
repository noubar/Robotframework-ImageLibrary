#!/usr/bin/env python


import sys
import os

from pathlib import Path

from robot import run_cli


if __name__ == '__main__':
    curdir = Path(__file__).parent
    srcdir = curdir / '..' / '..' / 'src'
    run_cli(sys.argv[1:] + ['-P', srcdir.resolve(), curdir])
