import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(os.environ['PYTHONPATH'] + '/venv/bin/chromedriver')
driver.get("https://www.google.com/")

search = driver.find_element_by_name("q")
search.clear()
search.send_keys("news", Keys.ENTER)
driver.implicitly_wait(10)


link_text = driver.find_elements_by_css_selector("html body div.srg div.g .rc > .r h3")
for i in link_text:
    print(i.text)
    print('-------------------------')

