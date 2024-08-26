from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class mouse_hover:
    def __init__(self, driver):
        self.driver = driver

    def mouse_hover(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.ID, "mousehover")).perform()
        action.move_to_element(self.driver.find_element(By.LINK_TEXT, "Top")).perform()