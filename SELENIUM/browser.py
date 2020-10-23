from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path = r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")

driver.get("https://www.wp.pl/")  #open browser

print(driver.title)  # print title
print(driver.current_url)

driver.close() # close the browser

