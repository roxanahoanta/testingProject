from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class LoginPage(BasePage):

    _URL = "https://www.zooplus.ro/checkout/login?notLoggedIn=true"
    EMAIL_INPUT= (By.ID, "customerEmail")
    PASSWORD_INPUT = (By.ID, "customerPassword")
    LOGGIN_BUTTON = (By.XPATH, "//span[text()='Intră în cont']")
    COOKIE_BUTTON = (By.ID, "onetrust-accept-btn-handler")
    NO_ACCOUNT_ERROR = (By.XPATH, "//div[@data-zta='SSOLoginErrorMessage'][@aria-hidden='false']")
    #LOGGIN_BUTTON = (By.CLASS_NAME, "button__group")

    def navigate_to_page(self):
        self.driver.get(self._URL)

    def click_accept_cookie(self):
        self.click(locator=self.COOKIE_BUTTON)

    def set_email(self, email):
        self.type(locator=self.EMAIL_INPUT, text=email)

    def set_password(self,password):
        self.type(text=password, locator=self.PASSWORD_INPUT)

    def click_loggin(self):
        self.click(locator=self.LOGGIN_BUTTON)

    def no_account_error_is_displayed(self):
        return self.is_displayed(self.NO_ACCOUNT_ERROR)





