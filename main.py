import datetime
import webbrowser
import random
import pyttsx3


def greet():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning Sir!"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon Sir!"
    else:
        greeting = "Good Evening Sir!"
    return greeting


def random_open_link():
    links = [
        "quickdraw.withgoogle.com",
        "elevenlabs.io",
        "teachable-snake.netlify.app",
        "musiclab.chromeexperiments.com/Song-Maker",
        "lexica.art",
        "research.google.com/semantris",
        "g.co/arts/2WST2Pqi1fXRq1kbA"
    ]

    # Open a random link
    link_to_open = random.choice(links)
    webbrowser.open(link_to_open)
    return f"Opening {link_to_open}"


def open_link():
    youtube = 'youtube.com'
    google = 'google.com'
    chatgpt = 'chat.openai.com'
    print("1) YouTube")
    print("2) Google")
    print("3) ChatGPT")
    link_input = input("Enter the link number(1/2/3): ")
    if link_input == '1':
        webbrowser.open(youtube)
        return f"Opening {youtube}"
    elif link_input == '2':
        webbrowser.open(google)
        return f"Opening {google}"
    elif link_input == '3':
        webbrowser.open(chatgpt)
        return f"Opening {chatgpt}"
    else:
        print("Enter a valid response")
        return "Enter a valid response"


# Main Program
print(greet())
pyttsx3.speak(greet())


print("Choose the function")
pyttsx3.speak("Choose the function")
print("1) Open Link")
print("2) Open Random Link")
usr_input = input("Enter 1/2: ")

if usr_input == '1':
    pyttsx3.speak(open_link())
elif usr_input == '2':
    pyttsx3.speak("Do you want to open a random link?")
    user_input = input("Do you want to open a random link? (yes/no): ").strip().lower()
    if user_input == "yes" or "y" or "yeah":
        pyttsx3.speak(random_open_link())
    else:
        print("Okay sir, no link will be opened.")
        pyttsx3.speak("Okay sir, no link will be opened.")
else:
    print("Enter a valid response from the dropdown")
    pyttsx3.speak("Enter a valid response from the dropdown")
