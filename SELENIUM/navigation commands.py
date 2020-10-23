from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox(executable_path= r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")

driver.get("https://www.flashscore.pl/") # forward applications

print(driver.title)

driver.get("https://www.wp.pl/") # TT(testing tool appi)

time.sleep(3)
print(driver.title) #Testing tools

driver.back() # back to first window
time.sleep(3)
print(driver.title)

driver.forward() # go to testing tools window
time.sleep(3)
print(driver.title)
