import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//loginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("***************** Test_002_DDT_Login *****************")
        self.logger.info("***************** Verifying Login DDT Test *****************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in excel:", self.rows)

        list_status = [] # Empty list variable

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            time.sleep(3)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***************** Passed *****************")
                    self.lp.clickLogout()
                    # list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***************** Failed *****************")
                    self.lp.clickLogout()
                    # list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("***************** Failed *****************")
                    # list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***************** Passed *****************")
                    # list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("***************** Login DDT test passed *****************")
            self.driver.quit()
            assert True
        else:
            self.logger.info("***************** Login DDT test failed *****************")
            self.driver.quit()
            assert False

        self.logger.info("***************** End of Login DDT Test *****************")
        self.logger.info("***************** Completed Test_002_DDT_Login *****************")