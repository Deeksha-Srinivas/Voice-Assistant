import speech_recognition as sr
import pyttsx3

def speak(text):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Capture voice input and convert to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return ""
    except sr.RequestError:
        print("Check your internet connection.")
        return ""
