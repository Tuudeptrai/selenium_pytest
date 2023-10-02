import time

import pyotp
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from libs.pages.BasePage import BasePage


class TwoFactorAuth(BasePage):

    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    def wait_page_loaded(self):
        self.wh.wait_page_loaded(by=By.XPATH, value="//*[text()=\"Two-factor Authentication\"]")

    def pass_2fa(self):
        self.wait_page_loaded()
        self.browser.find_element(by=By.XPATH, value="//*[@data-testid=\"next-btn\"]").click()
        self.browser.find_element(by=By.XPATH, value="//*[@aria-label=\"copy secret\"]").click()
        FA_Code = pyperclip.paste()
        totp = pyotp.TOTP(FA_Code)
        self.browser.find_element(by=By.XPATH, value="//*[@data-testid=\"next-btn\"]").click()
        time.sleep(1)
        for i in range(5):
            try:
                otp = totp.now()
                for _ in range(len(otp)):
                    self.browser.find_element(by=By.ID, value=f'pin-input-9-{i}').send_keys(otp[i])
                break
            except Exception as e:
                print(e, "Retry...")
                time.sleep(40)
        self.browser.find_element(by=By.XPATH, value="//button[text()=\"Enable\"]").click()
        time.sleep(2)
        return FA_Code

