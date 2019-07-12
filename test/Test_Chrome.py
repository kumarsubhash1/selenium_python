from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r'/home/subhash/PycharmProjects/Selenium_python/test/chromedriver')
driver.maximize_window()
driver.get("https://www.facebook.com/")
Username = driver.find_element(By.ID, "email")
Username.send_keys("")
Password = driver.find_element(By.ID, 'pass')
Password.send_keys('')
time.sleep(5)
driver.close()