# -*- coding: utf-8 -*-
# Time : 2024/1/5 14:45
# Author : Lucy
# File : test_page1.py
# Desc :
import unittest

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 加载服务器
from selenium.webdriver.common.by import By  # 导入by
from time import sleep  # 休眠
from pyconfig.configa import url, driver_path
from objectpage.login_page import LoginPage
from data.data import ReadWrite
from pylog.log1 import loggers
@allure.feature('登录模块')
class TestCases:
    def test_1(self,login):
        print('登录的第一个测试用例')
        self.driver=login
        self.loginpage=LoginPage(self.driver)
        user_list=ReadWrite().excelread('Sheet1')
        username=user_list[0][0]
        password=user_list[0][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(3)
        iframe = self.driver.find_elements(By.TAG_NAME, "iframe")[0]
        self.driver.switch_to.frame(iframe)
        assert '禅道' in self.driver.title
        self.loginpage.click_logout()
        loggers.info('有效的用户名和密码,成功登录系统')

