from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_atras_adelante(self):
        driver = self.driver
        driver.get('https://www.google.com')
        time.sleep(3)
        driver.execute_script('window.open('');')
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get('http://stackoverflow.com')
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)


    def tearDown(self):
        self.driver.close()

    
if __name__ == '__main__':
    unittest.main()