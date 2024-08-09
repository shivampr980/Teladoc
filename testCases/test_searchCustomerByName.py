import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()    # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("*************** Test_005_SearchCustomerByName ***************")
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
        self.logger.info("*************** Starting Search Customer By Name ***************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("*************** Searching Customer by Name ***************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(3)
        status = searchcust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("*************** Test_005_SearchCustomerByName Finished ***************")
        self.driver.quit()