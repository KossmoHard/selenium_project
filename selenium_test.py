from selenium import webdriver
from selenium.webdriver.common.keys import Keys


search_text = str(input("Enter values ​​to search:"))
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get("https://www.google.com/")
search = driver.find_element_by_name("q")
search.clear()
search.send_keys(search_text, Keys.ENTER)

title = driver.find_elements_by_css_selector("html body div.srg div.g .rc > .r h3")
desc = driver.find_elements_by_css_selector("html body div.srg div.g .rc > .s > div > span.st")
url = driver.find_elements_by_css_selector("html body div.srg div.g .rc > .r > a:not(.fl)")

for i in range(len(title)):
    print("Title: {} \nDescription: {} \nLink: {}".format(title[i].text, desc[i].text, url[i].get_attribute("href")))
    print('-------------------------')
