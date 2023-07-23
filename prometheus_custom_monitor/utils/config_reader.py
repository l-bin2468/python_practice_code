# -*- encoding: utf-8 -*-
# Author: Komorebi
# Date: 2023/7/23 18:23
# Describe:
from configparser import ConfigParser
from pathlib import Path

ROOT_PATH = Path(__file__).cwd().resolve().parent
CONFIG_PATH = ROOT_PATH / "configs/config.ini"


class ConfigReader(ConfigParser):
    def __init__(self, filename):
        super(ConfigReader, self).__init__()
        self.read(filenames=filename, encoding="utf-8")


config = ConfigReader(CONFIG_PATH)
host = config.get("Linux", "localhost")
user = config.get("Linux", "username")
pwd = config.get("Linux", "passwd")
