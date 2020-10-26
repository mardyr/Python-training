from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()

# JESLI CHCEMY USUNAC JEDNA KARTE Z WIELU, TO BIERZEMY HANDLER POBIERAMY GO I TOWRZY SIE LISTA HANDLEROW Z KARTY
handles = driver.window_handles # returns all the handle values of opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    time.sleep(10)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()




