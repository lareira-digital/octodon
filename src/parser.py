# DISCLAIMER: This parser is heavily based on the work of Emre Yilmaz for
# the stormssh project.

import sys
import logging
from os import makedirs, chmod, walk, symlink, remove
from os.path import dirname, expanduser, exists, join, islink
from shutil import rmtree

from paramiko import SSHConfig

logger = logging.getLogger('octodon')

DEFAULT_SSH_CONFIG_FILE = expanduser("~/.ssh/config")
DEFAULT_SSH_CONFIG_DIR = dirname(DEFAULT_SSH_CONFIG_FILE)
DEFAULT_SSH_ENV_DIR = join(DEFAULT_SSH_CONFIG_DIR, 'envs')


class SSHEnvironment():
    def __init__(self):
        self.check_if_config_exists()

    def check_if_config_exists(self, ssh_config_file=""):
        if not exists(ssh_config_file):
            self.ssh_config_file = DEFAULT_SSH_CONFIG_FILE

        if not exists(self.ssh_config_file):
            if not exists(DEFAULT_SSH_CONFIG_DIR):
                makedirs(DEFAULT_SSH_CONFIG_DIR)
            open(self.ssh_config_file, 'w+').close()
            chmod(self.ssh_config_file, 0o600)

    def parse_file(self):
        config = SSHConfig()
        config_data = []

        with open(self.ssh_config_file) as fd:
            config.parse(fd)

        for entry in config.__dict__.get("_config"):
            config_data.append(entry)
        return config_data

    def get_hosts(self):
        hosts = []
        config_data = self.parse_file()

        for entry in config_data:
            hosts.append(entry.get("host")[0])

        return hosts

    def get_host_detail(self, host):
        config_data = self.parse_file()
        for config in config_data:
            if config['host'][0] == host:
                return config['config']

    def get_environments(self):
        environments = []
        if not exists(DEFAULT_SSH_ENV_DIR):
            makedirs(DEFAULT_SSH_ENV_DIR)
            return False

        envs = walk(DEFAULT_SSH_ENV_DIR)

        for entry in envs:
            environments.append(entry[0].split("/")[-1])
        logger.debug(environments)
        return environments

    def activate_environment(self, environment_name):
        available_environments = self.get_environments()
        if environment_name in available_environments:
            ssh_config_file = join(DEFAULT_SSH_ENV_DIR, environment_name, 'config')
            if exists(ssh_config_file):
                if islink(ssh_config_file) or not exists(DEFAULT_SSH_CONFIG_FILE):
                    remove(ssh_config_file)
                    symlink(ssh_config_file, DEFAULT_SSH_CONFIG_DIR)
                else:
                    sys.exit("WARNING: SSH config file is not a symlink. It may contain information. Aborting.")
            else:
                sys.exit(f"ERROR: Environment {environment_name} does not have a config file.")
        else:
            sys.exit("Environment does not exist.")

    def delete_environment(self, environment_name):
        available_environments = self.get_environments()
        if environment_name in available_environments:
            rmtree(join(DEFAULT_SSH_ENV_DIR, environment_name))
        else:
            sys.exit("Environment does not exist.")
