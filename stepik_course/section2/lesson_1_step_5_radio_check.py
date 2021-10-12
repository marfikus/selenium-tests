
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

def calc_example(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)

    x = driver.find_element_by_css_selector("span[id='input_value']").text
    answer_input = driver.find_element_by_css_selector("input[id='answer']")
    answer_input.send_keys(calc_example(x))

    checkbox = driver.find_element_by_css_selector("input[id='robotCheckbox']")
    checkbox.click()

    radiobutton = driver.find_element_by_css_selector("input[id='robotsRule']")
    radiobutton.click()

    # time.sleep(3)

    submit_button = driver.find_element_by_css_selector("button[type='submit']")
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()
