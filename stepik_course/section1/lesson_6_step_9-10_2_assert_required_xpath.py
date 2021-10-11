
from selenium import webdriver
import time

link_1 = "http://suninjuly.github.io/registration1.html"
link_2 = "http://suninjuly.github.io/registration2.html"

data = {
    "first_name": "Nick",
    "last_name": "Dandy",
    "email": "nick.dandy@mail.com"
}

expected_message = "Congratulations! You have successfully registered!"

try:
    driver = webdriver.Chrome()
    driver.get(link_1)

    first_input = driver.find_element_by_xpath("//input[@required and contains(@class, 'first')]")
    first_input.send_keys(data["first_name"])

    second_input = driver.find_element_by_xpath("//input[@required and contains(@class, 'second')]")
    second_input.send_keys(data["last_name"])

    third_input = driver.find_element_by_xpath("//input[@required and contains(@class, 'third')]")
    third_input.send_keys(data["email"])

    # time.sleep(3)

    submit_button = driver.find_element_by_css_selector("button[type='submit']")
    submit_button.click()

    time.sleep(2)

    actual_message = driver.find_element_by_tag_name("h1").text
    assert actual_message == expected_message, "The expected and actual result do not match!"

finally:
    time.sleep(3)
    driver.quit()
