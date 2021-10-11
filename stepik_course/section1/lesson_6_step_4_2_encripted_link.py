
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"
text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
print(text)

data = {
    "first_name": "Nick",
    "last_name": "Dandy",
    "city": "Los Angeles",
    "country": "USA"
}

try:
    driver = webdriver.Chrome()
    driver.get(link)

    link2 = driver.find_element_by_link_text(text)
    # print(link2.get_attribute("href"))
    link2.click()

    first_name_input = driver.find_element_by_name("first_name")
    first_name_input.send_keys(data["first_name"])

    last_name_input = driver.find_element_by_name("last_name")
    last_name_input.send_keys(data["last_name"])

    city_input = driver.find_element_by_css_selector(".city")
    city_input.send_keys(data["city"])

    country_input = driver.find_element_by_id("country")
    country_input.send_keys(data["country"])

    submit_button = driver.find_element_by_tag_name("button")
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()
