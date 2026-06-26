from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/draggableLists.html")
element = driver.find_element(By.ID, "leftitem-1")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

source_element=driver.find_element(By.ID, "leftitem-2")
Target_element=driver.find_element(By.ID, "rightitem-3")
ActionChains(driver).drag_and_drop(source_element,Target_element).perform()
print("Success")

