import pytest

from Config.Config import TestData
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
import time

class Test_Login(BaseTest):
    def test_loginPage_title(self):
        self.LoginPage=LoginPage(self.driver)
        tit=self.LoginPage.do_loginpage_title(TestData.TITLE)
        assert tit==TestData.TITLE
    def test_loginPage_login(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        print(TestData.USER_NAME)
        print(TestData.PASSWORD)

