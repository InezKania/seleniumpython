import random
import string
import time

from fixtures.chrome import chrome_browser
from fixtures.testarena.login import browser
from pages.administration_page import AdministrationPage
from pages.home_page import HomePage
from pages.messages_page import MessagesPage
from pages.project_page import ProjectPage

administrator_email = 'administrator@testarena.pl'


def test_successful_login(browser):
    home_page = HomePage(browser)
    user_email = home_page.get_current_user_email()
    assert administrator_email == user_email


def test_add_project(browser):
    text_name_project = 'Projekt A05'
    text_prefix = generate_string(6)
    text_description = generate_string(20)

    home_page = HomePage(browser)
    home_page.click_administration_panel()

    new_project = AdministrationPage(browser)
    new_project.add_new_project(text_name_project, text_prefix, text_description)

    project_page = ProjectPage(browser)
    project_page.verify_project_added(text_name_project)


#def test_find_project(browser, text_name_project): --- nie działa, bo nie widzi textu
    #project_page = ProjectPage(browser)
    #project_page.verify_project_added(text_name_project)



def generate_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
