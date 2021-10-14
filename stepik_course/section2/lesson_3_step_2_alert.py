
from selenium import webdriver
import time

link_1 = "http://suninjuly.github.io/execute_script.html"

try:
    driver = webdriver.Chrome()
    # driver.get(link_1)

    driver.execute_script("alert('dfdfd')")
    # driver.execute_script("confirm('dfdfd')")
    alert = driver.switch_to.alert
    # confirm = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print(alert_text)

finally:
    time.sleep(3)
    driver.quit()
