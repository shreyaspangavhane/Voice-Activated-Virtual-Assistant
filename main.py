import speech_recognition as sr
import pyttsx3                   # Text to speech conversion
from bot_mechanism import *         # Embedded file of chatbot responses
import pywhatkit                        # Send video, message, etc.
import webbrowser           # Fetch URL in web browser
import wikipedia                
import time
import datetime             # Current time and date
import speedtest                # Check internet speed

from app_urls import app_urls  # Import the dictionary from app_urls.py

r = sr.Recognizer()             # Creates a recognizer to capture voice input
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say('Hey boss, Jarvis is here for you.')
engine.say('Tell me how can I help you')
engine.runAndWait()

def web(website_name):
    if website_name in app_urls:
        url = app_urls[website_name]
        talk(f'Opening {website_name}')
        webbrowser.open(url, new=1)
    else:
        talk('Sorry, the application is not available in the list.')



def voice(): 
    with sr.Microphone() as source:
        print('[listening].....')
        voice = r.listen(source)
        text = r.recognize_google(voice)
        text = text.lower()
        print(text)
    return text

def talk(text):
    engine.say(text)
    engine.runAndWait() 

def run_jarvis():
    command = voice()
    
    if 'play' in command:
        songs = command.replace('play', '')
        talk('playing ' + songs)
        pywhatkit.playonyt(songs)
    
    elif 'hello jarvis' in command or 'hi jarvis' in command or 'hey jarvis' in command:
        bot_voice(command)
    
    elif 'good' in command:
        bot(command)
    
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The time is ' + current_time)
    
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        print(current_date)
        talk('today is ' + current_date)

    elif 'who is' in command:
        wiki = command.replace('who is', '')
        about = wikipedia.summary(wiki, 1)
        print(about)
        talk(about)
    
    elif 'open' in command or 'search' in command or 'what is' in command or 'when' in command or 'website' in command:
        website_name = command.replace('search', '').replace('open', '').replace('website', '').strip()
        web(website_name)
    
    else:
        talk('Sorry, I did not get that. Try again.')

while True:
    run_jarvis()
    engine.runAndWait()
