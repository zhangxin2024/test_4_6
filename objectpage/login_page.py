# -*- coding: utf-8 -*-
# Time : 2024/1/5 17:29
# Author : Lucy
# File : login_page.py
# Desc :
from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self,driver):
        self.account_elem=By.ID,'account'
        self.password_elem=By.NAME,'password'
        self.login_elem=By.ID,'submit'
        self.ciframe=By.TAG_NAME,"iframe"
        self.user_logout=By.ID,'main-avatar'
        self.logout_elem=By.LINK_TEXT, '退出'
        self.driver=driver
    def input_username(self,username):
        self.driver.find_element(*self.account_elem).clear()
        self.driver.find_element(*self.account_elem).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(*self.password_elem).clear()
        self.driver.find_element(*self.password_elem).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_elem).click()
    def switch_iframe(self):
        self.driver.find_element(*self.ciframe)
    def click_logout(self):
        self.driver.find_element(*self.user_logout).click()
        self.driver.find_element(*self.logout_elem).click()
