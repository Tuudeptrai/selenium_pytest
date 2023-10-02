from selenium.webdriver.common.by import By


class HomePage():
    menu_login_link = "//a[contains(text(),'My Account')]"
    menu_shop_link = "//a[contains(text(),'Shop')]"

    def __init__(self, driver):
        self.driver = driver

    def clickLinklogin(self):
        self.driver.find_element(By.XPATH,self.menu_login_link).click()

    def clickLinkshop(self):
        self.driver.find_element(By.XPATH,self.menu_shop_link).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()

