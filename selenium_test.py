import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(os.environ['PYTHONPATH'] + '/venv/bin/chromedriver')
driver.get("https://www.google.com/")

search = driver.find_element_by_name("q")
search.clear()
search.send_keys("news", Keys.ENTER)
#driver.implicitly_wait(10)

desc = driver.find_elements_by_css_selector("html body div.srg div.g .rc > .s > div > span.st")
link_title = driver.find_elements_by_css_selector("html body div.srg div.g .rc > .r h3")
url = driver.find_elements_by_css_selector("html body div.srg div.g .rc > .r > a:not(.fl)")

for i in range(len(link_title)):
    print("Title: {} \nDescription: {} \nLink: {}".format(link_title[i].text, desc[i].text, url[i].get_attribute("href")))
    print('-------------------------')