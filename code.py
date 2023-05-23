import nltk
import numpy as np
import random
import string
import bs4 as bs
import urllib.request
import re



get_link = urllib.request.urlopen('https://en.wikipedia.org/wiki/Data_science')
get_link = get_link.read()

data = bs.BeautifulSoup(get_link, 'lxml')
data_paragraphs = data.find_all('p')

data_text = ''
for para in data_paragraphs:
    data_text += para.text

data_text = data_text.lower()
print(data_text)