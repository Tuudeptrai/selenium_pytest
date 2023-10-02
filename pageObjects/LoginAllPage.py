import pytest
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os
import time
from libs.helpers.mail_helper import get_cloudflare_code
from libs.helpers.mail_helper import get_inbox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginAll():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen() 
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    
    def __init__(self, driver):
        self.driver = driver

    fill_username_name = "email"
    fill_password= "password"
    click_login = "btn-user"
    click_button_xpath = "//*[contains(@class,\"Button\")]"
    code_digit = "code"
    fill_email = "//input[@id='email-address']"
    continue_btn = "//*[text()=\"Continue\"]"
    login_btn = "//*[text()=\"Log in\"]"
    # @pytest.mark.login
    def LoginAllFunc(self):

        self.logger.info("******* recycle login func **********")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        email = self.email
        pwd = self.password
        if self.driver.find_elements(By.XPATH, self.click_button_xpath):
            # if cloudflare page opened
            self.driver.find_element(By.NAME, self.fill_username_name).send_keys(email)
            self.driver.find_element(By.XPATH, self.click_button_xpath).click()
            time.sleep(6)
            code = get_cloudflare_code()
            print("da lay ma xac thuc")
            self.driver.find_element(By.NAME, self.code_digit).send_keys(code)
            self.driver.find_element(By.XPATH, self.click_button_xpath).click()
            print("da nhap ma xac thuc")
            time.sleep(10)
            self.wait_page_loaded()
            print("da nhap URL lần 2")
            self.driver.find_element(By.XPATH, self.fill_email).send_keys(email)
            self.driver.find_element(By.XPATH, self.continue_btn).click()
            print("da nhap email lay link dang nhap")
            time.sleep(10)
            link = get_inbox()
            print("da lay link dang nhap", link)
            self.driver.get(link)
            print("da vao link dang nhap")
            time.sleep(10)
            self.wait_page_loaded()
            self.driver.find_element(By.ID, self.fill_password).send_keys(pwd)
            self.driver.find_element(By.XPATH, self.login_btn).click()
            print("da dang nhap")
            time.sleep(10)
    
    def wait_page_loaded(self, by=By.XPATH, value="//*[contains(text(), 'Atato')]", delay=15, raise_on_error=False):  # 'About us'
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            self.wait_element_invisible(
                by=By.XPATH, value="//*[contains(@class, \"chakra-table\")]//*[contains(@class, \"chakra-skeleton\")]")
        except TimeoutException as e:
            self.logger.critical(f"Loading took more {delay} seconds: '{value}'!")
            if raise_on_error:
                raise e
    def wait_element_invisible(self, by=By.ID, value="About us", delay=6):
        WebDriverWait(self.driver, delay).until(EC.invisibility_of_element_located((by, value)))

    def wait_element_visible(self, by=By.ID, value="About us", delay=6):
        WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
        return self.driver.find_element(by=by, value=value)