# Copyright (C) 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002,
# 2003, 2004, 2005, 2006, 2007, 2008, 2009  Free Software Foundation,
# Inc.
# This Makefile.in is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.



# vim:set noet ts=4:
#
# ibus-tmpl - The Input Bus template project
#
# Copyright (c) 2007-2011 Peng Huang <shawn.p.huang@gmail.com>
# Copyright (c) 2011 Ryo Onodera <ryoqun@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

install:
	install -c ibus-engine-satsuki "/usr/local/bin"
	mkdir -p "/usr/share/ibus/component"
	install -c -m 644 satsuki.xml "/usr/share/ibus/component"
	mkdir -p "/usr/local/share/satsuki"
	install -c -m 644 engine.py factory.py main.py satsuki_sm.py "/usr/local/share/satsuki"
	mkdir -p "/usr/local/share/satsuki/icons"
	install -c -m 644 satsuki.svg anthy.svg "/usr/local/share/satsuki/icons"

test:
	env \
		LANG=en_US \
		python ./main.py
