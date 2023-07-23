# -*- encoding: utf-8 -*-

import logging
import sys

import colorlog


class Logger(object):
    def __init__(self, name=None, log_level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        # 日志文件名
        self.logfile_name = "logs/test.log"

        # 控制台输出格式
        self.console_fmt = '%(log_color)s%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s'
        # 日志文件输出格式
        self.file_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

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
            # 输出到控制台
            sh = logging.StreamHandler()
            # 打印该等级以上内容到控制台
            sh.setLevel(logging.DEBUG)

            # 输出到日志文件
            fh = logging.FileHandler(self.logfile_name)
            # 打印该等级以上内容到文件
            fh.setLevel(logging.INFO)

            # 第四步，定义handler的输出格式
            console_format = colorlog.ColoredFormatter(
                self.console_fmt,
                log_colors=self.color)
            formatter = logging.Formatter(self.file_fmt)
            sh.setFormatter(console_format)
            fh.setFormatter(formatter)

            self.logger.addHandler(sh)
            self.logger.addHandler(fh)
        return self.logger


# logger = Logger().get_log()


if __name__ == '__main__':
    logger = Logger("FRAME").get_log()
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')
    print(sys.platform)
    print(logger.__class__)

