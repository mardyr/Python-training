from selenium import webdriver

import time
driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")
while True:

    driver.get("https://www.google.com/")
    driver.implicitly_wait(5)
    time.sleep(3)

    driver.find_element_by_xpath("//*[@id=\"tsf\"]/div[2]/div[1]/div[1]/div/div[2]/input").send_keys("noclegi solec zdrój")

    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]").click()

    time.sleep(4)

    driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[5]/div[2]/span[1]/div/table/tbody/tr/td[3]/a").click()

    time.sleep(3)

    driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[5]/div/div[1]/a/h3/span").click()

    time.sleep(3)

    driver.get("https://www.google.com/")

    time.sleep(3)

    driver.find_element_by_xpath("//*[@id=\"tsf\"]/div[2]/div[1]/div[1]/div/div[2]/input").send_keys("u krzyśka solec zdrój")

    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]").click()

    time.sleep(2)

    driver.find_element_by_xpath("//*[@id=\"rso\"]/div[1]/div/div[1]/a/h3").click()

    time.sleep(4)

    driver.get("https://www.google.com/")

    time.sleep(3)

    driver.find_element_by_xpath("//*[@id=\"tsf\"]/div[2]/div[1]/div[1]/div/div[2]/input").send_keys("solec zdrój")

    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]").click()

    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[5]/div[2]/span[1]/div/table/tbody/tr/td[6]/a").click()

    time.sleep(4)

    driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[6]/div/div[1]/a/h3/span").click()

    time.sleep(4)

driver.quit()