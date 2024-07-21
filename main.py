import pyttsx3
from datetime import datetime
import webbrowser
import random

engine = pyttsx3.init()


def tts(input_text):
    # Initialize the TTS engine
    engine.say(input_text)


def curtime():
    # Get the current time
    now = datetime.now()

    # Format the time in 24-hour format
    formatted_time = now.strftime("%H:%M:%S")

    # Print the formatted time
    print("Current Time in 24-hour format:", formatted_time)


def display_time_with_greeting():
    # Get the current time
    now = datetime.now()

    # Format the time in 24-hour format
    formatted_time = now.strftime("%H:%M:%S")

    # Print the formatted time
    print("Current Time in 24-hour format:", formatted_time)

    # Determine the appropriate greeting based on the time
    hour = now.hour
    if 5 <= hour < 12:
        tts("Good Morning sir")
        tts("How may I help you?")
    elif 12 <= hour < 17:
        tts("Good Afternoon sir")
        tts("How may I help you?")
    elif 17 <= hour < 0:
        tts("Good Evening sir")
        tts("How may I help you?")
    else:
        tts("Good Midnight sir")
        tts("How may I help you?")


greetings = ["hello", "hi", "sup", "hey", "wassup", "heya"]
request = input("Input the text you want to convert to speech: ")
request = request.lower()

for request in greetings:
    curtime()
    display_time_with_greeting()
    request = input("Input the text you want to convert to speech: ")
    if request.lower in ["open link", "open", "search"]:
        req1 = input("Type the website number you want to visit:"
                     "1.YouTube"
                     "2.Google"
                     "3.ChatGPT"
                     "4.Random ")
        if req1 == "youtube" or '1':
            webbrowser.open_new_tab("https://youtube.com")
        if req1 == "google" or '2':
            webbrowser.open_new_tab("https://google.com")
        if req1 == "chatgpt" or '3':
            webbrowser.open_new_tab("https://chat.openai.com")
        if req1 == "random" or '4':
            webbrowser.open_new_tab(random.choice(["https://quickdraw.withgoogle.com/", "https://elevenlabs.io/",
                                                   "https://teachable-snake.netlify.app/",
                                                   "https://musiclab.chromeexperiments.com/Song-Maker",
                                                   "https://lexica.art/", "https://research.google.com/semantris/",
                                                   "https://g.co/arts/2WST2Pqi1fXRq1kbA"]))

