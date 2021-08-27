from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://login.live.com/login.srf')
usuario = driver.find_element_by_name('loginfmt')
usuario.send_keys('carlos-javier.rodriguez@outlook.com')
usuario.send_keys(Keys.ENTER)
time.sleep(3)

clave = driver.find_element_by_name('passwd')
clave.send_keys('asdfgh12')
clave.send_keys(Keys.ENTER)