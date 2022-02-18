

"""This is the parent of all pages"""
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.support import  expected_conditions as EC
"""it  contain all generic methods and utilites for all the pages"""

class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def exp_wait_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(by_locator)).click()
    def exp_wait_sendkeys(self,locator,text):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator)).send_keys(text)
    def exp_wait_gettext(self,by_locator):
        ele=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(by_locator))
        return ele.text
    def exp_wait_gettitle(self,title):
        WebDriverWait(self.driver,10).until(EC.title_is(title))
        return self.driver.title
