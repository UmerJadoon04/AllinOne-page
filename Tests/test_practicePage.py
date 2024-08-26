import pytest
from selenium import webdriver
from pageobjects.mousehover import mouse_hover
from pageobjects.optionPage import OptionPage
from pageobjects.tabledata import tabledata
from pageobjects.windowsoption import windowsoption
from testdata.practicepagedata import practicepagedata
from utilities.BaseClass import BaseClass


driver = webdriver.Chrome()


class TestPracticePage(BaseClass):

    def test_pageoptions(self, getdata, setup):
        driver = setup
        log = self.getlogger()
        optionpage = OptionPage(driver)
        optionpage.radiobutton().click()
        log.info("radio3 option is selected")
        optionpage.staticdropdown()
        log.info("Country Pakistan is selected")
        dropdown_value = getdata["dropdown"]
        optionpage.selectoption(dropdown_value)
        log.info("option3 is selected")
        optionpage.checkbox().click()
        log.info("checkbox1 is selected")
        windows_option = windowsoption(driver)
        windows_option.childwindow()
        log.info("successfully get control on child window")
        windows_option.childtab()
        log.info("successfully get control on child tab")
        windows_option.alert()
        log.info("successfully get Umer jadoon in alert")
        table_data = tabledata(driver)
        table_data.get_course_list()
        log.info("get course data from table and compares list successfully")
        table_data.showtextbox().click()
        table_data.displayedtext().send_keys("Show Text")
        log.info("get Show Text in displayed text")
        table_data.Sum_prices()
        log.info("get the sum of amount and compare with expected value ")
        mousehover = mouse_hover(driver)
        mousehover.mouse_hover()
        log.info("successfully click the Top option using mousehover")
        driver.quit()














