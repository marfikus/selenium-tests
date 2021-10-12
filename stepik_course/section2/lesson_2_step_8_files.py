
from selenium import webdriver
import time
import math
import os

link_1 = "http://suninjuly.github.io/file_input.html"

data = {
    "first_name": "Nick",
    "last_name": "Dandy",
    "email": "nick.d@mail.com"
}

file_name = "test_file.txt"
current_dir_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir_path, file_name)
# print(file_path)

with open(file_path, "w") as f:
    f.write("dfsdfsfsdfsf")

try:
    driver = webdriver.Chrome()
    driver.get(link_1)

    first_name_input = driver.find_element_by_css_selector("input[name='firstname']")
    first_name_input.send_keys(data["first_name"])

    last_name_input = driver.find_element_by_css_selector("input[name='lastname']")
    last_name_input.send_keys(data["last_name"])

    email_input = driver.find_element_by_css_selector("input[name='email']")
    email_input.send_keys(data["email"])

    file_input = driver.find_element_by_css_selector("input[type='file']")
    file_input.send_keys(file_path)

    submit_button = driver.find_element_by_css_selector("button[type='submit']")
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()
