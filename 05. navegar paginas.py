from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_buscar(self):
        driver = self.driver
        driver.get('https://www.google.com')
        driver.get('http://www.gmail.com')
        driver.get('https://www.yahoo.com')
        driver.back()
        driver.back()
        driver.forward()
        driver.forward()

    def tearDown(self):
        self.driver.close()

    
if __name__ == '__main__':
    unittest.main()