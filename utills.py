import math
import os
import re

from dotenv import load_dotenv
from selenium import webdriver as driver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

load_dotenv()

LESSON_URL = 'https://stepik.org/lesson/201964/step/3?unit=176022'

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

CAPCHA_SUBMIT = '//button[@type="submit"]'

AUTH_LINK = 'https://stepik.org/course/575/promo?auth=login'
LOGIN_FIELD = '//input[@name="login"]'
PASSWORD_FIELD = '//input[@name="password"]'
AUTH_SUBMIT = '//button[@type="submit"]'
COURSE_NAV = '//nav[@aria-label="Навигация по курсу"]'

AGAIN_BUTTON = '//button[contains(@class, "again")]'
ANSWER_FIELD = '//textarea[contains(@placeholder, "ваш ответ")]'
ANSWER_SUBMIT = '//button[@class="submit-submission"]'
NEXT_STEP = '//a[text()="Следующий шаг"]'


def wait_for_element_visible(locator, webdriver):
    return Wait(webdriver, 15).until(
        EC.visibility_of_element_located((
            By.XPATH, locator
        ))
    )


def wait_for_element_clickable(locator, webdriver):
    return Wait(webdriver, 15).until(
        EC.element_to_be_clickable((By.XPATH, locator))
    )


def find_element_by(by, locator, webdriver):
    return webdriver.find_element(getattr(By, by), locator)


def auth_to_stepik(webdriver):
    webdriver.get(AUTH_LINK)
    wait_for_element_clickable(LOGIN_FIELD, webdriver).send_keys(LOGIN)
    wait_for_element_clickable(PASSWORD_FIELD, webdriver).send_keys(PASSWORD)
    wait_for_element_clickable(AUTH_SUBMIT, webdriver).click()
    wait_for_element_visible(COURSE_NAV, webdriver)


def send_answer_to_stepik(lesson_url, alert, again=False):
    answer = float(
        alert.text.rsplit(maxsplit=1)[-1]
    )
    with driver.Chrome() as webdriver:
        auth_to_stepik(webdriver)
        webdriver.get(lesson_url)
        if again:
            wait_for_element_clickable(AGAIN_BUTTON, webdriver).click()
            wait_for_element_clickable(ANSWER_FIELD, webdriver)
        wait_for_element_visible(ANSWER_FIELD, webdriver).clear()
        wait_for_element_visible(ANSWER_FIELD, webdriver).send_keys(answer)
        wait_for_element_clickable(ANSWER_SUBMIT, webdriver).click()
        wait_for_element_visible(NEXT_STEP, webdriver)


def solve_captcha(webdriver):
    input_value = int(find_element_by('ID', 'input_value', webdriver).text)
    result = str(math.log(abs(12*math.sin(int(input_value)))))
    find_element_by('ID', 'answer', webdriver).send_keys(result)
    find_element_by('XPATH', CAPCHA_SUBMIT, webdriver).click()


def solve_quiz_and_get_code(webdriver, send_answer=False):
    alert = webdriver.switch_to.alert
    x = re.search(r'\S\d+', alert.text)[0]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    # try:
    #     alert = webdriver.switch_to.alert
    #     if send_answer:
    #         send_answer_to_stepik(LESSON_URL, alert,  True)
    #     alert.accept()
    # except NoAlertPresentException:
    #     print('Wrong answer')
