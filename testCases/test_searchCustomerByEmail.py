import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()    # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("*************** Test_004_SearchCustomerByEmail ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Login Admin Page
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login successful ***************")

        # Search Page
        self.logger.info("*************** Starting Search Customer By Email ***************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("*************** Searching Customer by emailID ***************")
        searchcust = SearchCustomer(self.driver)
        emailID = "victoria_victoria@nopCommerce.com"
        searchcust.setEmail(emailID)
        searchcust.clickSearch()
        time.sleep(3)
        status = searchcust.searchCustomerByEmail(emailID)
        assert True == status
        self.logger.info("*************** Test_004_SearchCustomerByEmail Finished ***************")
        self.driver.quit()