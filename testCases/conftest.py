import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser ..")
        driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching FireFox Browser ..")
        driver.maximize_window()
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
    return driver

def pytest_addoption(parser):   # This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# --------- PyTest HTML Report ---------------------------
# It is hook for adding environment info to HTML Report
#def pytest_configure(config):
   # config._metadata['Project Name'] = 'nop Commerce'
   # config._metadata['Module Name'] = 'Customers'
  #  config._metadata['Tester'] = 'Levi Ackerman'

# It is hook for delete/modify environment info to HTML Report
#@pytest.mark.optionalhook
#def pytest_metadata(metadata):
   # metadata.pop("JAVA_HOME", None)
   # metadata.pop("Plugins", None)