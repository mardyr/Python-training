import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):
    def test_Firefox(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title of the page is: "+ self.driver.title)
        self.driver.close()
    def test_Bing(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\Majster\Desktop\IEPS\Driver\geckodriver.exe")
        self.driver.get("https://bing.com")
        print("Title of the page is: "+ self.driver.title)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
