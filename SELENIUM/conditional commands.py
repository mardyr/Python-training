from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")

driver.get('http://demo.guru99.com/test/newtours/')


log = driver.find_element_by_name("userName")

print(log.is_displayed())

print(log.is_enabled())

password = driver.find_element_by_name("password")

print(password.is_displayed())
print(password.is_enabled())

log.send_keys("mercury");
password.send_keys("mercury");

driver.find_element_by_name("submit").click()

driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a").click()

roundTripButton = driver.find_element_by_css_selector("input[value=roundtrip]").is_selected()

if roundTripButton is True:
    print("To jest prawda")

radioButton = driver.find_element_by_css_selector("input[value=oneway]").is_selected()

if radioButton is True:
    print("Nie prawda")


    

