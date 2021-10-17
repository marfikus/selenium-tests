
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/"

# когда нужно проверить именно появление исключения при поиске элемента

def test_exception_1():
    try:
        driver = webdriver.Chrome()
        driver.get(link)
        with pytest.raises(NoSuchElementException):
            driver.find_element_by_css_selector("button.btn")
            pytest.fail("There should be no button!")
    finally:
        driver.quit()

def test_exception_2():
    try:
        driver = webdriver.Chrome()
        driver.get(link)
        with pytest.raises(NoSuchElementException):
            driver.find_element_by_css_selector("no_such_button.btn")
            pytest.fail("There should be no button!")
    finally:
        driver.quit()

