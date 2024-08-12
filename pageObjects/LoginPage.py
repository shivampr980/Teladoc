import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class LoginPage:
    textbox_username= "(//input[@placeholder='User name or email *'])[1]"
    click_next="//span[contains(@class,'input-group-text custom-input-group-btn ng-tns')]"
    textbox_password_id = "(//input[@type='password'])[1]"
    button_login_xpath = "(//button[@type='submit'])[1]"
    link_logout_linktext = "Logout"
    logout_Display ="//a[normalize-space()='One Login']"

    def __init__(self, driver):
        self.driver = driver

    def _wait_for_is_displayed(self, by, value, timeout):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(expected_conditions.visibility_of_element_located((by, value)))
        except TimeoutException:
            return False
        return True

    def setUserName(self, username):
        self._wait_for_is_displayed(By.XPATH, self.logout_Display, 20)
        self.driver.find_element(By.XPATH, self.textbox_username).send_keys(username)
        self.driver.find_element(By.XPATH, self.click_next).click()

    def setPassword(self, password):
        self._wait_for_is_displayed(By.XPATH, self.textbox_password_id, 10)
        self.driver.find_element(By.XPATH, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

    def Login_Page(self):
        self.setUserName()
        self.setUserName()
        self.clickLogin()
