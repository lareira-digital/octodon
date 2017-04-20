# -*- coding: utf-8 -*-
# @Author: Oscar Carballal Prego
# @Date:   2017-04-18 23:25:07
# @Last Modified by:   Oscar Carballal Prego
# @Last Modified time: 2017-04-20 22:54:12

import gi
from gi.repository import Gtk

from .parser import SSHConfigParser


class Handler():
    def __init__(self):
        self.ssh_config = SSHConfigParser()

    def quit_application(self, *args):
        Gtk.main_quit(*args)

    def show_host_config(self, treeview, treepath, column):
        selection = treeview.get_selection()
        model, treeiter = selection.get_selected()
        self.ssh_config.get_host_detail(model[treeiter][0])
