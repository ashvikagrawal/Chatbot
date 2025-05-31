import nltk
import random
import string

from nltk.chat.util import Chat, reflections
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# Sample patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created with Python.", "I go by many names!"]
    ],
    [
        r"how are you ?",
        ["I'm doing great, thank you!", "I'm fine! How can I assist you?"]
    ],
    [
        r"(.*)(weather|temperature)(.*)",
        ["I can't predict weather yet. But you can check weather.com!",]
    ],
    [
        r"(.*)(help|support)(.*)",
        ["Sure, I'm here to help. Tell me your problem."]
    ],
    [
        r"bye|exit",
        ["Goodbye!", "See you soon!", "Bye, have a nice day!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that.", "Can you rephrase?", "Interesting! Tell me more."]
    ]
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Run chatbot
def start_chat():
    print("Hi! I'm a ChatBot. Type 'bye' to exit.")
    chatbot.converse()

# Run the bot
if __name__ == "__main__":
    start_chat()