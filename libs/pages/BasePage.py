import logging
import string

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from libs.helpers.wait_helper import WaitHelper


class BasePage:
    logger = logging.getLogger(__name__)

    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.wh = WaitHelper(self.browser)

    @staticmethod
    def fill_form_by_ids(browser: WebDriver, **args):
        for k, v in args.items():
            browser.find_element(by=By.ID, value=k).send_keys(v)

    @staticmethod
    def fill_form_by_names(browser: WebDriver, **args):
        for k, v in args.items():
            browser.find_element(by=By.NAME, value=k).send_keys(v)

    @staticmethod
    def get_input_value_by_label(browser: WebDriver, label: string):
        try:
            return browser.find_element(By.XPATH, value=f"//*[contains(text(), '{label}')]/../input").get_attribute(
                'value')
        except NoSuchElementException:
            return browser.find_element(By.XPATH, value=f"//*[contains(text(), '{label}')]/../textarea").get_attribute(
                'value')

    @staticmethod
    def get_lower_text_by_label(browser: WebDriver, label: string):
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                        f"//*[contains(text(), '{label}')]")))
        try:
            return browser.find_element(By.XPATH, value=f"//*[contains(text(), '{label}')]/../p[2]").text
        except NoSuchElementException:
            return browser.find_element(By.XPATH, value=f"//*[contains(text(), '{label}')]/../a/p").text

    @staticmethod
    def set_input_value_by_label(browser: WebDriver, label: str, value: str):
        try:
            el = browser.find_element(By.XPATH, value=f"//*[contains(text(), '{label}')]/..//input")
        except NoSuchElementException:
            el = browser.find_element(By.XPATH, value=f"//*[contains(text(), '{label}')]/..//textarea")
        el.clear()
        el.send_keys(value)

    @staticmethod
    def set_selector_value_by_label(browser: WebDriver, label, value):
        browser.find_element(By.XPATH, value=f"//*[contains(text(), '{label}')]/..//div[contains(@class, \"chakra-select__icon-wrapper\")]/..").click()
        browser.find_element(
            By.XPATH, value=f"//*[contains(text(), '{label}')]/..//option[contains(text(), \"{value}\")]").click()

    @staticmethod
    def get_button_locator_by_label(browser: WebDriver, label: str):
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                       f"//button[contains(text(), '{label}')]")))
        exact_match = browser.find_elements(By.XPATH, value=f"//button[text()= '{label}']")
        if exact_match:
            return exact_match[0]
        else:
            return browser.find_element(By.XPATH, value=f"//button[contains(text(), '{label}')]")
