from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Firefox

driver = webdriver.Firefox(executable_path= r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)

# driver.close() # zamyka obecne okna

driver.quit() # zamyka wszystkie okna