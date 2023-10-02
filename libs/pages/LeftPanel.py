import time

from assertpy import assert_that
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from libs.pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC

from libs.pages.WalletsPage import WalletsPage


class LeftPanel(BasePage):

    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    def wait_page_loaded(self):
        self.wh.wait_page_loaded(by=By.ID, value="Wallets")

    def navigate(self, tab_name="Wallets", new_window=False):
        self.wh.wait_page_loaded(by=By.ID, value=tab_name, raise_on_error=True)
        self.wh.wait_element_visible(by=By.ID, value=tab_name)
        try:
            self.browser.find_element(by=By.ID, value=tab_name).click()
        except ElementClickInterceptedException:
            time.sleep(1)
            self.browser.find_element(by=By.ID, value=tab_name).click()
        element = self.browser.find_element(by=By.ID, value=tab_name)
        if not new_window:
            self.wh.wait_page_loaded()
            assert_that(element.get_attribute('style'), f"Tab {tab_name} was not selected"
                        ).contains(f"background-color: white")

    def navigate_hor_tab(self, hor_tab_name):
        el = self.wh.wait_element_visible(by=By.XPATH, value=f"//button[contains(text(), '{hor_tab_name}')]")
        el.click()
