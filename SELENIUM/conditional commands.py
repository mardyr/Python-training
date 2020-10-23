from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")

driver.get('https://www.nocowanie.pl/logowanie/')


log = driver.find_element_by_name("login")

print(log.is_displayed())

print(log.is_enabled())

password = driver.find_element_by_name("password")

print(password.is_displayed())
print(password.is_enabled())

log.send_keys("Marcin");
password.send_keys("Marcin");

driver.find_element_by_name("password").click()