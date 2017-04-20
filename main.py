# -*- coding: utf-8 -*-
# @Author: oscarcp
# @Date:   2017-04-18 23:21:38
# @Last Modified by:   Oscar Carballal Prego
# @Last Modified time: 2017-04-20 17:28:49

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio
from gui.handlers import Handler

from parser import SSHConfigParser

class GUI():
    def __init__(self):
        self.ssh_config = SSHConfigParser()
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gui/ui.glade")
        self.builder.connect_signals(Handler())

        # Styles
        css_provider = Gtk.CssProvider()
        css = open('gui/styles.css', 'rb')  # rb needed for python 3 support
        css_data = css.read()
        css.close()
        css_provider.load_from_data(css_data)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        # Put the data in place
        self.populate_hosts()
        self.populate_envs()

        # menu = Gio.Menu()
        # # 新建三个菜单选项
        # item_new = Gio.MenuItem.new("New", "app.new")
        # item_about = Gio.MenuItem.new("About", "app.about")
        # item_quit = Gio.MenuItem.new("Quit", "app.quit")
        # menu.append_item(item_new)
        # menu.append_item(item_about)
        # self.set_app_menu(menu)
        # Show the world!
        window = self.builder.get_object("main_window")
        window.show_all()
        Gtk.main()  # run the darn thing

    def populate_hosts(self):
        # Populate list
        host_list = self.ssh_config.get_hosts()
        list_store = self.builder.get_object("hosts_list")
        for host in host_list:
            list_store.append([host])

    def populate_envs(self):
        environment_list = self.ssh_config.get_environments()
        list_store = self.builder.get_object("environment_list")
        if environment_list:
            for environment in environment_list:
                list_store.append([environment])
        else:
            list_store.append(["No environments"])


if __name__ == "__main__":
    gui = GUI()
