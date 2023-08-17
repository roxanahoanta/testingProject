from driver2 import Driver
from pages.login_page import LoginPage

def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()

def after_all(context):
    context.browser.close_pyta()