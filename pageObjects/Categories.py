
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Categories:
    # Categories page

    Categories = "//p[contains(.,'Categories')]"
    Catalog ="(//p[contains(.,'Catalog')])[1]"
    AddNew ="//a[normalize-space()='Add new']"
    Name ="//input[@id='Name']"
    Description ="//body[@data-id='Description']"
    save ="//button[@name='save']"
    DisplayOrder= "//input[@id='DisplayOrder']"
    back_to_category_list="//a[contains(.,'back to category list')"
    Save_and_Continue_Edit="(//button[normalize-space()='Save and Continue Edit'])[1]"
    Advance_btn ="//span[@class='onoffswitch-inner']"

    SearchCategoryName ="//input[@id='SearchCategoryName']"
    search_Btn ="//button[@id='search-categories']"
    importexcel="//button[@name='importexcel']"
    Export_dropdown ="//button[@class='btn btn-success dropdown-toggle']"
    Export_to_XML="//a[normalize-space()='Export to XML']"
    Export_to_Excel="//a[normalize-space()='Export to Excel']"
    delete_selected_btn="//button[@id='delete-selected']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCategoriesMenu(self):
        self.driver.find_element(By.XPATH, self.Categories).click()

    def clickOnCatalog(self):
        self.driver.find_element(By.XPATH, self.Catalog).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.AddNew).click()

    def clickOnsave(self):
        self.driver.find_element(By.XPATH, self.AddNew).click()
        
    def click_On_back_to_category_list(self):
        self.driver.find_element(By.XPATH, self.back_to_category_list).click()

    def click_On_back_to_category_list(self):
            self.driver.find_element(By.XPATH, self.back_to_category_list).click()