import nltk
import numpy as np
import random
import string
import bs4 as bs


# List of possible inputs and corresponding outputs for greetings
inputs = ("hey", "hello", "good morning", "good afternoon", "good evening", "morning", "evening", "afternoon", "hi", "whatsup", "how do you do?")
outputs = ["hey", "Good Morning", "It’s nice to meet you", "Pleased to meet you", "How have you been?", "How do you do?", "Hey", "Hi", "How’s it going?"]

start = True
get_link = None
title = ""
sen = []

def get_random_article():
    global get_link, title, sen
    get_link = urllib.request.urlopen("https://en.wikipedia.org/wiki/Special:Random")
    get_link = get_link.read()
    soup = bs.BeautifulSoup(get_link, "html.parser")
    title = soup.find(class_="firstHeading").text
    print(title)

    # Separating the whole content from data into individual paragraphs.
    data = bs.BeautifulSoup(get_link, 'lxml')
    data_paragraphs = data.find_all('p')

    # Creating an empty string named data_text and adding each paragraph from data_paragraphs to it.
    data_text = ''
    for para in data_paragraphs:
        data_text += para.text

    data_text = data_text.lower()

    # Remove patterns enclosed in square brackets followed by digits and replace with a space
    data_text = re.sub(r'\[[0-9]*\]', ' ', data_text)
    # Remove extra whitespace by substituting multiple consecutive whitespace characters with a single space
    data_text = re.sub(r'\s+', ' ', data_text)

    # Tokenize the text into sentences
    sen = nltk.sent_tokenize(data_text)

    # Tokenize the text into words
    words = nltk.word_tokenize(data_text)


def generate_response(user_input):
    bot_response = ''
    # Add user input to the list of sentences
    sen.append(user_input)

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
        # Convert the document to lowercase, remove punctuation, tokenize, and lemmatize
        return lemmatization(nltk.word_tokenize(document.lower().translate(pr)))

    # Import the TfidfVectorizer class from scikit-learn for text feature extraction
    from sklearn.feature_extraction.text import TfidfVectorizer
    # Import the cosine_similarity function from scikit-learn for calculating cosine similarity
    from sklearn.metrics.pairwise import cosine_similarity

    # Create word vectors using TF-IDF vectorization
    word_vectorizer = TfidfVectorizer(tokenizer=processed_text, stop_words='english')
    word_vectors = word_vectorizer.fit_transform(sen)

    # Calculate cosine similarity between the user input vector and all other vectors
    similar_vector_values = cosine_similarity(word_vectors[-1], word_vectors)

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
        bot_response = bot_response + "I am sorry I did not understand"
        return bot_response

    # If there is a meaningful match
    else:
        bot_response = bot_response + sen[similar_sentence_numbers]
        return bot_response


def greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in inputs:
            return random.choice(outputs)

def main():
    global start, get_link, title
    print("Hello F-15, I am your personal assistant")
    get_random_article()
    print(f"Question me on {title}")

    # Create a Tkinter window
    window = tk.Tk()
    window.title("F-15 Bot")
    window.geometry("400x500")

    # Create a text box for displaying the conversation
    textbox = tk.Text(window)
    textbox.pack(pady=10, padx=10)
    textbox.insert(tk.END, "Hello F-15, I am your personal assistant\n")

    # Create an entry field for user input
    entry = tk.Entry(window, width=40)
    entry.pack(pady=10)

    # Create a button for sending the message
    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.pack(pady=10)

    # Start the Tkinter event loop
    window.mainloop()


    def display_response(response):
        textbox.insert(tk.END, "F-15 Bot: " + response + "\n")
        textbox.see(tk.END)


    def send_message():
        # Get user input from the entry field
        user_input = entry.get().lower()
        entry.delete(0, tk.END)

        if user_input != 'bye':
            if user_input == 'thanks' or user_input == 'thank you':
                display_response("Most welcome from our team")
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
            window.after(2000, window.destroy)  # Close the window after 2 seconds
if __name__ == "__main__":
    import threading

    t = threading.Thread(target=main)
    t.start()

main()



