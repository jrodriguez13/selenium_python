import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome('chromedriver.exe')

	def test_usando_implicit_wait(self):
		driver = self.driver
		driver.implicitly_wait(5) # segundos
		driver.get("http://www.google.com")	
		myDynamicElement = driver.find_element_by_name("q")
	
	def tearDown(self):
		self.driver.close()
			
if __name__ == '__main__':
		unittest.main()	