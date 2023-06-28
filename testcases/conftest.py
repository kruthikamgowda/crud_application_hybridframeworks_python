#generic
from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
       driver = webdriver.Chrome()
       print("launching chrome browser")
    elif browser=="firefox":
        driver=webdriver.Firefox()
        print("launching firefox browser")
    else:
        driver=webdriver.Ie()
        print("launching IE browser")

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########## pytest html report. ##########

def pytest_configure(config):
    config._metadata['Project Name'] = "crud_appliaction_hybridframeworks_pyhton"
    config._metadata['Module Name'] = 'Register page and Login Page'
    config._metadata['Tester'] = "kruthika "


# it is a hook for delete/modify environment info in to the html report.
# inorder to remove some non-essential(default) values generated automatically we will use pop to remove them.
@pytest.hookimpl(optionalhook=True)
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
