#!/usr/bin/python
# Copyright (c) TurnKey GNU/Linux - http://www.turnkeylinux.org
#
# This file is part of Verseek
#
# Verseek is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3 of the License, or (at your
# option) any later version.

from os.path import *
import pyproject

class CliWrapper(pyproject.CliWrapper):
    INSTALL_PATH = dirname(__file__)

if __name__ == '__main__':
    CliWrapper.main()

