# -*- encoding: utf-8 -*-
# @Author: Administrator
# @Date: 2022/10/11 21:16
# @Describe:
import logging
import os
import re
import time
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path


class MyTimedRotatingFileHandler(TimedRotatingFileHandler):
    """
    时间为切割点日志
    """
    def getFilesToDelete(self):
        """
        Determine the files to delete when rolling over.
        More specific than the earlier method, which just used glob.glob().
        """
        dirName, baseName = os.path.split(self.baseFilename)
        fileNames = os.listdir(dirName)
        result = []
        for fileName in fileNames:
            #
            if self.extMatch.match(fileName):
                result.append(os.path.join(dirName, fileName))
        if len(result) < self.backupCount:
            result = []
        else:
            result.sort()
            result = result[:len(result) - self.backupCount]
        return result


def split_file_name(default_name):
    """
    修改日志文件名称
    """
    file_path = default_name.split('default.log.')
    return ''.join(file_path)


def setup_log(log_name):
    # 创建logger对象,log_name: 日志名字
    logger_obj = logging.getLogger(log_name)
    # log文件夹路径
    logger_folder_path = Path(__file__).parent / 'logs'
    # 创建log文件夹
    logger_folder_path.mkdir(exist_ok=True)
    date = time.strftime("%Y-%m-%d_%H-%M-%S") + ".log"
    # loge文件路径
    log_file_path = os.path.join(logger_folder_path, date)
    # when="MIDNIGHT", interval=1,表示每天0点为更新点，每天生成一个文件
    logger_handler = MyTimedRotatingFileHandler(filename=log_file_path, when='S', interval=1, backupCount=5,
                                                encoding='utf-8')
    # 处理日志文件名称
    # logger_handler.namer = split_file_name

    # 修改后缀suffix,生成.log文件
    # extMatch是编译好正则表达式，用于匹配日志文件名后缀
    # 需要注意的是suffix和extMatch一定要匹配的上，如果不匹配，过期日志不会被删除
    logger_handler.suffix = f"{logger_handler.suffix}.log"
    # when=S: r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}(.log)$"
    # when=M: r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}(.log)$"
    # when=H: r"^\d{4}-\d{2}-\d{2}_\d{2}(.log)$"
    # when=D or MIDNIGHT : r"^\d{4}-\d{2}-\d{2}(.log)$"
    # when=W: r"^\d{4}-\d{2}-\d{2}(.log)$"
    logger_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}(.log)$", re.ASCII)

    # 创建日志输出格式
    logger_formatter = logging.Formatter(
        "[%(asctime)s] [%(process)d] [%(levelname)s] - %(module)s.%(funcName)s (%(filename)s:%(lineno)d) - %(message)s")

    # 配置日志输出格式
    logger_handler.setFormatter(logger_formatter)

    # 增加日志处理器
    logger_obj.addHandler(logger_handler)

    # 设置日志的记录等级,常见等级有: DEBUG<INFO<WARING<ERROR
    logger_obj.setLevel(logging.INFO)

    return logger_obj


if __name__ == "__main__":
    logger = setup_log("llz_log")
    n = 1
    while True:
        logger.info(f"this is info message")
        time.sleep(1)
        logger.warning(f"this is a warning message")
        n += 1
