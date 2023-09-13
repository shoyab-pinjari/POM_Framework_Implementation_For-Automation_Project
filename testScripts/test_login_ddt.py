import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils

class Test_003_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//testData/LoginTD.xlsx"
    logger=LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("****** Test_003_DDT_Login ******")
        self.logger.info("****** Verifying the login DDT test ******")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path, 'Sheet1')
        print("No.of rows in Excel: ",self.rows)

        list_status=[]  #Empty list variable
        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp =XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info(" ****** Passed ******")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info(" ****** Failed ******")
                    self.lp.clickLogout()
                    list_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp=='Pass':
                    self.logger.info(" ****** Failed ******")
                    list_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info(" ****** Passed ******")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("****** Login DDT test passed... ******")
            self.driver.close()
            assert True
        else:
            self.logger.info("****** Login DDT test failed... ******")

        self.logger.info("****** End of login DDT ******")
        self.logger.info("****** Completed TC_LoginDDT_002 ******")
