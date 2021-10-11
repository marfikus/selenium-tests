
from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"
text = "my answer"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    inputs = driver.find_elements_by_css_selector("input[type='text']")
    # print("inputs:", len(inputs))
    for input in inputs:
        input.send_keys(text)

    submit_button = driver.find_element_by_css_selector("button[type='submit']")
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()
