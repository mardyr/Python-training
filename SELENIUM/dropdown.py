from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element_by_id("RESULT_RadioButton-9")

dropdown = Select(element)

#select by visible text
dropdown.select_by_visible_text('Morning')

time.sleep(10)

# select by index
dropdown.select_by_index(2) # od zera typowo - Afternoon

time.sleep(10)

# select by value
dropdown.select_by_value("Radio-2") # Evening

# Count numner of options

print(len(dropdown.options)) # no tak , bo Empty, Morning , Afternoon i Evening

# Capture all options

ls = dropdown.options
for option in ls:
    print(option.text)