
from selenium import webdriver
import time

link_1 = "https://SunInJuly.github.io/execute_script.html"

try:
    driver = webdriver.Chrome()
    driver.get(link_1)

    button = driver.find_element_by_tag_name("button")
    # driver.execute_script("window.scrollBy(0, 100);")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)

    button.click()

finally:
    time.sleep(3)
    driver.quit()
