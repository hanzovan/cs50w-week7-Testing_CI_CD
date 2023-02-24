import os
import pathlib
import unittest
import time

from selenium import webdriver


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


driver = webdriver.Safari()


class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("count.html"))
        self.assertEqual(driver.title, "count")

    def test_increase(self):
        driver.get(file_uri("count.html"))
        increase = driver.find_element("id", "increase")
        increase.click()

        self.assertEqual(driver.find_element('tag name', 'h1').text, '1')

    def test_decrease(self):
        """ Check if decrease button work as expected """
        driver.get(file_uri('count.html'))
        decrease = driver.find_element('id', 'decrease')
        decrease.click()
        self.assertEqual(driver.find_element('tag name', 'h1').text, '-1')

    def test_multiple_increase(self):
        """ Check if click increase 3 times will turn h1 into 3 or not"""
        driver.get(file_uri('count.html'))
        increase = driver.find_element('id', 'increase')
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element('tag name', 'h1').text, '3')


if __name__=='__main__':
    unittest.main()