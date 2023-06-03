import urllib.request
from bs4 import BeautifulSoup

get_link = urllib.request.urlopen("https://en.wikipedia.org/wiki/Special:Random")
get_link = get_link.read()
soup = BeautifulSoup(get_link, "html.parser")
title = soup.find(class_="firstHeading").text
print(title)
