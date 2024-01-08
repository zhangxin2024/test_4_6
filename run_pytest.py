# -*- coding: utf-8 -*-
# Time : 2024/1/7 14:58
# Author : Lucy
# File : run_pytest.py
# Desc :通过pytest来运行
import pytest
import subprocess

pytest.main()
subprocess.call('allure generate ./result/temp -o ./result/report --clean',shell=True)#生成报告
subprocess.call('allure open -h 127.0.0.1 -p 8883 ./result/report',shell=True)#打开报告