import os
import unittest
import pathlib
import time

from selenium import webdriver


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


driver = webdriver.Safari()


class WebpageTests(unittest.TestCase):

    def test_title(self):
        """ Check that the title is correct as 'Counter'"""
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, 'Counter')

    def test_increase(self):
        """ Check that clicking the + button will increase the counter value by 1"""
        driver.get(file_uri('counter.html'))
        increase = driver.find_element('id', 'increase')
        increase.click()
        self.assertEqual(driver.find_element('tag name', 'h2').text, '1')

    def test_decrease(self):
        """ Check that clicking the - btn will decrease the counter value by 1"""
        driver.get(file_uri('counter.html'))
        decrease = driver.find_element('id', 'decrease')
        decrease.click()
        self.assertEqual(driver.find_element('tag name', 'h2').text, '-1')

    def test_multiple_increase(self):
        """ Check that clicking the + btn multiple time will increase the value of counter by the times clicked """
        driver.get(file_uri('counter.html'))
        increase = driver.find_element('id', 'increase')
        for i in range(100):
            increase.click()        
        self.assertEqual(driver.find_element('tag name', 'h2').text, '100')

    
if __name__=='__main__':
    unittest.main()