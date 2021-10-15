
from selenium import webdriver
import time
import math

link_1 = "http://suninjuly.github.io/wait1.html"

try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) # ожидание при поиске элементов 
    driver.get(link_1)

    verify_button = driver.find_element_by_id("verify")
    verify_button.click()

    message = driver.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    time.sleep(5)
    driver.quit()
