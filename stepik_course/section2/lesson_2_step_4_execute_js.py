
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link_1 = "http://suninjuly.github.io/selects1.html"
link_2 = "http://suninjuly.github.io/selects2.html"

def calc_example(a, b):
    return str(int(a) + int(b))

try:
    driver = webdriver.Chrome()
    # driver.get(link_2)
    # driver.execute_script("alert('hello');")
    driver.execute_script(
        """
        document.title='scriptdfdf';
        alert('hello!');
        """
    )

finally:
    time.sleep(3)
    driver.quit()
