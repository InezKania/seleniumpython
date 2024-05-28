from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class ProjectPage:
    menu_project_button = (By.CLASS_NAME, 'activeMenu')
    search_input = (By.ID, 'search')
    search_button = (By.ID, 'j_searchButton')
    project_name_on_list = (By.CSS_SELECTOR, 'td:nth-child(1)')


    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)


    def verify_project_added(self, text_name_project):
        self.browser.find_element(*self.menu_project_button).click()
        self.browser.find_element(*self.search_input).send_keys(text_name_project)
        self.browser.find_element(*self.search_button).click()

        try:
            self.wait.until(lambda x: any(text_name_project in element.text for element in
                                          self.browser.find_elements(*self.project_name_on_list)))
        except TimeoutException:
            print(
                f"Error: The expected text '{text_name_project}' was not found in any message_content_text element within the given time.")
