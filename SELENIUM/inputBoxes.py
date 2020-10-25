from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")



# Find how many inputboxes present in web page
inputboxes = driver.find_elements(By.CLASS_NAME,"text_field")

print(len(inputboxes))

# Provide value to text box

if driver.find_element(By.ID,'RESULT_TextField-1').is_displayed():
    driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("Marcin ")  # Provide First Name

driver.find_element(By.ID,'RESULT_TextField-2').send_keys("DyrdóŁ".capitalize())
driver.find_element_by_id('RESULT_TextField-3').send_keys("000000000")

## RADIO BUTTONS AND CHECK BOXES

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)


femaleButton = driver.find_element(By.ID,"RESULT_RadioButton-7_1").is_selected()
if femaleButton is True:
    print("Kobieta")

# check boxes
wait = WebDriverWait(driver,10)

elem =wait.until(expected_conditions.element_to_be_clickable((By.ID,"RESULT_CheckBox-8_0"))) # Sunday clicked
elem.click()

driver.find_element_by_id("RESULT_CheckBox-8_5").click() # Friday clicked