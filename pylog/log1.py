# -*- coding: utf-8 -*-
# Time : 2024/1/6 18:21
# Author : Lucy
# File : log1.py
# Desc :unittest
import logging
from pyconfig.configa import log_file_path

# 创建日志器
loggers = logging.getLogger()
# 定义日志器的级别
loggers.setLevel(logging.INFO)
# 定义处理器的格式
format1 = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
logFile = log_file_path
# 创建处理器
fh = logging.FileHandler(logFile, mode='a', encoding='utf-8')
# 设置处理器的级别
fh.setLevel(logging.INFO)
# 设置处理器的格式
fh.setFormatter(format1)
# 添加到日志器
loggers.addHandler(fh)
