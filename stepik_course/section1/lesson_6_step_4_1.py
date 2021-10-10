
from selenium import webdriver
import time

link = "https://www.degreesymbol.net"
link_text = "Degree Symbol in Math"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    link2 = driver.find_element_by_link_text(link_text)
    # link2 = driver.find_element_by_partial_link_text("Math")
    # print(link2.get_attribute("href"))
    link2.click()

finally:
    time.sleep(2)
    driver.quit()
