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

@pytest.fixture(autouse=True)
def prepare_data():
    print("\nprepare data for every test")


class TestMainPage1():

    def test_guest_should_see_login_link(self, driver):
        print("start test1")
        driver.get(link)
        driver.find_element_by_css_selector("#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, driver):
        print("start test2")
        driver.get(link)
        driver.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")

