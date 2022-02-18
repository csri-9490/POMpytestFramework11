from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL=(By.XPATH,"//input[@id='email']")
    PASSWORD=(By.XPATH,"//input[@id='pass']")
    LOGIN_BUTTON=(By.XPATH,"//button[@id='u_0_h_gq']")
    def __init__(self,driver):
        super().__init__(driver)

    def do_loginpage_title(self,title):
        return self.exp_wait_gettitle(title)
    def do_login(self,username,password):
        self.exp_wait_sendkeys(self.EMAIL,username)
        self.exp_wait_sendkeys(self.PASSWORD,password)
        # self.exp_wait_click(self.LOGIN_BUTTON)
        # self.driver.find_element(LoginPage.LOGIN_BUTTON).click()


