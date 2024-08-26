from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class tabledata:

    def __init__(self, driver):
        self.driver = driver

    def get_course_list(self):
        Courses = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "(//body/div[3]/div[1]/fieldset[1])//tr/td[2]"))
        )

        # Print the number of elements found
        print(f"Number of elements found: {len(Courses)}")
        Browser_list = []
        # Print the text of each element
        for course in Courses:
            Course_list = course.text
            Browser_list.append(Course_list)
            complete_course = Browser_list.copy()
            assert complete_course == Browser_list

    def showtextbox(self):
        return self.driver.find_element(By.ID, "show-textbox")

    def displayedtext(self):
        return self.driver.find_element(By.ID, "displayed-text")

    def Sum_prices(self):
        prices = self.driver.find_elements(By.XPATH, "(//body/div[3]/div[2]/fieldset[2]/div[1])//tr/td[4]")
        Sum = 0
        for price in prices:
            actual_price = int(price.text)
            Sum = Sum + actual_price
        expected_price = 296
        assert Sum == expected_price


