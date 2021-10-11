
from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

data = {
    "first_name": "Nick",
    "last_name": "Dandy",
    "city": "Los Angeles",
    "country": "USA"
}

try:
    driver = webdriver.Chrome()
    driver.get(link)

    first_name_input = driver.find_element_by_xpath("//input[@name='first_name']")
    first_name_input.send_keys(data["first_name"])

    last_name_input = driver.find_element_by_xpath("//input[@name='last_name']")
    last_name_input.send_keys(data["last_name"])

    city_input = driver.find_element_by_xpath("//input[contains(@class, 'city')]")
    city_input.send_keys(data["city"])

    country_input = driver.find_element_by_xpath("//input[@id='country']")
    country_input.send_keys(data["country"])

    submit_button = driver.find_element_by_xpath("//button[text()='Submit']")
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()
