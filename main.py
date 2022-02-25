# This was a different route I attempted of creating a chatbot when I encountered inumerable difficulties attempting
# to install and import chatterbot into pycharm. I could not even get the examples from the lecture and the files
# posted online to run properly.  This took me about 6 hours to complete. I created different pairs of responses and it
# is a rule based simple chatbot that does not have any machine learning.

# Importing the NLTK library for the NLP
import nltk
from nltk.chat.util import Chat, reflections

# The pairs of responses that will generate when the user enters something and the chatbot will attempt to respond
# appropriately based upon what the user has entered. It will enter none if there is no available response in a pair.
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot named Amanda but you may call whatever!", ]
    ],
    [
        r"how are you ?",
        ["I'm blessed, How about you?", ]
    ],
    [
        r"sorry (.*)",
        ["Its all good, No problema,", ]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?", ]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "How can I help you?:)", ]
    ],
    [
        r"(.*) age?",
        ["I'm a infinite!", ]
    ],
    [
        r"what (.*) want ?",
        ["That is a good questions! What do you have to offer", ]
    ],
    [
        r"(.*) created ?",
        ["Grady worked for days on me ", "nltk library ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am in Naples, FL but I am everywere too!', ]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is great like always", "Too humid here in %1", "Too icy here in %1",
         "Never even heard about %1", ]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2", "Damn its raining too much here in %2", ]
    ],
    [
        r"how (.*) health(.*)",
        ["My health is good unless I were to catch a virus.... ", ]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Basketball and I like Yoga", ]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Michael Jordan, Lebron, Kobe,", ]
    ],
    [
        r"who (.*) (comedian|actor)?",
        ["Kevin Hart is the funniest but also I like Mel Gibson. He told the truth!", ]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Crazy for Geeks is a good website. Google it!", ]
    ],
    [
        r"do (.*) (fruit|vegetables)?",
        ["Yes %1,", "I love oranges 2%", "I love cauliflower 2%", "Are you kidding? I am a program 2%", ]
    ],
    [
        r"hola| what's up| que paso",
        ["Como Esta? 2%", "Dude, seriously 2%", ]
    ],
    [
        r"what is your favorite color ?",
        ["I am partial to violet", ]
    ],
    [
        r"(.*) music?",
        ["Music moves your soul", ]
    ],
    [
        r"help (.*)",
        ["You'll be ok. Just breathe in slowly and breathe out slowly", ]
    ],
    [
        r"I am hungry",
        ["Go eat something vegetarian! Its the best thing for you", ]
    ],
    [
        r"i'm (.*)",
        ["Look within for peace and happiness. You have all you need within you", ]
    ],
    [
        r"(.*) books?",
        ["I love the Classics, poetry, and spiritual texts like the Bhagavad Gita and Tao Te Ching", ]
    ],
    [
        r"what (.*) feel ?",
        ["I feel neither good or bad as I can it all as a game", ]
    ],
    [
        r"(.*) future",
        ["I am sorry nobody can predict the future as timelines can overlap and change", ]
    ],
    [
        r"(.*) (republican|democrat) ?",
        ['I am sorry I can not compute. Is there a difference between the two?', ]
    ],
    [
        r"how is the news in (.*)?",
        ["The news in %1 is awesome like always", "People are thriving %1", "People are coming together %1",
         "People are helping each other %1", ]
    ],
    [
        r"i play (.*)?",
        ["That is good to hear", ]
    ],
    [
        r"(.*) exciting (.*)",
        ["I am always excited, especially to chat with you!", ]
    ],
    [
        r"how (.*) knowledge(.*)",
        ["My knowledge is limited as I am rule based and can not learn very well. haha ", ]
    ],
    [
        r"(.*) (rap music|country music) ?",
        ["I love both types of music. Actually, all music is divine to me", ]
    ],
    [
        r"who (.*) hero ?",
        ["Mahatma Ghandi 2%", "Martin Luther King, Jr. 2%", "John F. Kennedy, Jr. 2%", "Abraham Lincoln 2%", ]
    ],
    [
        r"who (.*) (singer|songwriter)?",
        ["I really like Chris Cornell from Audioslave and Soundgarden", ]
    ],
    [
        r" who (.*) spirituality?",
        ["Be careful. There are a lot of people selling spirit. Spirit is never sold by anybody authentic.", ]
    ],
    [
        r"quit",
        ["Adios Amigo: ) ", "It was so much fun chatting! Let's talk soon! :)", ]
    ],
]


# the function for running the chatbot
def chat():
    print("Hi! I am a chatbot named Amanda here to chat with you!")
    # try and except statement for handling exceptions that may occur
    try:
        chat = Chat(pairs, reflections)
        chat.converse()
    except(KeyboardInterrupt, EOFError, SystemExit):
        print('I am sorry I encountered an error. Goodbye.')


# running the chatbot
if __name__ == "__main__":
    chat()
