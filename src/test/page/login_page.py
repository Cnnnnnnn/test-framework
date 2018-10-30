# -*- coding: utf-8 -*-
from src.test.common.page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    Username = (By.NAME, 'phone')
    Password = (By.NAME, 'password')
    login_button = (By.XPATH, '//div[@class="title"]/form/button')

    def login(self, role):
        if role == 1:  # 售后
            phone = 13412345678
            password =
        elif role == 2:  # 市场
            phone = 18866666666
            password =
        elif role == 3:  # 财务
            phone = 13411110001
            password =

        self.find_element(*self.Username).clear()
        self.find_element(*self.Username).send_keys(str(phone))
        self.find_element(*self.Password).clear()
        self.find_element(*self.Password).send_keys(str(password))
        self.find_element(*self.login_button).click()

