import nltk
nltk.download('punkt')
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

data_text = re.sub(r'\[[0-9]*\]', ' ',data_text)
data_text = re.sub(r'\s+',' ',data_text)
print(data_text)
sen = nltk.sent_tokenize(data_text)
words = nltk.word_tokenize(data_text)
print(sen)
