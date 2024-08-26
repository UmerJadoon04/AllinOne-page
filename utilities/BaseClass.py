import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Tests.conftest import setup


@pytest.mark.usefixtures('setup')
class BaseClass:
    driver = None

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s %(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def selectoption(self, value):
        dropdown = Select(self.driver.find_element(By.ID, "dropdown-class-example"))
        dropdown.select_by_value(value)





