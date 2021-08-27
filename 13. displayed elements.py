from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.google.com")
time.sleep(3)
displayelement = driver.find_element_by_name("btnI")
print(displayelement.is_displayed())# regresa true o false si ya cargo el elemento
print(displayelement.is_enabled())# regresa un true o false si el elemento esta disponible