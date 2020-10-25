from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame") # 1st frame

driver.find_element_by_link_text("org.openqa.selenium").click()

driver.switch_to.default_content() # have to back to default frame

time.sleep(5)

driver.switch_to.frame("packageFrame") # 2nd frame
driver.find_element_by_link_text("WebDriver").click()

time.sleep(5)

driver.switch_to.default_content()

time.sleep(5)

driver.switch_to.frame("classFrame") #third frame

driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click() #click in deprecated sections






