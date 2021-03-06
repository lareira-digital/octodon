# octodon

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/esmorga/Lobby)

octodon is a configuration editor for SSH config files.

![Screenshot](http://i.imgur.com/k9KUCCl.png)

# Why?

It may look like octodon is trying to fix a non-existent problem, but it's
not like that. Imagine that you work for two companies or you have one laptop
that you use for both your personal work and the company where you're in.

Now, unfortunately both situations require to use a GitHub account and you have
in your configuration specific instructions as to the user, port etc. to use
for your github account, but also for the company and both cannot coexist in
the configuration file. This program fixes that situation.

# Features

- Environments: It supports multiple separate environments for config files/keys
- Search: Search for your hosts instead of scrolling through hundreds of entries.

# Requirements

* GTK3+
* Python 3.7+
* Python GObject
* Paramiko

# How to install

## Arch Linux (from AUR)

    $ yay -S octodon-git

## Manually

    $ git clone https://git.sr.ht/~oscarcp/octodon
    $ cd octodon
    $ ./octodon

# How to run (terminal)

    $ ./octodon
    usage: octodon [-h] [-g] [-l] [-c CREATE] [-a ACTIVATE] [-r REMOVE]

    Octodon SSH environments selector and editor.

    optional arguments:
      -h, --help            show this help message and exit
      -g, --gui             start the graphical interface
      -l, --list            list all available environments
      -c CREATE, --create CREATE
                            create a new environment
      -a ACTIVATE, --activate ACTIVATE
                            change to the specified environment
      -r REMOVE, --remove REMOVE
                            delete an environment. WARNING: This will delete your keys as well!

# License

MIT License

# Credits

Although this project was in my head for a long time, I have to give thanks to
[emre](https://github.com/emre) and his [storm project](https://github.com/emre/storm)
for giving me the inspiration and some ideas on how to start.
