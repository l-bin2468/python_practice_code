# -*- encoding: utf-8 -*-
# Author: Komorebi
# Date: 2023/7/23 18:05
# Describe:
import paramiko

from utils.config_reader import *


class ConnLinux(object):
    def __init__(self):
        # 创建一个ssh client对象
        self.ssh = paramiko.SSHClient()

        # 允许连接不在know_host中的主机
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接主机
        self.ssh.connect(
            hostname=host,
            port=22,
            username=user,
            password=pwd
        )

    def exec_command(self, command):
        """
        执行命令
        stdin 标准输入,也就是我们输入的命令
        stdout 标准输出,命令执行的结果
        stderr 命令执行过程中的错误
        """
        stdin, stdout, stderr = self.ssh.exec_command(command)

        # 读取结果
        res, err = stdout.read().decode("utf-8"), stderr.read().decode("utf-8")
        result = res if res else err

        # 关闭client对象
        self.ssh.close()
        return result


connLinux = ConnLinux()
