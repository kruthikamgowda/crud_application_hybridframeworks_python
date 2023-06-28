from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
ele=driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']")
ele.click()
ele.send_keys("moblie")