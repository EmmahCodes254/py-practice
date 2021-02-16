import requests
from bs4 import BeautifulSoup


url = "https://www.linkedin.com/jobs/"

scrap = requests.get(url)

content = BeautifulSoup(scrap.text, "html.parser")

"""print(content.prettify())"""

text = content.find_all("section", class_ = "section section--full")

print(text)
