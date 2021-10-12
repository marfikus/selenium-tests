
from selenium import webdriver
import time
import math

link_1 = "http://suninjuly.github.io/execute_script.html"

def calc_example(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link_1)

    x = driver.find_element_by_css_selector("span[id='input_value']").text
    answer_input = driver.find_element_by_css_selector("input[id='answer']")
    answer_input.send_keys(calc_example(x))

    submit_button = driver.find_element_by_css_selector("button[type='submit']")
    driver.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

    checkbox = driver.find_element_by_css_selector("input[id='robotCheckbox']")
    checkbox.click()

    radiobutton = driver.find_element_by_css_selector("input[id='robotsRule']")
    radiobutton.click()

    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()
