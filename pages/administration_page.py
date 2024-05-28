from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AdministrationPage:
    project_button = (By.CSS_SELECTOR, 'a.button_link[href="http://demo.testarena.pl/administration/add_project"]')
    project_name = (By.ID, 'name')
    prefix_input = (By.ID, 'prefix')
    description_input = (By.ID, 'description')
    save_button = (By.ID, 'save')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def add_new_project(self, text_name_project, text_prefix, text_description):
        self.browser.find_element(*self.project_button).click()
        self.browser.find_element(*self.project_name).send_keys(text_name_project)
        self.browser.find_element(*self.prefix_input).send_keys(text_prefix)
        self.browser.find_element(*self.description_input).send_keys(text_description)
        self.browser.find_element(*self.save_button).click()

        return self