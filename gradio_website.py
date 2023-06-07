import nltk
import numpy as np
import random
import string
import bs4 as bs
import urllib.request
import re
import gradio as gr
# List of possible inputs and corresponding outputs for greetings
inputs = ("hey","hello","good morning", "good afternoon","good evening","morning","evening","afternoon","hi", "whatsup","how do you do?")
outputs = ["hey","Good Morning"," It’s nice to meet you","Pleased to meet you"," How have you been?"," How do you do?","Hey","Hi"," How’s it going?"]
input_textbox=gr.inputs.Textbox(label="user_input")

output_textbox=gr.outputs.Textbox(lines=1,label="user_output")


start = True
print("Hello F-15, I am your personal assistant")
# Get a random Wikipedia article
get_link = urllib.request.urlopen("https://en.wikipedia.org/wiki/Special:Random")
get_link = get_link.read()
soup = bs.BeautifulSoup(get_link, "html.parser")
    # This soup object represents the parsed HTML content of the random Wikipedia article obtained from the URL.
title = soup.find(class_="firstHeading").text
print(title)

# Seperating the whole content from data to individual paragraphs.
data = bs.BeautifulSoup(get_link, 'lxml')
data_paragraphs = data.find_all('p')

# Creating a empty string named data_text and adding each paragraphs from data_paragraphs to it.
data_text = ''
for para in data_paragraphs:
    data_text += para.text

data_text = data_text.lower()

# Remove patterns enclosed in square brackets followed by digits and replace with a space
data_text = re.sub(r'\[[0-9]*\]', ' ',data_text)
# Remove extra whitespace by substituting multiple consecutive whitespace characters with a single space
data_text = re.sub(r'\s+',' ',data_text)

# Tokenize the text into sentences
sen = nltk.sent_tokenize(data_text)
# Tokenize the text into words
words = nltk.word_tokenize(data_text)

# Create an instance of WordNetLemmatizer for lemmatization
wnlem = nltk.stem.WordNetLemmatizer()
# Define a function for lemmatization
def lemmatization(tokenized):
    # Lemmatize each token using the WordNetLemmatizer instance
    return [wnlem.lemmatize(token) for token in tokenized]

# Create a translation table to remove punctuation marks
pr = dict((ord(punctuation),None) for punctuation in string.punctuation)
# Define a function for processing text
def processed_text(document):
    # Convert the document to lowercase, remove punctuation, tokenize, and lemmatize
    return lemmatization(nltk.word_tokenize(document.lower().translate(pr)))

# Import the TfidfVectorizer class from scikit-learn for text feature extraction       
from sklearn.feature_extraction.text import TfidfVectorizer
# Import the cosine_similarity function from scikit-learn for calculating cosine similarity
from sklearn.metrics.pairwise import cosine_similarity

def generate_response(user_input):
    bot_response = ''
    # Add user input to the list of sentences
    sen.append(user_input)
    # Create word vectors using TF-IDF vectorization
    word_vectorizer = TfidfVectorizer(tokenizer=processed_text, stop_words='english')
    word_vectors = word_vectorizer.fit_transform(sen)
    # Calculate cosine similarity between the user input vector and all other vectors
    similar_vector_values = cosine_similarity(word_vectors[-1],word_vectors)
    # Get the index of the most similar sentence
    similar_sentence_numbers = similar_vector_values.argsort()[0][-2]

    # Flatten the similarity scores array into a 1D array
    matched_vector = similar_vector_values.flatten()
    # Sort the similarity scores in ascending order
    matched_vector.sort()
    # Get the second-to-last element from the sorted array, representing the similarity score of the second most similar sentence
    vector_matched = matched_vector[-2]

    # Check if the similarity score is 0.0, indicating no meaningful match
    if vector_matched == 0.0:
        # Append the "I am sorry I did not understand" message to the bot response
        bot_response = bot_response +"I am sorry I did not understand"
        return bot_response
    
    # If there is a meaningful match
    else:
        bot_response = bot_response + sen[similar_sentence_numbers]
        return bot_response
    
def greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in inputs:
            return random.choice(outputs)
    
def process_text(user_input):
    user_input=input_textbox.read()
    
  
    if greeting_response(human) != None:
        return "F-15 Bot: " + greeting_response(user_input)

    return  "F-15:"+ generate_response(user_input)

interface=gr.Interface(fn=process_text,inputs=input_textbox,outputs=output_textbox,title="F-15 assistant")

interface.launch(share=True)



# start1=True
# print(f"Question me on {title} ")
while start == True:
    human = input()
    human = human.lower()
    if human != 'bye':
        if human == 'thanks' or human == 'thank you':
            start = False
            print("Most welcome from our team")
        else:
            if greeting_response(human) != None:
                print("F-15 Bot: "+ greeting_response(human))
            else:
                print("F-15 Bot: ",end ='')
                print(generate_response(human))
                sen.remove(human)
                # This removes user input from the list of sentences
    else:
        start = False
        print("Sure! If you have any more questions in the future, feel free to ask. Have a great day! Goodbye!")
