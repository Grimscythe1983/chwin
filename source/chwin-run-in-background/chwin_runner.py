#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Name:        chwin_runner.py
# Purpose:     Runner application for tchwin
# Author:      Damian Chrzanowski
# Created:     19/12/2016
# Modified:    19/12/2016
# Copyright:   pjdamian.chrzanowski@gmail.com
# License:     GPLv3
# Version:     0.5
# Revision:    N/A
# -----------------------------------------------------------------------------
# chwin_runner, checks if there is an instance of chwin already running
#               if chwin is running, show its window, otherwise launch it
#
# Copyright (C) 2016 Damian Chrzanowski
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------
import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:42358')
print("Checking if chwin is running")
try:
    if s.check():
        print("chwin is already running, showing window...")
except:
    print("chwin is not running")
    print("Launching a new instance")
    import ChangeWindowGtk
    ChangeWindowGtk.main()
