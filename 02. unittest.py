from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_buscar_x_nombre(self):
        driver = self.driver
        driver.get('https://www.google.com')
        self.assertIn('Google', driver.title)
        elemento = driver.find_element_by_name('q')
        elemento.send_keys('selenium')
        elemento.send_keys(Keys.ENTER)
        time.sleep(5)
        assert 'No se encontró el elemento: ' not in driver.page_source

    def tearDown(self):
        self.driver.close()

    
if __name__ == '__main__':
    unittest.main()