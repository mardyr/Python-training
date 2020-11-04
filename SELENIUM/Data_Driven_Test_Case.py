#Check correctness of login and password in travel website

import xlutils as util

from selenium import webdriver

driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

driver.maximize_window()


path = r"C:\Users\Majster\Desktop\IEPS\PYTHON\SELENIUM\test.xlsx"
sheetName = 'Arkusz1'

rows = util.getRowCount(path,sheetName)
columns = util. getColumnCount(path,sheetName)

for row in range(2,rows+1):

    login = util.readData(path,sheetName,row,1)
    password = util.readData(path,sheetName,row,2)

    driver.find_element_by_name("userName").send_keys(login)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("submit").click()

    if driver.current_url == r"http://demo.guru99.com/test/newtours/login_sucess.php":
        data = "test passed"
        util.writeData(path,sheetName,row,3,data)
    else :
        data = "test failed"
        util.writeData(path, sheetName, row, 3, data)

    driver.find_element_by_link_text("Home").click() # back to home page to check second scenario


driver.close()