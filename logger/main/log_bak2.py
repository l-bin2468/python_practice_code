# -*- encoding: utf-8 -*-
# @Author: Administrator
# @Date: 2022/10/12 20:09
# @Describe:
import logging
import time

import colorlog

from main import log_time
from utils.config_reader import ConfigRead, LOG_PATH


class Logger(object):
    def __init__(self, name=None, log_level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        c = ConfigRead('log.yml').get('log')
        # 日志文件名
        logfile_name = c.get('file_name')
        self.logfile_path = LOG_PATH / logfile_name
        # 控制台输出等级
        self.console_level = c['level'].get('console_level')
        # 日志文件输出等级
        self.file_level = c['level'].get('file_level')
        # 控制台输出格式
        self.console_fmt = c['format'].get('console_fmt')
        # 日志文件输出格式
        self.file_fmt = c['format'].get('file_fmt')
        # 文件备份个数
        self.backupCount = c['backupCount']
        # 文件备份间隔时间
        self.when = c['when']
        # 文件匹配正则表达式
        self.regular = c['regular']

        # 日志颜色
        self.color = {
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "FATAL": "purple"
        }

    def get_log(self):
        # 避免重复打印日志
        if not self.logger.handlers:
            # 定义控制台日志输出格式
            console_format = colorlog.ColoredFormatter(
                self.console_fmt,
                log_colors=self.color
            )
            # 输出到控制台
            sh = logging.StreamHandler()
            # 打印该等级以上内容到控制台
            sh.setLevel(self.console_level)
            # 控制台设置格式
            sh.setFormatter(console_format)

            # 输出到日志文件
            fh = log_time.MyTimedRotatingFileHandler(
                filename=self.logfile_path,
                when=self.when,
                interval=1,
                backupCount=self.backupCount,
                encoding='utf-8'
            )
            # 修改日志文件名称
            fh.namer = log_time.split_file_name
            # 修改日志文件后缀
            fh.suffix = f'{fh.suffix}.log'
            # 定义日志文件输出格式
            file_fmt = logging.Formatter(self.file_fmt)
            # 打印该等级以上内容到文件
            fh.setLevel(self.file_level)
            # 文件设置格式
            fh.setFormatter(file_fmt)

            self.logger.addHandler(sh)
            self.logger.addHandler(fh)
        return self.logger


if __name__ == '__main__':
    logger = Logger("FRAME").get_log()
    n = 1
    while True:
        logger.info('info message')
        time.sleep(0.1)
        logger.warning('warning message')
        n += 1
