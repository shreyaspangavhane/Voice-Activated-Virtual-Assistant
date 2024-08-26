# bot_mechanism.py

import pyttsx3

engine = pyttsx3.init()

def bot_voice(command):
    responses = {
        "hello jarvis": "Hello! How can I assist you today?",
        "hi jarvis": "Hi! What can I do for you?",
        "hey jarvis": "Hey! How can I help?",
    }
    response = responses.get(command, "I'm here, what do you need?")
    talk(response)

def bot(command):
    if 'good morning' in command:
        talk('Good morning! Hope you have a great day ahead.')
    elif 'good night' in command:
        talk('Good night! Sleep well.')
    elif 'goodbye' in command:
        talk('Goodbye! See you later.')
    else:
        talk('Glad to hear that!')

def talk(text):
    engine.say(text)
    engine.runAndWait()
