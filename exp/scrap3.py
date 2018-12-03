from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
titles_element = browser.find_elements_by_tag_name("strong")
#titles_element = browser.find_elements_by_id("__BVID__192")
#print(len(titles_element))
#print(titles_element[0].text)
for menu in titles_element:
    if menu.text != "":
        print(menu.text)
#for menu in titles_element:
#    print(menu.text, '\n')

#titles = [x.text for x in titles_element]
#print(len(titles))
