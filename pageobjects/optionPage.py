from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OptionPage:
    def __init__(self, driver):
        self.driver = driver

    def radiobutton(self):
       return self.driver.find_element(By.XPATH, "//input[@value='radio3']")

    def staticdropdown(self):
        dropdown_element =self.driver.find_element(By.ID, "autocomplete")
        dropdown_element.send_keys("pa")

        countries = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "ui-menu-item"))
        )
        for country in countries:
            if country.text == "Pakistan":
                country.click()
                break

    def selectoption(self, value):
        dropdown = Select(self.driver.find_element(By.ID, "dropdown-class-example"))
        dropdown.select_by_value(value)

    def checkbox(self):
        return self.driver.find_element(By.ID, "checkBoxOption1")

