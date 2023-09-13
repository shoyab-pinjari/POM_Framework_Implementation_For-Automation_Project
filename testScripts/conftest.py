import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser=='firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif browser=='edge':
        driver = webdriver.Edge()
        driver.maximize_window()
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
    return driver


def pytest_addoption(parser): # This will get the value from CLI / Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########## To generate Pytest HTML Reports #############

# ### It is the hook for adding Environment info to HTML report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'I am Automation Technology Unicorn'

#
# ### It is hook for Delete/Modify environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('JAVA_HOME',None)
#     metadata.pop('Plugins', None)