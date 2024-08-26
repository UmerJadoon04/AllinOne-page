from selenium.webdriver.common.by import By


class windowsoption():

    def __init__(self, driver):
        self.driver = driver

    def childwindow(self):
        current_window = self.driver.current_window_handle
        self.driver.find_element(By.ID, "openwindow").click()
        new_window = [window for window in self.driver.window_handles if window != current_window][0]
        self.driver.switch_to.window(new_window)
        self.driver.find_element(By.LINK_TEXT, "Courses").click()
        self.driver.close()
        self.driver.switch_to.window(current_window)

    def childtab(self):
        current_tab = self.driver.current_window_handle
        self.driver.find_element(By.ID, "opentab").click()
        new_tab = [tab for tab in self.driver.window_handles if tab != current_tab][0]
        self.driver.switch_to.window(new_tab)
        self.driver.find_element(By.LINK_TEXT, "Courses")
        self.driver.close()
        self.driver.switch_to.window(current_tab)

    def alert(self):
        Name = "Umer Jadoon"
        self.driver.find_element(By.ID, "name").send_keys("Umer Jadoon")
        self.driver.find_element(By.ID, "alertbtn").click()
        alert = self.driver.switch_to.alert
        Alert = alert.text
        assert Name in Alert
        alert.accept()
