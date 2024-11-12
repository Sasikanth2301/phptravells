from email.policy import default

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib3 import request
from pytest_metadata.plugin import metadata_key


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",help="Specify the browser : chrome or firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("unsupported browser")

    return driver

###########  Pytest Html Reports ##########
# adding hooks for to show info in html report

def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'phptravels Demo'
    config.stash[metadata_key]['Test Module Name'] = 'Admin Login'
    config.stash[metadata_key]['Tester Name'] = 'vicky'

# hook for modify/delete  in report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    #metadata.pop('Java_Home',None)
    metadata.pop('Plugins', None)

