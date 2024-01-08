# -*- coding: utf-8 -*-
# Time : 2024/1/7 14:49
# Author : Lucy
# File : conftest.py
# Desc :
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 加载服务器
from pyconfig.configa import url, driver_path

@pytest.fixture(scope='session')
def login():
    e = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=e)
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()