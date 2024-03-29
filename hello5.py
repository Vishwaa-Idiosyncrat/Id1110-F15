import nltk
import numpy as np
import random
import string
import bs4 as bs
import urllib.request
import re


inputs = ("hey","hello","good morning", "good afternoon","good evening","morning","evening","afternoon","hi", "whatsup")
outputs = ["hey","Good Morning", "Good Afternoon","Good Evening"," It’s nice to meet you","Pleased to meet you"," How have you been?"," How do you do?","Hey","Hi"," How’s it going?"]

def greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in inputs:
            return random.choice(outputs)
start1= True
print("Hello F-15, I am your personal assistant")

while True:
    get_link = urllib.request.urlopen("https://en.wikipedia.org/wiki/Special:Random")
    soup = bs.BeautifulSoup(get_link, "html.parser")
    title = soup.find(class_="firstHeading").text
    print(f"{title} \nDo you want to question me about it? (Y/N)")
    ans = input("").lower()
    if ans == "y":
        get_link = get_link.read()
        break
    elif ans == "n":
        print("Try again!")
        continue

data = bs.BeautifulSoup(get_link, 'lxml')
data_paragraphs = data.find_all('p')

data_text = ''
for para in data_paragraphs:
    data_text += para.text

data_text = data_text.lower()

data_text = re.sub(r'\[[0-9]*\]', ' ',data_text)
data_text = re.sub(r'\s+',' ',data_text)

sen = nltk.sent_tokenize(data_text)
words = nltk.word_tokenize(data_text)

wnlem = nltk.stem.WordNetLemmatizer()

def lemmatization(tokenized):
    return [wnlem.lemmatize(token) for token in tokenized]

pr = dict((ord(punctuation),None) for punctuation in string.punctuation)

def processed_text(document):
    return lemmatization(nltk.word_tokenize(document.lower().translate(pr)))



from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def generate_response(user_input):
    bot_response = ''
    sen.append(user_input)

    word_vectorizer = TfidfVectorizer(tokenizer=processed_text, stop_words='english')
    word_vectors = word_vectorizer.fit_transform(sen)
    similar_vector_values = cosine_similarity(word_vectors[-1],word_vectors)
    similar_sentence_numbers = similar_vector_values.argsort()[0][-1]

    matched_vector = similar_vector_values.flatten()
    matched_vector.sort()
    vector_matched = matched_vector[-1]
    if vector_matched == 0.0:
        bot_response = bot_response +"I am sorry, I did not understand"
        return bot_response
    else:
        bot_response = bot_response + sen[similar_sentence_numbers]
        return bot_response
    start=True
print(f"Question me about {title} ")
while start == True:
    human = input()
    human = human.lower()
    if human != 'bye':
        if human == 'thanks' or human == 'thank you':
            start = False
            print("You're welcome! From the F-15 team")
        else:
            if greeting_response(human) != None:
                print("F-15 Bot: "+ greeting_response(human))
            else:
                bot_response = generate_response(human)
                if bot_response == human:
                    print("F-15 Bot: I am sorry, I did not understand")
                else:
                    print("F-15 Bot: " + bot_response)
                    sen.remove(human)
    else:
        start = False
        print("F-15 Bot wishes you all the best")

