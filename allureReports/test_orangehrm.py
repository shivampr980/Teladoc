import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.severity(allure.severity_level.NORMAL)
class TestHRM:
    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status = self.driver.find_element(By.XPATH, "//div[@id='divLogo']/img").is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listEmployees(self):
        pytest.skip('Skipping test')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        actTitle = self.driver.title
        if actTitle == "OrangeHRM123":
            self.driver.quit()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen", attachment_type=AttachmentType.PNG)
            self.driver.quit()
            assert False