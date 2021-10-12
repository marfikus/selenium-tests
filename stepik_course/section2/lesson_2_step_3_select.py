
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link_1 = "http://suninjuly.github.io/selects1.html"
link_2 = "http://suninjuly.github.io/selects2.html"

def calc_example(a, b):
    return str(int(a) + int(b))

try:
    driver = webdriver.Chrome()
    driver.get(link_2)

    a = driver.find_element_by_css_selector("span[id='num1']").text
    b = driver.find_element_by_css_selector("span[id='num2']").text
    x = calc_example(a, b)

    select = Select(driver.find_element_by_css_selector("select[id='dropdown']"))
    select.select_by_value(x)

    # time.sleep(3)

    submit_button = driver.find_element_by_css_selector("button[type='submit']")
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()
