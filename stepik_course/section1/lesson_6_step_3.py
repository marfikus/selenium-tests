
from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"
data = {
    "first_name": "Nick",
    "last_name": "Dandy",
    "city": "Los Angeles",
    "country": "USA"
}

try:
    driver = webdriver.Chrome()
    driver.get(link)

    first_name_input = driver.find_element_by_name("first_name")
    first_name_input.send_keys(data["first_name"])

    last_name_input = driver.find_element_by_name("last_name")
    last_name_input.send_keys(data["last_name"])

    city_input = driver.find_element_by_css_selector(".city")
    city_input.send_keys(data["city"])

    country_input = driver.find_element_by_id("country")
    country_input.send_keys(data["country"])

    submit_button = driver.find_element_by_id("submit_button")
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()
