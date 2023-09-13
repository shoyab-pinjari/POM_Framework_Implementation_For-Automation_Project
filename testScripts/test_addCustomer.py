import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustmerPage import AddCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen() # Logger

    def test_addCustomer(self,setup):
        self.logger.info("****** Test_004_AddCustomer ******")
        self.driver =setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login successful ******")
        self.logger.info("****** Startiing add customer test ******")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddNew()

        self.logger.info("****** Providing customer info ******")

        self.email = random_generator() + "@kpmg.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Aman")
        self.addcust.setLastName("Pinjari")
        self.addcust.setDob("25/10/2000") #DD-MM-YYYY
        self.addcust.setCompanyName("KPMG")
        self.addcust.setAdminComment("This is for testing...")
        self.addcust.clickOnSave()

        self.logger.info("****** Add customer validation started ******")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True==True
            self.logger.info("****** Add customer test passed ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png") #Screenshot
            self.logger.error("****** Add customer test failed ******")
            assert True==False

        self.driver.close()
        self.logger.info("****** Ending home page title test ******")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))