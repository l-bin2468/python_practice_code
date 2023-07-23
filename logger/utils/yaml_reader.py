# -*- encoding: utf-8 -*-
# @Author: Administrator
# @Date: 2022/10/11 21:16
# @Describe: 获取yml文件全部数据
from pathlib import Path

import yaml


class YamlRead(object):
    def get(self, yml_path=None):
        if Path(yml_path).exists():
            with open(yml_path, 'r', encoding='utf-8') as f:
                data = list(yaml.safe_load_all(f.read()))
            return data
        else:
            raise FileNotFoundError("YML配置文件不存在！")


if __name__ == '__main__':
    yml_path = r'D:\JetBrains\IntelliJ IDEA 2021.1.3\Workspaces\log_test\config\log.yml'
    yml_data = YamlRead().get(yml_path)
    print(yml_data)
