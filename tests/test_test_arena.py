import pytest
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.chrome import chrome_browser

administrator_email = 'administrator@testarena.pl'


@pytest.fixture
def browser(chrome_browser):
    chrome_browser.set_window_size(1920, 1080)
    chrome_browser.get('http://demo.testarena.pl/zaloguj')
    chrome_browser.find_element(By.CSS_SELECTOR, '#email').send_keys(administrator_email)
    chrome_browser.find_element(By.CSS_SELECTOR, '#password').send_keys('sumXQQ72$L')
    chrome_browser.find_element(By.CSS_SELECTOR, '#login').click()
    yield chrome_browser


def test_successful_login(browser):
    user_email = browser.find_element(By.CSS_SELECTOR, ".user-info small")
    assert administrator_email == user_email.text


def test_add_message(browser):
    browser.find_element(By.CLASS_NAME, 'icon_mail').click()
    wait = WebDriverWait(browser, 10)
    text_input = (By.ID, 'j_msgContent')
    wait.until(EC.element_to_be_clickable(text_input))
    my_text = generate_random_string(10)
    browser.find_element(*text_input).send_keys(my_text)
    browser.find_element(By.ID, 'j_msgResponse-193').click()
    wait.until(lambda x: browser.find_elements(By.CLASS_NAME, 'message_content_text')[-1].text == my_text)
    assert browser.find_elements(By.CLASS_NAME, 'message_content_text')[-1].text == my_text


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string