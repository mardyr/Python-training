from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

links = driver.find_elements(By.TAG_NAME,"a")

print("Number of links",len(links))

for link in links:
    if link.text == "" : continue
    print(link.text)

# clicking on the link

driver.find_element(By.LINK_TEXT,"REGISTER").click()

# driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click() #partial linking text
