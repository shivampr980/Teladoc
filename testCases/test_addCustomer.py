import random
import string

import pytest
from selenium.webdriver.common.by import By

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()    # Logger

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*************** Test_003_AddCustomer ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Login Admin Page
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login successful ***************")

        # Admin Home Page
        self.logger.info("*************** Starting Add Customer Test ***************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddNew()

        # Add New Customer Page
        self.logger.info("*************** Providing Customer Info ***************")
        self.email = random_generator() + "@nopCommerce.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Eren")
        self.addcust.setLastName("Yeager")
        self.addcust.setDob("10/10/1999")
        self.addcust.setCompanyName("AOT Company")
        self.addcust.setAdminComment("This is for testing purposes...")
        self.addcust.clickOnSave()
        self.logger.info("*************** Saving Customer Info ***************")
        self.logger.info("*************** Add Customer validation started ***************")

        # Validate success message
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*************** Add Customer Test Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")    # Screenshot
            self.logger.info("*************** Add Customer Test Failed ***************")
            assert True == False

        self.driver.quit()
        self.logger.info("*************** Ending Test_003_AddCustomer Test  ***************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))