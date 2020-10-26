from selenium import webdriver


driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

# scroll down page by pixel
#driver.execute_script("window.scrollBy(0,1000)","")

# scroll down to element
#flag = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();", flag)


# scroll down till end of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

