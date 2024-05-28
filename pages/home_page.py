from selenium.webdriver.common.by import By
from pages.administration_page import AdministrationPage
from pages.messages_page import MessagesPage


class HomePage:
    user_email = (By.CSS_SELECTOR, ".user-info small")
    mail_icon = (By.CLASS_NAME, 'icon_mail')
    administration_panel = (By.CLASS_NAME, 'header_admin')

    def __init__(self, browser):
        self.browser = browser

    def get_current_user_email(self):
        return self.browser.find_element(*self.user_email).text

    def click_mail_icon(self):
        self.browser.find_element(*self.mail_icon).click()
        return MessagesPage(self.browser)

    def click_administration_panel(self):
        self.browser.find_element(*self.administration_panel).click()
        return AdministrationPage(self.browser)
