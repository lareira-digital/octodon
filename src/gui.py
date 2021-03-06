import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from src.handlers import Handler
from src.parser import SSHConfigParser

class GUI():
    """Main user interface class."""

    def __init__(self):
        """Initialize the GUI, get the glade files and tie everything up."""
        self.ssh_config = SSHConfigParser()
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gui/ui2.glade")
        self.builder.connect_signals(Handler(self.builder))

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

        window = self.builder.get_object("main_window")
        window.show_all()
        Gtk.main()  # run the darn thing

    def populate_hosts(self):
        """Populate the hosts list with the information from the parser."""
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
