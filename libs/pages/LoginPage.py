import time

import pyotp
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from libs.pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC

from libs.pages.WalletsPage import WalletsPage


class LoginPage(BasePage):

    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    def wait_page_loaded(self):
        self.wh.wait_page_loaded(by=By.ID, value="email-address")

    def pass_2fa(self, fa_code, num_retries=3, delay=20):
        time.sleep(1)
        temp_element = self.wh.wait_element_visible(by=By.XPATH, value='//*[contains(@id,"pin-input-")]')
        template = temp_element.get_attribute("id")[:-1]
        totp = pyotp.TOTP(fa_code)
        for i in range(num_retries):
            try:
                otp = totp.now()
                for j in range(len(otp)):
                    self.browser.find_element(by=By.ID, value=f'{template}{j}').send_keys(otp[j])
                self.browser.find_element(by=By.XPATH, value="//button[text()=\"Verify\"]").click()
                WalletsPage(self.browser).wait_page_loaded(delay=delay, raise_on_error=True)
                time.sleep(1)
                break
            except Exception as e:
                if i < num_retries - 1:
                    self.logger.warn(f"{e} Retry...")
                    time.sleep(40-delay)
                else:
                    if num_retries != 1:  # num_retries=1 we use for negative func tests
                        raise e

    def handle_recaptcha(self, value):
        time.sleep(3)
        recaptcha_token = self.browser.find_elements(
            by=By.XPATH, value="//*[text()=\"Recaptcha failed to verify, please try again\"]")
        if recaptcha_token and recaptcha_token[0].is_displayed():
            self.logger.info("recaptcha found")
            self.browser.find_element(by=By.NAME, value=value).click()
            WebDriverWait(self.browser, 10).until(EC.invisibility_of_element_located(recaptcha_token[0]))
            time.sleep(2)
        self.wh.wait_page_loaded()

    def login(self, email, password, fa_code=None):
        if email:  # not needed for example, when we already set it but dismissed 2fa
            element = self.wh.wait_element_visible(by=By.ID, value="email-address")
            element.clear()
            element.send_keys(email)
        if password:
            self.browser.find_element(by=By.ID, value="password").send_keys(password)
        self.browser.find_element(by=By.NAME, value="login-button").click()
        self.handle_recaptcha(value="login-button")
        if fa_code:
            self.pass_2fa(fa_code)

    def login_welcome_back(self, email, password, fa_code=None, workspace=None):
        email_el = self.browser.find_element(by=By.ID, value="email-address")
        email_el.clear()
        email_el.send_keys(email)
        self.browser.find_element(by=By.NAME, value="continue-button").click()
        self.handle_recaptcha(value="continue-button")
        if workspace:
            self.wh.wait_page_loaded(by=By.XPATH, value=f"//*[text()=\"{workspace}\"]", delay=5)
            self.handle_recaptcha(value='continue-button')
            workspace_element = self.wh.wait_element_visible(by=By.XPATH, value=f"//*[text()='{workspace}']")
            workspace_element.click()
        else:
            self.browser.find_element(by=By.XPATH, value=f"//button").click()
        password_element = self.wh.wait_element_visible(by=By.ID, value="password", delay=20)
        password_element.send_keys(password)
        self.browser.find_element(by=By.NAME, value="login-button").click()
        self.handle_recaptcha(value="login-button")
        if fa_code:
            self.pass_2fa(fa_code)
