from bs4 import BeautifulSoup
import requests

import requests

page = requests.get("https://www.dineoncampus.com/trinity/whats-on-the-menu")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
