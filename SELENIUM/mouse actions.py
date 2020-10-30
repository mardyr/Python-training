from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
# DOUBLE CLICK

driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")
#
# driver.get("https://testautomationpractice.blogspot.com/")
#
# driver.maximize_window()
#
# element = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/button")
#
# actions = ActionChains(driver)
#
# actions.double_click(element).perform()
#
# time.sleep(5)
# driver.quit()
#
# time.sleep(10)

# RIGHT CLICK

# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
#
# button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
#
# action = ActionChains(driver)
#
# action.context_click(button).perform()



# DRAG & DROP

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

source = driver.find_element(By.ID,"box6")
target = driver.find_element(By.ID, "box106")

actions = ActionChains(driver)

actions.drag_and_drop(source,target).perform()