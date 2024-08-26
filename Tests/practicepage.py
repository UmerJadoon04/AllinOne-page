from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")
driver.find_element(By.XPATH, "//input[@value='radio2']").click()
driver.find_element(By.ID, "autocomplete").send_keys("Pa")
elements = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CLASS_NAME, "ui-menu-item"))
)
for course in elements:
    if course.text == "Pakistan":
        course.click()
        break
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdown.select_by_value("option3")
driver.find_element(By.ID, "checkBoxOption1").click()
current_window = driver.current_window_handle
driver.find_element(By.ID, "openwindow").click()
new_window = [window for window in driver.window_handles if window != current_window][0]
driver.switch_to.window(new_window)
driver.find_element(By.LINK_TEXT, "Courses").click()
driver.close()
driver.switch_to.window(current_window)
current_tab = driver.current_window_handle
driver.find_element(By.ID, "opentab").click()
new_tab = [tab for tab in driver.window_handles if tab != current_tab][0]
driver.switch_to.window(new_tab)
driver.find_element(By.LINK_TEXT, "Courses").click()
driver.close()
driver.switch_to.window(current_tab)
Name = "Umer Jadoon"
driver.find_element(By.ID, "name").send_keys("Umer Jadoon")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
Alert = alert.text
assert Name in Alert
alert.accept()
Browser_list = []
Courses = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, "(//body/div[3]/div[1]/fieldset[1]/table[1])//tr/td[2]"))
)
for course in Courses:
    course_list = Browser_list.append(course.text)
    new_course_list = Browser_list.copy()
    assert new_course_list == Browser_list
driver.find_element(By.ID, "show-textbox").click()
driver.find_element(By.ID, "displayed-text").send_keys("Show text")
Sum = 0
prices = driver.find_elements(By.XPATH, "(//body/div[3]/div[2]/fieldset[2]/div[1])//tr/td[4]")
for price in prices:
    actual_price = int(price.text)
    Sum = Sum + actual_price
expected_price = 296
assert Sum == expected_price
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Top")).perform()


