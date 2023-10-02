import pytest
from pageObjects.HomePage import HomePage
from pageObjects.UploadPage import UploadPage
from pageObjects.LoginPage import LoginPage
from pageObjects.LoginAllPage import LoginAll
from utilities.readProperties import ReadConfig
from utilities.readjsonData import ReadJson
from utilities.readJsonScreenshot import ReadJsonScreenshot 
from utilities.customLogger import LogGen
from utilities.randomeString import RanDom
from selenium.webdriver.common.by import By
import json
import requests
import jsonpath
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class Test_Login():
    
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    approver_code = 0
    approver_id = ""
    rule_id = ""
    wallet_id =""
    public_key=""
    operation_id=""
    @pytest.fixture(autouse=True)
    def run_around_tests(self, setup):
        
        print("******* run before each test **********")
        self.driver = setup
        # self.la=LoginAll(self.driver)
        # self.la.LoginAllFunc()

    # @pytest.mark.jira("PR-1316", "PR-1961")
    # def test_login_pass_home_page(self):
    #     header = self.driver.find_element(By.XPATH, value="//h1[contains(.,'Wallets')]").text
    #     assert header == "Wallets"
    
    # @pytest.mark.jira("PR-0001")
    # def test_create_approver(self) :
    #         baseUrl = "https://qa-api.atato.com/workspace/my-workspace/api/custody/approvers"
    #         inputData = {"name":"010101001001'"+RanDom.random_string_generator(5)+"'"}
    #         headers = {
    #                 "Content-Type": "application/json; charset=utf-8",
    #                 "Authorization": "Bearer " + ReadConfig.getBearToken()
    #             }
    #         response = requests.post(url=baseUrl,json=inputData,headers=headers )
    #         print("AAAAAAAAAAAAAAAa", response.text)
    #         responseJson = json.loads(response.text)
    #         self.approver_code = responseJson["data"]["activation_code"]
    #         self.approver_id = responseJson["data"]["approver_id"]
    #         a = {
    #             "approver_code": self.approver_code,
    #             "approver_id": self.approver_id,
    #             "rule_id": self.rule_id,
    #             "wallet_id": self.wallet_id,
    #             "public_key": self.public_key,
    #             "operation_id": self.operation_id,
    #             "approver_name": inputData
    #         }
    #         ReadJson.writetoafile(a)
    #         print("apruve code day nha em", self.approver_code)
    #         print("apruve id day nha em", self.approver_id)
    #         print("apruve name day nha em", inputData)

    
           
    def test_get_approver(self) :
            baseUrl = "https://qa-api.atato.com/workspace/my-workspace/api/custody/approvers?skip=0&limit=1000"
            headers = {
                    "Content-Type": "application/json; charset=utf-8",
                    "Authorization": "Bearer " + ReadConfig.getBearToken()
                }
            response = requests.get(url=baseUrl,headers=headers )
            
            responseJson = json.loads(response.text)
            print("AAAAABBBBB", responseJson["data"])
            ab="" 
            for i in responseJson["data"]:
                if str(i["id"]) == "99e37ec5-3fd9-4867-a84d-e255f40a460f": #ReadJson.geinputData()["approver_id"]:
                    ab = i["public_key"]
                    print("AAAAABBBBB", responseJson["data"])
                    a = {
                        "approver_code": ReadJson.geinputData()["approver_code"],
                        "approver_id": ReadJson.geinputData()["approver_id"],
                        "rule_id": self.rule_id,
                        "wallet_id": self.wallet_id,
                        "public_key": ab,
                        "operation_id": self.operation_id,
                        "approver_name": ReadJson.geinputData()["approver_name"]
                    }
                    ReadJson.writetoafile(a)
            print("public_key code day nha em",  ReadJson.geinputData()["public_key"])
           
    
    
    # def test_active_approver(self) :
    #         baseUrl = "https://qa-api.atato.com/workspace/my-workspace/api/custody/approvers/'"+ReadJson.geinputData()["approver_id"]+"'/activate"
    #         headers = {
    #                 "Content-Type": "application/json; charset=utf-8",
    #                 "Authorization": "Bearer " + ReadConfig.getBearToken()
    #             }
    #         inputData= {"activation_code":ReadJson.geinputData()["approver_code"],"public_key":"BGeHd9I77wnoyfz3CoDx/z6APYqoFr+O23uN2zEYwFgNniPEu7qJ+gKGw9k1rrwnUgyYOQ/pZqQIy90xbo8ZNno=","type":"iOS","is_offline": "true" }
    #         response = requests.post(url=baseUrl,json=inputData,headers=headers )
            
    #         # responseJson = json.loads(response.text)
    #         print("AAAAABBBBBAAAAA", response.text)
            
    
    # @pytest.mark.jira("PR-0002")
    # def test_create_rule(self) :
    #         print(ReadJson.geinputData()["approver_id"])
    #         baseUrl = "https://qa-api.atato.com/workspace/my-workspace/api/custody/rule-templates"
    #         inputData = {"name":"rule test '"+RanDom.random_string_generator(5)+"'","network_id":"84703c2b-2c33-4ebf-b195-ab3ec8beda71","approvers":[ReadJson.geinputData()["approver_id"]],"conditions":[],"action":"send_to_approver","type":"transfer"}
    #         headers = {
    #                 "Content-Type": "application/json; charset=utf-8",
    #                 "Authorization": "Bearer " + ReadConfig.getBearToken()
    #             }
    #         response = requests.post(url=baseUrl,json=inputData,headers=headers )
    #         print("BBBBBBBBBBBBBa", response.text)
    #         responseJson = json.loads(response.text)
    #         self.rule_id = responseJson["data"]["id"]
    #         a = {
    #             "approver_code": ReadJson.geinputData()["approver_code"],
    #             "approver_id": ReadJson.geinputData()["approver_id"],
    #             "rule_id": self.rule_id,
    #             "wallet_id": self.wallet_id,
    #             "approver_name": ReadJson.geinputData()["approver_name"]
    #         }
    #         ReadJson.writetoafile(a)
    #         print("ruleid day nha em", self.rule_id)

    # # @pytest.mark.jira("PR-0003")
    # def test_create_walet(self) :
    #         print(ReadJson.geinputData()["approver_id"])
    #         baseUrl = "https://qa-api.atato.com/workspace/my-workspace/api/custody/wallets"
    #         inputData = {"name":"test rain '"+RanDom.random_string_generator(5)+"'","approvers":[ReadJson.geinputData()["approver_id"]],"description":"test rain 1","rules":[ReadJson.geinputData()["rule_id"]],"network_id":"84703c2b-2c33-4ebf-b195-ab3ec8beda71","is_mainnet":"false"}

    #         headers = {
    #                 "Content-Type": "application/json; charset=utf-8",
    #                 "Authorization": "Bearer " + ReadConfig.getBearToken()
    #             }
    #         response = requests.post(url=baseUrl,json=inputData,headers=headers )
    #         print("CCCCCCCCCCCCa", response.text)
    #         responseJson = json.loads(response.text)
    #         self.wallet_id = responseJson["data"]["id"]
    #         a = {
    #             "approver_code": ReadJson.geinputData()["approver_code"],
    #             "approver_id": ReadJson.geinputData()["approver_id"],
    #             "rule_id": ReadJson.geinputData()["rule_id"],
    #             "wallet_id": self.wallet_id,
    #             "approver_name": ReadJson.geinputData()["approver_name"]
    #         }
    #         ReadJson.writetoafile(a)
    #         print("ruleid day nha em", self.rule_id)
    
    # def test_get_operation(self) :
    #             baseUrl = "https://qa-api.atato.com/workspace/my-workspace/api/custody/operations?skip=0&limit=10&wallet_id="+ ReadJson.geinputData()["wallet_id"]
    #             headers = {
    #                     "Content-Type": "application/json; charset=utf-8",
    #                     "Authorization": "Bearer " + ReadConfig.getBearToken()
    #                 }
    #             response = requests.get(url=baseUrl,headers=headers )
                
    #             responseJson = json.loads(response.text)
    #             print("AAAAABBBBB", response.text)
    #             for i in responseJson["data"]:
                   
    #                     a = {
    #                         "approver_code": ReadJson.geinputData()["approver_code"],
    #                         "approver_id": ReadJson.geinputData()["approver_id"],
    #                         "rule_id": ReadJson.geinputData()["rule_id"],
    #                         "wallet_id": ReadJson.geinputData()["wallet_id"],
    #                         "public_key": self.public_key,
    #                         "operation_id": i["id"],
    #                         "approver_name": ReadJson.geinputData()["approver_name"]
    #                     }
    #                     ReadJson.writetoafile(a)
    #             print("public_key code day nha em", ReadJson.geinputData()["operation_id"])

    # def test_active_wallet(self) :
    #             baseUrl = "https://qa-api.atato.com/workspace/my-workspace/api/custody/vote"
    #             inputData ={"operation_id": ReadJson.geinputData()["operation_id"],"approver_id": ReadJson.geinputData()["approver_id"],"approval_type":"APPROVE",
    #             "signature":"MEQCIEwAlpNGX8RLf0M+hNsXgXvhbSNBmoedL6SyJ2ac791bAiBXLTOeBOBbtVKRYTD0SD+auc7IHvTPfBoSuOpwYrCwIg==","encoded_request":"eyJyZXF1ZXN0X3V1aWQiOiJjODAzODE3ZS1iMjIzLTQwZmEtOTVjYy02ZTEwZjU4MWY3OGUiLCJ3YWxsZXRfaWQiOiI0ZWI5OWY1Zi1hOGY5LTQwZjItYTE4ZS03MjY2Y2YyNGIxOTUiLCJ3b3Jrc3BhY2UiOiJteS13b3Jrc3BhY2UiLCJhbXBjX3ZlcnNpb24iOiJ2My4wIiwic291cmNlIjoie1wiZGV2aWNlX3R5cGVcIjogXCJQT1JUQUxcIn0iLCJyZXF1ZXN0X3RpbWVzdGFtcCI6MTY3Nzg3NjM2NCwid2FsbGV0X2FkbWlucyI6WyJCR2VIZDlJNzd3bm95ZnozQ29EeC96NkFQWXFvRnIrTzIzdU4yekVZd0ZnTm5pUEV1N3FKK2dLR3c5azFycnduVWd5WU9RL3BacVFJeTkweGJvOFpObm89Il0sIndhbGxldF9hZG1pbnNfcXVvcnVtX3RocmVzaG9sZCI6MSwid2FsbGV0X3BvbGljeSI6Ilt7XCJpZFwiOlwiNjRlMmZlODctYTMwNS00ZmUyLTkyMmUtOGY5NmRkNWNmOWE1XCIsXCJ3YWxsZXRfaWRcIjpcIjRlYjk5ZjVmLWE4ZjktNDBmMi1hMThlLTcyNjZjZjI0YjE5NVwiLFwiYXBwcm92ZXJzXCI6W1wiQktYVElQVzdZNCtwd1ZtZ0ZEc3hXVVNHWktZWGhIWGFpcGpYM0V2N3MzOXAwSU9EWFlieHJ3M3ZmbFFyWlUrcWNDRE9KWjFKNVZha3RNQTVyOE03Wmc0PVwiXSxcImFjdGlvblwiOlwic2VuZF90b19hcHByb3ZlclwiLFwiY2hhaW5faWRcIjpudWxsLFwiY29uZGl0aW9uc1wiOltdLFwibmFtZVwiOlwiMDEwMTAxXCIsXCJuZXR3b3JrX25hbWVcIjpudWxsLFwidHlwZVwiOlwiZGFwcFwifV0ifQ=="}
    #             headers = {
    #                     "Content-Type": "application/json; charset=utf-8",
    #                     "Authorization": "Bearer " + ReadConfig.getBearToken()
    #                 }
    #             response = requests.post(url=baseUrl,json=inputData, headers=headers )
                
    #             responseJson = json.loads(response.text)
    #             print("AAAAABBBBB", response.text)


    # def test_QR_screenshot_page(self):
    #     self.driver.get("https://app.uniswap.org/#/swap")
    #     self.driver.find_element(By.XPATH, "//main[@id='swap-page']/div[3]/div[2]/button").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='wallet-connect']").click()
    #     time.sleep(1)
    #     outFileName= (r'../screenshots')
    #     self.driver.execute_script("document.body.style.zoom='200%'")
    #     b = RanDom.random_string_generator(5)
    #     self.driver.get_screenshot_as_file(outFileName+"/"+b+".png")
    #     a = {
    #             "namepicture": b,
    #             "url": "",
    #             "pic_id":"" 
    #         }
    #     ReadJsonScreenshot.writetoafile(a)

    # def test_QR_screenshot_upload(self):
    #     c =  '../screenshots/'+ ReadJsonScreenshot.geinputData()["namepicture"]+".png"
    #     files = {
    #             'file': open( c, 'rb'),
    #             'custom_id': (None, 'SampleMedia'+RanDom.random_string_generator(5)),
    #     }
    #     response = requests.post('https://api-cloud.browserstack.com/app-automate/upload-media', files=files, auth=('testsavvy_deyw9B', 'AWsf9sjzd5YFxTu1Pmwc'))
    #     print(response.text)
    #     responseJson = json.loads(response.text)
    #     a = {
    #             "namepicture": ReadJsonScreenshot.geinputData()["namepicture"]+".png",
    #             "url": responseJson["media_url"],
    #             "pic_id":responseJson["custom_id"]
    #         }
    #     ReadJsonScreenshot.writetoafile(a)