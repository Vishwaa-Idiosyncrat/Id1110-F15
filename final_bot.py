import tkinter as tk
import nltk
import numpy as np
import random
import string
import bs4 as bs
import urllib.request
import re
# Import the TfidfVectorizer class from scikit-learn for text
# feature extraction


from sklearn.feature_extraction.text import TfidfVectorizer
# Import the cosine_similarity function from scikit-learn for
# calculating cosine similarity


from sklearn.metrics.pairwise import cosine_similarity

# Function to display the bot's response in the chat window


def display_response(response):
    # Insert the bot's response at the end of the text in the textbox widget
    textbox.insert(tk.END, "F-15 Bot: " + response + "\n")
    # Scroll the textbox widget to the end, making the latest message visible
    textbox.see(tk.END)


def change_theme():
    # Toggle between dark and light mode
    current_theme = window.tk.call("ttk::style", "theme", "use")
    # Check the current theme and switch to the opposite theme
    if current_theme == "clam":
        # Switch to the 'alt' theme
        window.tk.call("ttk::style", "theme", "alt")
    else:
        # Switch to the 'clam' theme
        window.tk.call("ttk::style", "theme", "clam")


# Create a Tkinter window
window = tk.Tk()
window.title("F-15 Bot")
window.geometry("800x800")

# Create a menu bar
menubar = tk.Menu(window)
# Create a submenu for the theme options
theme_menu = tk.Menu(menubar, tearoff=0)
# Add a menu item for toggling the theme
theme_menu.add_command(label="Toggle Theme", command=change_theme)
# Add the theme submenu to the menu bar
menubar.add_cascade(label="Theme", menu=theme_menu)
# Configure the window to use the menu bar
window.config(menu=menubar)

# Create a text box for displaying the conversation
textbox = tk.Text(window)
textbox.pack(pady=10, padx=10)
textbox.insert(tk.END, "Hello F-15, I am your personal assistant\n")

# Create an entry field for user input
entry = tk.Entry(window, width=40)
entry.pack(pady=10)


# List of possible inputs and corresponding outputs for greetings
inputs = ("hey", "hello", "good morning", "good afternoon", "good evening",
          "morning", "evening", "afternoon", "hi", "whatsup", "how do you do?")
outputs = ["hey", "Good Morning", " It’s nice to meet you",
           "Pleased to meet you", " How have you been?", " How do you do?",
           "Hey", "Hi", " How’s it going?"]


start = True

# Get a random Wikipedia article
get_link = urllib.request.urlopen("https://en.wikipedia.org/wiki/Special:Random")
get_link = get_link.read()
soup = bs.BeautifulSoup(get_link, "html.parser")
# This soup object represents the parsed HTML content of the random
# Wikipedia article obtained from the URL.
title = soup.find(class_="firstHeading").text
display_response("Hello, F-15")
display_response(f"Wikipedia Article is on {title}")

# Seperating the whole content from data to individual paragraphs.
data = bs.BeautifulSoup(get_link, 'lxml')
data_paragraphs = data.find_all('p')

# Creating a empty string named data_text and adding each paragraphs
# from data_paragraphs to it.
data_text = ''
for para in data_paragraphs:
    data_text += para.text

data_text = data_text.lower()

# Remove patterns enclosed in square brackets followed by digits
# and replace with a space
data_text = re.sub(r'\[[0-9]*\]', ' ', data_text)
# Remove extra whitespace by substituting multiple consecutive
# whitespace characters with a single space
data_text = re.sub(r'\s+', ' ', data_text)

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


pr = dict((ord(punctuation), None) for punctuation in string.punctuation)
# Define a function for processing text


def processed_text(document):
    # Convert the document to lowercase, remove punctuation, tokenize,
    # and lemmatize
    return lemmatization(nltk.word_tokenize(document.lower().translate(pr)))


def generate_response(user_input):
    bot_response = ''
    # Add user input to the list of sentences
    sen.append(user_input)
    # Create word vectors using TF-IDF vectorization
    word_vectorizer = TfidfVectorizer(tokenizer=processed_text,
                                      stop_words='english')
    word_vectors = word_vectorizer.fit_transform(sen)
    # Calculate cosine similarity between the
    # user input vector and all other vectors
    similar_vector_values = cosine_similarity(word_vectors[-1], word_vectors)
    # Get the index of the most similar sentence
    similar_sentence_numbers = similar_vector_values.argsort()[0][-2]

    # Flatten the similarity scores array into a 1D array
    matched_vector = similar_vector_values.flatten()
    # Sort the similarity scores in ascending order
    matched_vector.sort()
    # Get the second-to-last element from the sorted array, representing
    # the similarity score of the second most similar sentence
    vector_matched = matched_vector[-2]

    # Check if the similarity score is 0.0, indicating no meaningful match
    if vector_matched == 0.0:
        # Append the "I am sorry I did not understand"
        # message to the bot response
        bot_response = bot_response + "I am sorry I did not understand"
        return bot_response

    # If there is a meaningful match
    else:
        bot_response = bot_response + sen[similar_sentence_numbers]
        return bot_response

# Function to greet the user from pre defined list of greetings


def greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in inputs:
            # If user's input is in the predefined list of greeting
            # inputs the bot returns random greetings from the
            # list of predefined oututs
            return random.choice(outputs)


start1 = True

# Displays the following sentence after the wikipedia article has been chosen
display_response(f"Question me on {title} ")

# Function to display the bot's response in the chat window


def display_response(response):
    # Insert the bot's response at the end of the text in the textbox widget
    textbox.insert(tk.END, "F-15 Bot: " + response + "\n")
    # Scroll the textbox widget to the end, making the latest message visible
    textbox.see(tk.END)


def give_command():
    # Get user input from the entry field
    user_input = entry.get().lower()
    # Once the Command button is clicked the input is cleared from the input box
    entry.delete(0, tk.END)

    # Displays the end response message
    if user_input != 'bye':
        if user_input == 'thanks' or user_input == 'thank you':
            display_response("Most welcome from our team")
            # If the end response is not as mentioned above it is either greeting response or it is treated as generate response
        else:
            greeting = greeting_response(user_input)
            if greeting:
                display_response(greeting)
            else:
                response = generate_response(user_input)
                display_response(response)
                sen.remove(user_input)
    else:
        display_response("F-15 Bot wishes you all the best")
        # Close the window after 2 seconds
        window.after(2000, window.destroy)  

# Create a button for sending the message
command_button = tk.Button(window, text="Command", command=give_command)
command_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()


