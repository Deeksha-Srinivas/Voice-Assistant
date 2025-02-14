import wikipedia
import webbrowser
import os
import datetime
from modules.speech import speak

def open_application(command):
    """Open applications based on voice command."""
    if "notepad" in command:
        os.system("notepad")
    elif "calculator" in command:
        os.system("calc")
    elif "browser" in command:
        webbrowser.open("https://www.google.com")
    else:
        speak("Sorry, I cannot open that application.")

def get_time():
    """Fetch the current system time."""
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def search_wikipedia(query):
    """Search Wikipedia and return summary."""
    speak("Searching Wikipedia...")
    result = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia, ")
    speak(result)
