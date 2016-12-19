#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Name:        ChangeWindowGtk.py
# Purpose:     Keyboard based window switcher for Linux
# Author:      Damian Chrzanowski
# Created:     17/12/2016
# Modified:    17/12/2016
# Copyright:   pjdamian.chrzanowski@gmail.com
# License:     GPLv3
# Version:     0.2
# Revision:    N/A
# -----------------------------------------------------------------------------
# chwin, GUI application that assists in window selection using just a keyboard
#        user is presented with a list of currently open windows,
#        user can narrow the choice by a standard keyboard entry,
#        arrow keys or digits from 0 to 9
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
try:
    from gi.repository import Gtk, Gdk
    import subprocess
    import WmctrlWrapper
except Exception as e:
    print("\n\nchwin is missing a module!!!")
    print(e)
    quit()

VERSION = "0.2"


class MainWindow(object):
    """Create the main window class"""
    def __init__(self):
        # class variables
        self.window_choices = WmctrlWrapper.grab_window_names()
        self.current_window_choices = list(self.window_choices)
        self.selector_pos = 0
        self.selector_max = len(self.window_choices) - 1

        # main window and grid
        self.window = Gtk.Window()
        self.window.connect("destroy", lambda q: Gtk.main_quit())
        self.window.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("black"))
        self.window.set_title("chwin v" + VERSION)
        # self.window.set_icon_from_file('icon_small.png')
        self.grid = Gtk.Grid()
        self.window.add(self.grid)

        # entry box
        self.entry_box = Gtk.Entry()
        self.entry_box.set_hexpand(True)
        self.entry_box.connect("activate", self.entry_activated)
        self.entry_box.connect("key-press-event", self.key_activated)
        self.entry_box.connect("changed", self.entry_changed)
        self.entry_box.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("black"))
        self.entry_box.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("white"))

        # main view as a label
        self.search_view = Gtk.Label()
        self.search_view.set_xalign(0)
        self.search_view.set_margin_left(10)
        self.search_view.set_margin_right(10)
        self.search_view.set_margin_top(5)
        self.search_view.set_justify(Gtk.Justification.LEFT)
        self.search_view.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("black"))
        self.search_view.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("white"))

        # insert content to the view
        self.draw_selections()

        # attack widgets to the grid
        self.grid.attach(self.entry_box, 0, 0, 1, 1)
        self.grid.attach(self.search_view, 0, 1, 1, 1)
        self.window.show_all()

    def run_wmctrl(self):
        user_input = self.entry_box.get_text()

        if user_input != "":
            subprocess.run(["wmctrl", "-a", self.current_window_choices[self.selector_pos]])
        else:
            subprocess.run(["wmctrl", "-a", self.window_choices[self.selector_pos]])
        Gtk.main_quit()

    def entry_activated(self, widget):
        self.run_wmctrl()

    def key_activated(self, widget, ev, data=None):
        if ev.keyval == Gdk.KEY_Escape:
            Gtk.main_quit()

        elif ev.keyval == Gdk.KEY_Up:
            self.selector_pos -= 1
            if self.selector_pos < 0:
                self.selector_pos = 0

            self.draw_selections()

        elif ev.keyval == Gdk.KEY_Down:
            self.selector_pos += 1
            if self.selector_pos > self.selector_max:
                self.selector_pos = self.selector_max

            self.draw_selections()

        elif ev.keyval > 47 and ev.keyval < 58:
            key_in = ev.keyval - 48
            self.selector_pos = key_in
            self.run_wmctrl()

    def entry_changed(self, widget):
        user_input = widget.get_text()
        self.selector_pos = 0  # reset the selector position

        if user_input != "":  # if the string is not empty -> search list
            self.current_window_choices = []  # reset current choices

            if user_input[0].isupper():  # if the first char is uppercase treat the rest so as well
                for each in self.window_choices:
                    if user_input in each:
                        self.current_window_choices.append(each)

            else:  # first char is not upper case, treat the rest as not case sensitive
                for each in self.window_choices:
                    if user_input in each.lower():
                        self.current_window_choices.append(each)
        else:  # string is empty, just show a list of all the windows
            self.current_window_choices = list(self.window_choices)

        self.selector_max = len(self.current_window_choices) - 1  # set the max value for the selector
        self.draw_selections()

    def draw_selections(self):
        label_txt = ""

        for idx, each in enumerate(self.current_window_choices):
            if idx == self.selector_pos:
                label_txt += "<span color='green'>" + str(idx) + "</span><span color='red'> > </span><b>" + each + "</b>\n"
            else:
                label_txt += "<span color='green'>" + str(idx) + "</span>   " + each + "\n"

        self.search_view.set_markup(label_txt)


if __name__ == '__main__':
    window = MainWindow()
    Gtk.main()
