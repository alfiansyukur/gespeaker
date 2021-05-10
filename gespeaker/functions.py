##
#     Project: Gespeaker
# Description: A GTK frontend for espeak
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2009-2021 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

import os.path
from gettext import dgettext as gettext_with_domain
from gettext import gettext as _

from gi.repository import Gtk

from .constants import DIR_UI


def get_ui_file(filename):
    """Return the full path of a Glade/UI file"""
    return os.path.join(DIR_UI, filename)


def readlines(filename, empty_lines=False):
    """
    Read all the text in the specified filename, allowing to skip
    empty lines
    """
    result = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            if line or empty_lines:
                result.append(line)
        f.close()
    return result


def process_events():
    """
    Process every pending GTK+ event
    """
    while Gtk.events_pending():
        Gtk.main_iteration()


def GTK30_(message, context=None):
    """
    Get a translated message from GTK+ 3 domain
    """
    return gettext_with_domain('gtk30',
                               '{CONTEXT}\x04{MESSAGE}'.format(
                                   CONTEXT=context,
                                   MESSAGE=message)
                               if context
                               else message)


__all__ = [
    'get_ui_file',
    'readlines',
    'process_events',
    '_',
    'GTK30_',
]