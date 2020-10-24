from selenium import  webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

#waait
driver.implicitly_wait(5) # wait for 5 sec

assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("submit").click()
