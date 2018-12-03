from selenium import webdriver


browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
url = "https://www.dineoncampus.com/trinity/whats-on-the-menu"
browser.get(url) #navigate to the page
"""

username = browser.find_element_by_tag_name('strong') #username form field
print(username[1].text)
#password = browser.find_element_by_id("password_id") #password form field

"""
browser.get("https://www.dineoncampus.com/trinity/whats-on-the-menu") #navigate to page behind login
innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
print(innerHTML)

browser.close()
#"""
