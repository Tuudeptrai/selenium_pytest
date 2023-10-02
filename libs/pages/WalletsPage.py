from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


from libs.pages.BasePage import BasePage


class WalletsPage(BasePage):

    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    def wait_page_loaded(self, raise_on_error=False, delay=15):
        self.wh.wait_page_loaded(by=By.ID, value="get-started-flex", delay=delay, raise_on_error=raise_on_error)


