from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.expedia.com/")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/ul/li[2]/a/span").click()

time.sleep(2)
# set departure place
firstwind = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[1]/button").send_keys("SSFO")
firstwindclick = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[2]/ul/li[1]/button/div/div[1]/span/strong").click()

time.sleep(2)
# set arrival place
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[1]/button").send_keys("NNYC")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]/ul/li[1]/button/div/div[1]/span/strong").click()

# set trip date
driver.find_element(By.ID,"d1-btn").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[3]/td[5]/button").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div[2]/button").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/div/div[2]/div/form/div[3]/div[2]/button").click()

wait = WebDriverWait(driver,10)

element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stops-0']")))

element.click()

time.sleep(3)


