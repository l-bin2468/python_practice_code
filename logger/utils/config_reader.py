# -*- encoding: utf-8 -*-
# @Author: Administrator
# @Date: 2022/10/11 21:16
# @Describe: 获取配置文件指定数据
import configparser
import os
from pathlib import Path

from utils.yaml_reader import YamlRead


BASE_PATH = Path(__file__).parents[1]
CONFIG_PATH = BASE_PATH / "config"
LOG_PATH = BASE_PATH / "logs"


class ConfigRead(object):
    def __init__(self, conf_name):
        conf = os.path.join(CONFIG_PATH, conf_name)
        if conf_name.endswith('.yml'):
            self.c = YamlRead().get(conf)
        elif conf_name.endswith('.ini'):
            self.cf = configparser.ConfigParser()
            self.cf.read(conf)

    def get(self, element, index=0):
        return self.c[index].get(element)

    def getSections(self):
        return self.cf.sections()

    def getOptions(self, section):
        return self.cf.options(section)

    def getIni(self, section, option):
        return self.cf.get(section, option)


if __name__ == '__main__':
    yml = 'log.yml'
    c = ConfigRead(yml)
    data = c.get('log')
    print(data)
    ini = 'config.ini'
    c = ConfigRead(ini)
    _data = c.getSections()
    print(_data)
    _data1 = c.getOptions('App')
    print(_data1)
    _data2 = c.getIni('App', 'name')
    print(_data2)
