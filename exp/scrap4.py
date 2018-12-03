from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support import Select
from selenium.common.exceptions import TimeoutException
import time

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# Create new Instance of Chrome in incognito mode
browser = webdriver.Chrome()

# Go to desired website
browser.get("https://www.dineoncampus.com/trinity/whats-on-the-menu")

# Get all of the titles for the pinned repositories
# We are not just getting pure titles but we are getting a selenium object
# with selenium elements of the titles.

# find_elements_by_xpath - Returns an array of selenium objects.
#titles_element = browser.find_elements_by_xpath("//table[@class='menu-items']")
time.sleep(5)

"""
titles_element = browser.find_elements_by_tag_name("strong")
for menu in titles_element:
    if menu.text != "":
        print(menu.text)

#a = browser.find_element_by_css_selector('button.clear')
#a = browser.find_element_by_xpath('//button[@type = "button"]/span')
a = browser.find_element_by_xpath('//input[@type = "search"]')
a.click()
time.sleep(5)
b = browser.find_elements_by_xpath('//ul[@class="dropdown-menu"]/li/a')
b[1].click()
time.sleep(10)
titles_element = browser.find_elements_by_tag_name("strong")
for menu in titles_element:
    if menu.text != "":
        print(menu.text)
"""

a = browser.find_element_by_xpath('//input[@type = "search"]')
a.click()
time.sleep(3)
b = browser.find_elements_by_xpath('//ul[@class="dropdown-menu"]/li/a')
b[2].click()
time.sleep(10)
a = browser.find_elements_by_xpath('//li[@role = "presentation"]/a')
a[1].click()
time.sleep(3)
titles_element = browser.find_elements_by_tag_name("strong")
for menu in titles_element:
    if menu.text != "":
        print(menu.text)

a[2].click()
time.sleep(3)
titles_element = browser.find_elements_by_tag_name("strong")
for menu in titles_element:
    if menu.text != "":
        print(menu.text)
