# -*- coding: utf-8 -*-
# Time : 2024/1/5 18:32
# Author : Lucy
# File : config.py
# Desc :unittest路径配置
import os

root_path=os.path.dirname(os.path.dirname(__file__))
url='http://localhost/zentao/user-login-L3plbnRhby8=.html'
driver_path=root_path+r'/driver/chromedriver.exe'
case_path=root_path+r'/test_demo'
# report_path=root_path+r'/report'
log_file_path=root_path+r'/pylog/log1.txt'
