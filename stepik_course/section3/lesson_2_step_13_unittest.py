import unittest
from selenium import webdriver
import time

link_1 = "http://suninjuly.github.io/registration1.html"
link_2 = "http://suninjuly.github.io/registration2.html"

data = {
    "first_name": "Nick",
    "last_name": "Dandy",
    "email": "nick.dandy@mail.com"
}

expected_message = "Congratulations! You have successfully registered!"

class TestRegistration(unittest.TestCase):
    def test_reg_1(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get(link_1)

        first_input = driver.find_element_by_xpath("//input[@required and contains(@class, 'first')]")
        first_input.send_keys(data["first_name"])

        second_input = driver.find_element_by_xpath("//input[@required and contains(@class, 'second')]")
        second_input.send_keys(data["last_name"])

        third_input = driver.find_element_by_xpath("//input[@required and contains(@class, 'third')]")
        third_input.send_keys(data["email"])

        submit_button = driver.find_element_by_css_selector("button[type='submit']")
        submit_button.click()

        # time.sleep(1)

        actual_message = driver.find_element_by_tag_name("h1").text
        self.assertEqual(actual_message, expected_message, "The expected and actual result do not match!")

    def test_reg_2(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get(link_2)

        first_input = driver.find_element_by_xpath("//input[@required and contains(@class, 'first')]")
        first_input.send_keys(data["first_name"])

        second_input = driver.find_element_by_xpath("//input[@required and contains(@class, 'second')]")
        second_input.send_keys(data["last_name"])

        third_input = driver.find_element_by_xpath("//input[@required and contains(@class, 'third')]")
        third_input.send_keys(data["email"])

        submit_button = driver.find_element_by_css_selector("button[type='submit']")
        submit_button.click()

        # time.sleep(1)

        actual_message = driver.find_element_by_tag_name("h1").text
        self.assertEqual(actual_message, expected_message, "The expected and actual result do not match!")


if __name__ == "__main__":
    unittest.main()
