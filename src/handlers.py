# -*- coding: utf-8 -*-
# @Author: Oscar Carballal Prego
# @Date:   2017-04-18 23:25:07
# @Last Modified by:   Oscar Carballal Prego
# @Last Modified time: 2017-04-20 22:54:12

import gi
from gi.repository import Gtk

from .parser import SSHConfigParser


class Handler():
    def __init__(self, builder):
        self.ssh_config = SSHConfigParser()
        self.builder = builder
        self.grid = self.builder.get_object("config_grid")

    def quit_application(self, *args):
        Gtk.main_quit(*args)

    def show_host_config(self, treeview, treepath, column):
        # TODO: This is a piece of crap code, needs to be replaced
        # whether someone likes it or not.
        # Clear the grid before repopulating
        if self.grid.get_children():
            for element in self.grid.get_children():
                self.grid.remove(element)
        selection = treeview.get_selection()
        model, treeiter = selection.get_selected()
        hostconf = self.ssh_config.get_host_detail(model[treeiter][0])
        row_count = 0
        for key in hostconf.keys():
            # Define label
            label = Gtk.Label(key)
            label.set_justify(Gtk.Justification.RIGHT)
            # Define input
            gtkinput = Gtk.Entry()
            if type(hostconf[key]) == list:
                gtkinput.set_text(hostconf[key][0])
            else:
                gtkinput.set_text(hostconf[key])
            self.grid.attach(label, 0, row_count, 1, 1)
            self.grid.attach(gtkinput, 1, row_count, 2, 1)
            row_count += 1
        self.grid.show_all()
        row_count = 0
    
    def add_new_environment(self, *args):
        dialog = self.builder.get_object('dialog_add_environment')
        print(dir(dialog))
        dialog.run()
        # On ok button save details to the file

    def cancel_new_environment(self, dialog):
        dialog.destroy()

    def create_new_environment(self, *args):
        # TODO
        pass
    
    def load_environment(self, combobox):
        print(dir(combobox))
        print("loading environment")
        print(combobox.get_entry_text_column())
        pass