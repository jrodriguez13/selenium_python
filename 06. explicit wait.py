from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_explicit_wait(self):
        driver = self.driver
        driver.get('https://www.google.com')
        try:
            elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'q'))
            )
        finally:
            driver.quit()

    def tearDown(self):
        self.driver.close()

    
if __name__ == '__main__':
    unittest.main()