import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    def test_search_in_google(self):
        driver = self.driver
        driver.get("https://www.google.com/")

        self.assertIn("Google", driver.title)

        search = driver.find_element_by_name("q")
        search.clear()
        search.send_keys("News", Keys.ENTER)

        assert "ничего не найдено" not in driver.page_source

        title = driver.find_elements_by_css_selector("html body div.srg div.g .rc > .r h3")
        desc = driver.find_elements_by_css_selector("html body div.srg div.g .rc > .s > div > span.st")
        url = driver.find_elements_by_css_selector("html body div.srg div.g .rc > .r > a:not(.fl)")

        self.assertIsNotNone(title)
        self.assertIsNotNone(desc)
        self.assertIsNotNone(url)
        self.assertEqual(len(title), len(desc))
        self.assertEqual(len(title), len(url))

        for i in range(len(title)):
            print("Title: {} \nDescription: {} \nLink: {}".format(title[i].text, desc[i].text,
                                                                  url[i].get_attribute("href")))
            print('-------------------------')

    def tearDown(self):
        self.driver.close()
