import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def driver():
    print("\nstart browser")
    driver = webdriver.Chrome()
    yield driver
    print("\nclose browser")
    driver.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, driver):
        driver.get(link)
        driver.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, driver):
        driver.get(link)
        driver.find_element_by_css_selector(".basket-mini .btn-group > a")

