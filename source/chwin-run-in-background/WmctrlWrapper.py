#!/usr/bin/env python3
# coding=utf-8
# -----------------------------------------------------------------------------
# Name:        WmctrlWrapper.py
# Purpose:     Builds a list of currently open windows, uses wmctrl
# Author:      Damian Chrzanowski
# Created:     17/12/2016
# Modified:    17/12/2016
# Copyright:   pjdamian.chrzanowski@gmail.com
# License:     GPLv3
# Version:     0.2
# Revision:    N/A
# -----------------------------------------------------------------------------
# WmctrlWrapper, builds a list of currently open windows, uses wmctrl
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

import subprocess


def grab_window_names(BANNED_NAMES):

    try:
        hostname = str(subprocess.check_output("echo $HOSTNAME", shell=True), "utf-8")
    except:
        print("Error retrieving environmental variable!\n")
        print("$HOSTNAME environment variable is not set!!!")
        quit()
    hostname = hostname.strip()

    if hostname == "":
        print("Error retrieving environmental variable!\n")
        print("$HOSTNAME environment variable is not set!!!")
        quit()

    try:
        wmctrl_output = str(subprocess.check_output("wmctrl -l", shell=True), "utf-8")
    except:
        print("wmctrl not found!\n")
        print("Please make sure that wmctrl is installed using your distro's package manager")
        print("Eg. on Ubuntu: sudo apt-get install wmctrl")
        print("Arch Linux: sudo pacman -S wmctrl")

    wmctrl_output = wmctrl_output.split("\n")

    window_names = []
    for each in wmctrl_output:
        if check_ban(BANNED_NAMES, each):
            continue

        # split at hostname, grab the last index and strip of whitespace
        if hostname not in each:  # no hostname , split string using 'N/A'
            window_names.append(each.split("N/A", 1)[-1].strip())
        else:
            window_names.append(each.split(hostname, 1)[-1].strip())
    del window_names[-1]  # there is always one empty at the end, remove it
    return window_names


def check_ban(bans, against):
    for each in bans:
        if each in against:
            return True
