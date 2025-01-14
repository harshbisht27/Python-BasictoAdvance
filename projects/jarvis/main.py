import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import webbrowser
import wikipedia

# Logger setup
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Initialize the pyttsx3 engine
engine = pyttsx3.init()  # Default driver for macOS
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # You can choose another voice if available

def speak(text):
    """
    Converts text to speech.

    Args:
        text (str): Text to be converted to voice.
    """
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    """
    Listens to and recognizes a voice command.

    Returns:
        str: Recognized command as text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        logging.info(e)
        print("Say that again, please.")
        return "None"
    return query

def wish_me():
    """
    Wishes the user based on the current time.
    """
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning sir! How are you doing?")
    elif 12 <= hour < 18:
        speak("Good afternoon sir! How are you doing?")
    else:
        speak("Good evening sir! How are you doing?")
    
    speak("I am JARVIS. Tell me sir, how can I help you?")

# Main program starts here
wish_me()

while True:
    query = takeCommand().lower()
    print(query)

    if "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif "name" in query:
        speak("My name is JARVIS")

    elif "exit" in query:
        speak("Goodbye sir")
        exit()

    elif "open google" in query:
        speak("Ok sir. Please type here what do you want to read")
        webbrowser.open("https://www.google.com")

    elif "open facebook" in query:
        speak("Ok sir. Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "wikipedia" in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
        print(results)
        speak(results)
