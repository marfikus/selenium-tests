
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

# driver = webdriver.Chrome()
with (webdriver.Chrome()) as driver:
    driver.get(link)

    # button = driver.find_element_by_id("submit_button")
    button = driver.find_element(By.ID, "submit_button")

# driver.quit()
