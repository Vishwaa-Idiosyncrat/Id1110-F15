import nltk
import numpy as np
import random
import string
import bs4 as bs
import urllib.request
import re
link = urllib.request.urlopen('https://en.wikipedia.org/wiki/Data_science')
link = link.read()
data = bs.BeautifulSoup(link,'lxml')
print(data)
data_paragraphs = data.find_all('p')
data_text = ''
for para in data_paragraphs:
    data_text += para.text
print(data_text)
data_text = data_text.lower()
data_text = re.sub(r'\[[0-9]*\]',' ',data_text)
data_text = re.sub(r'\s+',' ',data_text)
print(data_text)

