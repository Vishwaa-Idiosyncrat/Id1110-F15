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
