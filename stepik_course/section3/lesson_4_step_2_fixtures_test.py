
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser")
        self.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("\nclose browser")
        self.driver.quit()

    def test_guest_should_see_login_link(self):
        self.driver.get(link)
        self.driver.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.driver.get(link)
        self.driver.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("\nstart browser")
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        print("\nclose browser")
        self.driver.quit()

    def test_guest_should_see_login_link(self):
        self.driver.get(link)
        self.driver.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.driver.get(link)
        self.driver.find_element_by_css_selector(".basket-mini .btn-group > a")

