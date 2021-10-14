
from selenium import webdriver
import time
import math

link_1 = "http://suninjuly.github.io/redirect_accept.html"

def calc_example(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link_1)

    submit_button = driver.find_element_by_css_selector("button[type='submit']")
    submit_button.click()

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    x = driver.find_element_by_css_selector("span[id='input_value']").text
    answer_input = driver.find_element_by_css_selector("input[id='answer']")
    answer_input.send_keys(calc_example(x))

    submit_button = driver.find_element_by_css_selector("button[type='submit']")
    submit_button.click()

    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    precode = "quiz: "
    code_pos = alert_text.index(precode) + len(precode)
    code = alert_text[code_pos:]
    print(code)

finally:
    time.sleep(5)
    driver.quit()
