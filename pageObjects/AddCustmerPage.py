import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
    #Add customer page
    link_Customer_menu_xpath = "//nav[@class='mt-2']/ul/li[4]"
    link_Customers_menitem_xpath = "//nav[@class='mt-2']/ul/li[4]/ul/li//p[contains(.,'Customers')]"#"//span[@class='menu-item-title'][contains(text(),'Customers')]"
    button_AddNew_xpath = "//a[@class='btn btn-primary' and @href='/Admin/Customer/Create']"#"//a[@class='btn bg-blue']"

    textbox_Email_xpath = "//input[@id='Email']"
    textbox_Password_xpath = "//input[@id='Password']"
    textbox_FirstName_xpath = "//input[@id='FirstName']"
    textbox_LastName_xpath = "//input[@id='LastName']"
    radiobtn_MaleGender_id = "Gender-Male"
    radiobtn_FemaleGender_id = "Gender-Female"
    textbox_dob_xpath = "//input[@id='DateOfBirth']"
    textbox_CompanyName_xpath = "//input[@id='Company']"
    textbox_customerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    listitem_Administrators_xpath = "//li[contains(text(),'Administrators')]"
    listitem_Registered_xpath = "//li[contains(text(),'Registered')]"
    listitem_Guests_xpath = "//li[contains(text(),'Guests')]"
    listitem_Vendors_xpath = "//li[contains(text(),'Vendors')]"
    drp_mgrOfVendor_xpath = "//*[@id='VendorId']"
    textbox_AdminComment_xpath = "//textarea[@id='AdminComment']"
    button_Save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.link_Customer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.link_Customers_menitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.button_AddNew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.textbox_Email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_Password_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.textbox_customerRoles_xpath).click()
        time.sleep(3)
        if role =='Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.listitem_Registered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH,self.listitem_Administrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered (or) Guest, only one, this combination together not allowed
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH,self.listitem_Guests_xpath)
        elif role=='Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.listitem_Registered_xpath)
        elif role=='Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.listitem_Vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH,self.listitem_Guests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("argument[0].click();",self.listitem)

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.drp_mgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID,self.radiobtn_MaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element(By.ID,self.radiobtn_FemaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.radiobtn_MaleGender_id).click()

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.textbox_FirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.textbox_LastName_xpath).send_keys(lname)

    def setDob(self,dob):
        self.driver.find_element(By.XPATH,self.textbox_dob_xpath).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element(By.XPATH,self.textbox_CompanyName_xpath).send_keys(comname)

    def setAdminComment(self,comment):
        self.driver.find_element(By.XPATH,self.textbox_AdminComment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.button_Save_xpath).click()