# -*- coding: utf-8 -*-

# Author: Milan Nikolic <gen2brain@gmail.com>
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

from threading import Thread

import gtk

class PopupMenu(gtk.Menu):
    """ Popup menu """

    def __init__(self, main_instance):
        """ Constructor """
        gtk.Menu.__init__(self)
        self.main = main_instance

        self.toggle_mute = gtk.CheckMenuItem(_("Mute"))
        self.toggle_mute.set_active(self.main.alsactrl.is_muted())
        self.mute_handler_id = self.toggle_mute.connect("toggled", self.on_toggle_mute)
        self.add(self.toggle_mute)

        self.toggle_mixer = gtk.CheckMenuItem(_("Show Mixer"))
        self.toggle_mixer.set_active(self.main.mixer_get_active())
        self.mixer_handler_id = self.toggle_mixer.connect("toggled", self.on_toggle_mixer)
        self.add(self.toggle_mixer)

        item = gtk.ImageMenuItem("gtk-preferences")
        item.connect("activate", self.show_preferences)
        self.add(item)

        item = gtk.ImageMenuItem("gtk-quit")
        item.connect("activate", self.main.quit)
        self.add(item)

        self.show_all()

    def show_preferences(self, widget=None, data=None):
        """ Show preferences window """
        self.main.preferences.open()

    def on_toggle_mute(self, widget=None):
        """ Toggles mute status """
        self.main.toggle_mute(widget)

    def on_toggle_mixer(self, widget=None):
        """ Start mixer app in new thread """
        Thread(target = self.main.toggle_mixer).start()
