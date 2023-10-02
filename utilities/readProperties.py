import configparser
import os

config = configparser.RawConfigParser()
config.read('..\\configurations\\config.ini')
# config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('commonInfo', 'email')
        return username

    @staticmethod
    def getPassword():
        password=config.get('commonInfo', 'password')
        return password

    @staticmethod
    def getFromEmail():
        password=config.get('commonInfo', 'FROM_EMAIL')
        return password

    @staticmethod
    def getFromPwd():
        password=config.get('commonInfo', 'FROM_PWD')
        return password

    @staticmethod
    def getSmtpServer():
        password=config.get('commonInfo', 'SMTP_SERVER')
        return password
    
    @staticmethod
    def getBearToken():
        password=config.get('commonInfo', 'bearToken')
        return password

   

