import pytest
from selenium import webdriver

from testdata.practicepagedata import practicepagedata


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(params=practicepagedata.Test_practicepage_data)
def getdata(request):
    return request.param

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name").lower()

    if browser_name in ["chrome", "Google Chrome", "Chrome"]:
        driver = webdriver.Chrome()
    elif browser_name in ["Microsoft Edge", "edge", "Edge"]:
        driver = webdriver.Edge()
    else:
        print("f:browser not support '{browser_name}' default browser")
        driver = webdriver.Chrome()

    driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver

    driver.quit()







