
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import re

link_1 = "http://suninjuly.github.io/explicit_wait2.html"

def calc_example(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) # ожидание при поиске элементов 
    driver.get(link_1)

    button = driver.find_element_by_id("book")

    # ожидание определённого текста в элементе
    price = WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button.click()

    x = driver.find_element_by_css_selector("span[id='input_value']").text
    answer_input = driver.find_element_by_css_selector("input[id='answer']")
    answer_input.send_keys(calc_example(x))

    submit_button = driver.find_element_by_id("solve")
    submit_button.click()

    alert = driver.switch_to.alert
    result = re.findall(r"\w+:\s+(\d+\.\d+)", alert.text)
    print("code:", result[0])

finally:
    time.sleep(2)
    driver.quit()
