![screenshot](https://cloud.githubusercontent.com/assets/16053284/21318741/67e0896e-c602-11e6-8ea8-cbc1fbb7928b.png)

# chwin v 0.3
Keyboard based window switcher for Linux

Copyright (C) 2016 Damian Chrzanowski
License : GNU Public License v3
Check out my website at: http://damianch.eu.pn/

### Overview:
chwin is an application for linux only. It shows a small window with a list of currently open windows.
A selection can be made by narrowing down the search with a keyboard and pressing Enter, note that using a capital letter as the first input triggers a case sensitive search.
Users can also use numbers from 0 to 9 to quick jump.
For traditional usage, use up and down arrows keys and press enter to switch to the selected window.

### Dependencies
This software is for linux ONLY and requires you to install wmctrl (it is tiny), python3 and Gtk3 should be already installed on most of linux distributions.
To install the dependencies type (Ubuntu, Debian etc.):

`sudo apt-get install wmctrl python3 gtk3`

For arch linux and similar type:

`sudo pacman -S wmctrl python3 gtk3`

Any other distro should also have wmctrl python3 gtk3 in their availability, just user your package manager.

#### Installation:

chwin-standard is a low resource version (recommended).
chwin-run-in-background is slightly more demanding on the resources (only a few megs), but it is also much faster.

Copy all the files from either the source/chwin-standard or source/chwin-run-in-background
to your ~/bin (/home/your-username/bin) directory and just in case make sure that chwim is executable by running: `chmod +x chwin` from your terminal. Now you can bind `chwin` to any shortcut, or run it from wherever you want.

#### Configuration:

After the first run a configuration file will be created in ~/.config/chwin/settings.cfg

In the configuration file the user can change the window's colors and change the list of windows that should be ignored by chwin.

#### TODO:

create packages for .deb and PKGBUILD


#### Change Log:

* version 0.3
    * added a version that runs in the background and also added a settings manager
* version 0.2
    * fist release


#### JDFlibrary uses the following libraries/software:

* wmctrl
* GTK+ 3
* Python


Refer to the LICENSE file for details on licenses for the above mentioned.


#### chwin License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.<br>

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see:
http://www.gnu.org/licenses/
