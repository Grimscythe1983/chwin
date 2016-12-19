#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Name:        SettingManager.py
# Purpose:     Checks setting for the chwin application
# Author:      Damian Chrzanowski
# Created:     19/12/2016
# Modified:    19/12/2016
# Copyright:   pjdamian.chrzanowski@gmail.com
# License:     GPLv3
# Version:     0.1
# Revision:    N/A
# -----------------------------------------------------------------------------
# SettingManager, Reads settings for the chwin application, colors, bans, etc
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
import os

HOME_PATH = os.path.expanduser('~')
SETTINGS_PATH = os.path.join(HOME_PATH, ".config/chwin/settings.cfg")


def create_default_config(VERSION):
    PATH_TO_CONFIG = os.path.split(SETTINGS_PATH)[0]
    if not os.path.exists(PATH_TO_CONFIG):
        os.makedirs(PATH_TO_CONFIG)

    comments = """# You can also place colors in a hexadecimal format
# like so -> entry_BG:#FF0000
# to make the entry background red
# or arrow:#0000FF
# to make the arrow blue
# Bans line has to be a single line. bans are windows that will not be displayed
# they can contain a full name of the window or just a part of the name
# and need to be semicolon ; separated
"""
    entry_bg = "black"
    entry_fg = "white"
    results_bg = "black"
    results_fg = "white"
    arrow = "red"
    numbers = "green"
    bans = "chwin v" + VERSION + ";conky;Desktop;xfce4;tilda"
    output = """{7}
entry_BG:{0}
entry_FG:{1}
results_BG:{2}
results_FG:{3}
arrow:{4}
numbers:{5}
bans:{6}
""".format(entry_bg, entry_fg, results_bg, results_fg, arrow, numbers, bans, comments)
    f_handle = open(SETTINGS_PATH, "w")
    f_handle.write(output)
    f_handle.close()


def extract(setting_name, line):
    line = line.split(setting_name)[-1]
    line = line.strip()
    return line


def read_config():
    f_handle = open(SETTINGS_PATH, "r")
    settings = {"entry_BG": "",
                "entry_FG": "",
                "results_BG": "",
                "results_FG": "",
                "arrow": "",
                "numbers": "",
                "bans": []}
    for each_line in f_handle:
        if each_line.startswith("#"):
            continue
        elif "entry_BG:" in each_line:
            settings["entry_BG"] = extract("entry_BG:", each_line)
        elif "entry_FG:" in each_line:
            settings["entry_FG"] = extract("entry_FG:", each_line)
        elif "results_FG:" in each_line:
            settings["results_FG"] = extract("results_FG:", each_line)
        elif "results_BG:" in each_line:
            settings["results_BG"] = extract("results_BG:", each_line)
        elif "arrow:" in each_line:
            settings["arrow"] = extract("arrow:", each_line)
        elif "numbers:" in each_line:
            settings["numbers"] = extract("numbers:", each_line)
        elif "bans:" in each_line:
            bans = extract("bans:", each_line)
            bans = bans.split(";")
            settings["bans"] = bans

    return settings


def check_config(VERSION):

    if os.path.exists(SETTINGS_PATH):
        return read_config()
    else:
        create_default_config(VERSION)
        return read_config()

if __name__ == '__main__':
    print(check_config("0.2"))
