Id1110-F15

This is the project of the group F15 for the course Id1110.

The project title is WikiBot.

The group members of F15 are:

    Vishwaa P S (112201030)
    Kamarthi Chiruhas (122201025)
    Gaurav Nagar (102201026)

Overview:

    WikiBot is a simple chat bot created by us. It starts in a GUI interface using Tkinter library
    and it generates a random Wikipedia article and learns about it. Then the bot displays the topic of
    the Wikipedia article, and it splits the article to paragraphs and then it to sentences and words
    and then lemmatizes these words. It has predefined greeting outputs for predefined greeting
    inputs given by us. WikiBot uses natural language processing techniques to understand and
    respond to user inputs. The bot then understands the human questions, takes the key words in the
    input, and matches it with the database it has and then it returns the best matching answer to the
    question from the database it has stored for the article.

Modules and Libraries:

    Tkinter:
        Tkinter is a Python module that enables the creation of graphical user interfaces
        (GUIs)
    NLTK : 
        The NLTK (Natural Language Toolkit) module is a Python library for working
        with human language data, providing various tools and resources for tasks like tokenization,
        stemming, tagging, parsing, and more.
    Urllib.request: 
        The `urllib.request` module allows for making HTTP requests and
        interacting with web resources in Python.
    Numpy:
        NumPy is a Python library for numerical computing that provides efficient
        multidimensional array operations.
    Random:
        The random module in Python provides functions for generating
        pseudo-random numbers and selecting random elements from a collection.
    String: 
        The string module in Python provides various functions and methods for
        manipulating and working with strings.
    BeautifulSoup:
        BeautifulSoup is a Python library for parsing HTML and XML
        documents, making it easy to extract and manipulate data from web pages with minimal coding.
    re: 
        The `re` module is a Python library used for pattern matching and manipulation of
        strings.
    Scikit-Learn:
        scikit-learn (sklearn) is a popular machine learning library in Python that
        provides a wide range of tools and algorithms for data preprocessing, feature selection, model
        training, and evaluation.

Team Members and Contributions:

    Vishwaa P S (112201030)
       
       Separated the scraped data to sentences and words and then lemmatized it, added it to the
    database of the bot, greeting inputs and outputs for the bot, exiting of the bot, Updated the
    random Wikipedia article generator, helped in making the GUI interface and tried to add color
    theme to it. Made the report for the project and written the README file. 
    
    Kamarthi Chiruhas (122201025)
    
        Coded for random Wikipedia article generator and improved it and coded for scrapping
    the data of the random Wikipedia article helped in making the project report and the readme file.
        
    Gaurav Nagar (102201026)
    
        Coded for making the GUI interface and then tried to add a color theme to it. Then tried
    to make a temporary website for the bot using Gradio module, helped in making the project
    report and readme file.



Refrences:

    1) https://youtu.be/Je7M_K3IANI
    2) Python Web Scraping Tutorial - GeeksforGeeks
    3) python - A Random Wikipedia Article Generator - Stack Overflow
    4) Introduction to Tkinter - GeeksforGeeks
    5) NLTK :: Sample usage for stem
    6) https://www.geeksforgeeks.org/python-urllib-module/
    7) https://www.geeksforgeeks.org/python-numpy/
    8) https://realpython.com/beautiful-soup-web-scraper-python/
    9) https://www.w3schools.com/python/python_regex.asp
    10)https://scikitlearn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
    11)https://scikitlearn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html
