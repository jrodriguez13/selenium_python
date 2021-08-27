from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.w3schools.com/")
time.sleep(2)

encontrar_link = driver.find_element_by_link_text('Learn PHP')
encontrar_link.click()