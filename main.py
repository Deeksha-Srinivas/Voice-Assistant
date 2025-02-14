from modules.speech import speak, take_command
from modules.commands import open_application, get_time, search_wikipedia

def main():
    speak("Hello! How can I assist you today?")
    
    while True:
        command = take_command()
        
        if "wikipedia" in command:
            query = command.replace("wikipedia", "")
            search_wikipedia(query)
        elif "time" in command:
            speak(f"The current time is {get_time()}")
        elif "open" in command:
            open_application(command)
        elif "exit" in command or "stop" in command:
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("Sorry, I didn't understand that. Can you repeat?")

if __name__ == "__main__":
    main()
