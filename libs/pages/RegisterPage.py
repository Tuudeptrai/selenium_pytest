import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from libs.pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage(BasePage):
    PASSWORD_ERROR_ALL = """• At least 10 characters—the more characters, the better
• Requires a mixture of both uppercase and lowercase letters
• Requires a mixture of letters and numbers
• Inclusion of at least one special character, e.g., !@#$%^&*"""

    PASSWORD_ERROR_LETTER_NUMBERS_EXCL = """• At least 10 characters—the more characters, the better
• Requires a mixture of both uppercase and lowercase letters
• Inclusion of at least one special character, e.g., !@#$%^&*"""

    PASSWORD_ERROR_10_CHARS = "• At least 10 characters—the more characters, the better"
    PASSWORD_SPECIAL_CHAR = "• Inclusion of at least one special character, e.g., !@#$%^&*"
    PASSWORD_UPPER_LOWER_CASE = "• Requires a mixture of both uppercase and lowercase letters"

    NOT_ALLOWED_SPECIAL_CHARACTER = "❌ Not allowed special characters (@,#,!,&...)"

    def __init__(self, browser):
        super().__init__(browser)

    def wait_page_loaded(self):
        self.wh.wait_page_loaded(by=By.NAME, value="register-button")

    def click_register_and_handle_recaptcha(self):
        self.browser.find_element(by=By.NAME, value="register-button").click()
        self.wh.wait_page_loaded()
        time.sleep(2)
        recaptcha_token = self.browser.find_elements(
            by=By.XPATH, value="//*[text()=\"recaptcha_token: This field may not be blank.\"]")
        if recaptcha_token and recaptcha_token[0].is_displayed():
            self.logger.info("recaptcha found")
            self.browser.find_element(by=By.NAME, value="register-button").click()
            WebDriverWait(self.browser, 10).until(EC.invisibility_of_element_located(recaptcha_token[0]))
            time.sleep(2)
            self.wh.wait_page_loaded()
        time.sleep(2)
