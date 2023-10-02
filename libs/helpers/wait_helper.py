import logging
from contextlib import contextmanager

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitHelper:

    logger = logging.getLogger(__name__)

    def __init__(self, browser):
        self.browser = browser

    # @contextmanager
    # def wait_for_page_load(self, timeout=30):
    #     old_page = self.browser.find_element_by_tag_name('html')
    #     yield
    #     WebDriverWait(self.browser, timeout).until(staleness_of(old_page))

    def wait_page_loaded(self, by=By.XPATH, value="//*[contains(text(), 'Atato')]", delay=15, raise_on_error=False):  # 'About us'
        try:
            WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((by, value)))
            self.wait_element_invisible(
                by=By.XPATH, value="//*[contains(@class, \"chakra-table\")]//*[contains(@class, \"chakra-skeleton\")]")
        except TimeoutException as e:
            self.logger.critical(f"Loading took more {delay} seconds: '{value}'!")
            if raise_on_error:
                raise e

    def wait_element_invisible(self, by=By.ID, value="About us", delay=6):
        WebDriverWait(self.browser, delay).until(EC.invisibility_of_element_located((by, value)))

    def wait_element_visible(self, by=By.ID, value="About us", delay=6):
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((by, value)))
        return self.browser.find_element(by=by, value=value)

    # def page_has_loaded(self):
    #     self.logger.info("Checking if {} page is loaded.".format(self.browser.current_url))
    #     page_state = self.browser.execute_script('return document.readyState;')
    #     return page_state == 'complete'
    #
    # def wait_page_has_loaded(self):
    #     delay = 5
    #     try:
    #         WebDriverWait(self.browser, delay).until(self.page_has_loaded)
    #     except TimeoutException:
    #         self.logger.exception(f"Loading took too more {delay} seconds!")