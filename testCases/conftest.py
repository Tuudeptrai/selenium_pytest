import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
        print("Launching firefox browser.........")
    elif browser == 'bs':
        caps = {
            "os" : "Windows",
            "os_version" : "11",
            "browser" : "Chrome",
            "browser_version" : "latest-beta",
            "project" : "selenium demo",
            "build" : "jenkins ",
            "name" : "test jenkins browserstack",
            "browserstack.local" : "false",
            "browserstack.selenium_version" : "4.0.0",
            "resolution": "2560x1920"
        }
        print("Launching browserstack.........")
        driver = webdriver.Remote(
            command_executor='https://rainthe_0K23fG:MzukUonFP1FYpDqBq5Nz@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=caps)
    else:
        options = [
            "--headless",
            "--disable-gpu",
            "--window-size=1920,1200",
            "--ignore-certificate-errors",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-dev-shm-usage"
            ]   
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching chrome browser.........")
    
    yield driver
    driver.close()

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'
    config.option.htmlpath = "..\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
    @pytest.hookimpl(tryfirst=True)
    def pytest_configure(config):
        config.option.htmlpath = "..\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

