
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

link_1 = "http://suninjuly.github.io/wait2.html"

try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) # ожидание при поиске элементов 
    driver.get(link_1)

    # ожидание кликабельности кнопки
    verify_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "verify"))
        )
    verify_button.click()

    message = driver.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    time.sleep(5)
    driver.quit()
