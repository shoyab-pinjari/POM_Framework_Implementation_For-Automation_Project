from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_HomePageTitle(self,setup):

        self.logger.info("****** Test_001_Login ******")
        self.logger.info("****** Verifying Home Page Title ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title =='Your store. Login':
            assert True
            self.driver.close()
            self.logger.info("****** Home Page Title Test is Passed ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("****** Home Page Title Test is Failed ******")
            assert False

    def test_login(self,setup):
        self.logger.info("****** Verifying Login test ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # Dashboard / nopCommerce administration
        act_title = self.driver.title

        if act_title=='Dashboard / nopCommerce administration':
            assert True
            self.logger.info("****** Login test is Passed ******")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("****** Login test is Failed ******")
            assert False