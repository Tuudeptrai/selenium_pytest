from selenium.webdriver.common.by import By
from utilities import XLUtils

class UploadPage():

    click_continue = "//button[contains(.,'Chọn cây và nhấn để tiếp tục')]"
    click_add_btn = "//button/a/i"
    click_name_tf = "//input[@name='ten']"
    click_name_File = "//input[@name='file']"
    click_add_data_btn = "//input[@value='Thêm dữ liệu']"
    path = "..\\testdata\\Opencart_LoginData.xlsx"

    def __init__(self, driver):
        self.driver = driver

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.click_continue).click()
    def clickAddFile(self):
        self.driver.find_element(By.XPATH,self.click_add_btn).click()
    def clickNameTf(self):
        self.driver.find_element(By.XPATH,self.click_name_tf).click()
    def typeNameFileTf(self):
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        self.driver.find_element(By.XPATH,self.click_name_tf).send_keys(XLUtils.readData(self.path,"Sheet1",1,1))
    def typeNameFileTf2(self):
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("######################## 11111: ###########: ",XLUtils.readData(self.path,"Sheet1",1,1))
        print("######################## 22222: ###########: ",XLUtils.readData(self.path,"Sheet1",2,1))
        self.driver.find_element(By.XPATH,self.click_name_tf).send_keys(XLUtils.readData(self.path,"Sheet1",2,1))
    def typeNameFilePath(self):
        self.driver.find_element(By.XPATH,self.click_name_File).send_keys("C:/Users/vuvan/OneDrive/Desktop/crypto/selenium-pytest/testdata/19HungVuong.jpg")
    def clickAddData(self):
        self.driver.find_element(By.XPATH,self.click_add_data_btn).click()

