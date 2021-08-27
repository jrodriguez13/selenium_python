from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_buscar_x_path(self):
        driver = self.driver
        driver.get('https://www.google.com')
        time.sleep(3)
        buscar_por_xpath = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        time.sleep(3)
        buscar_por_xpath.send_keys('selenium', Keys.ARROW_DOWN)
        time.sleep(3)


    def tearDown(self):
        self.driver.close()

    
if __name__ == '__main__':
    unittest.main()