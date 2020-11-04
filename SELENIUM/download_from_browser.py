from selenium import webdriver
from selenium.webdriver.common.by import By

#firefox preferences
fp = webdriver.FirefoxProfile()

fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", r"C:\Users\Majster\Desktop\IEPS\PYTHON")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)



driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe",
                           firefox_profile=fp)

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

#Generate text file

driver.find_element(By.ID, "textbox").send_keys("Testing download text file")
driver.find_element(By.ID, "createTxt").click()
driver.find_element(By.ID, "link-to-download").click()

#Generate pdf file

driver.find_element(By.ID,"pdfbox").send_keys("Testing pdf file")
driver.find_element(By.ID,"createPdf").click()
driver.find_element(By.ID,"pdf-link-to-download").click()