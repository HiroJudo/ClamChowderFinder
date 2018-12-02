from selenium import webdriver

browser = webdriver.PhantomJS()

browser.get("https://www.dineoncampus.com/trinity/whats-on-the-menu")

innerHTML = browser.execute_script("return document.body.innerHTML")

#print(innerHTML)


print(browser.find_element_by_id("app").text)

browser.close()
