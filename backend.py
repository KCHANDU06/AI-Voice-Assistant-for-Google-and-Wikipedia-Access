import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime
import os

# Initialize the speech engine
def speak(text):
    """Convert text to speech."""
    engine = pyttsx3.init('sapi5')  # SAPI5 is a speech API for Windows
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Use the first voice
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def greet_user():
    """Greet the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I assist you today?")

def take_command():
    """Listen for a voice command and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please say that again.")
        speak("Sorry, I didn't catch that. Please say that again.")
        return None
    except sr.RequestError:
        print("Could not connect to the internet.")
        speak("Could not connect to the internet.")
        return None

def search_wikipedia(query):
    """Search Wikipedia for the given query."""
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "").strip()
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("Here is the information I found.")
        print(results)
        speak(results)
    except wikipedia.exceptions.DisambiguationError:
        speak("The term is ambiguous. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find any information on that topic.")
    except Exception as e:
        speak("An error occurred while searching Wikipedia.")

def open_website(url, site_name):
    """Open a website in the default web browser."""
    webbrowser.open(url)
    speak(f"Opening {site_name}")

def tell_time():
    """Tell the current time."""
    str_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {str_time}")

def open_application(path, app_name):
    """Open an application."""
    if os.path.exists(path):
        os.startfile(path)
        speak(f"Opening {app_name}")
    else:
        speak(f"Sorry, I couldn't find {app_name} on your system.")

def process_query(query):
    """Process the user query and execute relevant functions."""
    if "what is your name" in query:
        speak("My Name Is Chitti 2.0 Reloaded")
    elif 'wikipedia' in query:
        search_wikipedia(query)
    elif 'open youtube' in query:
        open_website("https://www.youtube.com", "YouTube")
    elif 'open google' in query:
        open_website("https://www.google.com", "Google")
    elif 'the time' in query:
        tell_time()
    elif 'open code' in query:
        code_path = "C:\\Path\\To\\Your\\CodeEditor.exe"  # Replace with actual path
        open_application(code_path, "Code Editor")
    elif 'exit' in query or 'quit' in query or 'stop conversation' in query:
        speak("Goodbye! See you soon!")
        return False  # Return False to exit the loop in main()
    else:
        speak("I can search the web for you. What would you like me to search?")
        search_query = take_command()
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Here are the search results for {search_query}")
    return True  # Continue running

def main():
    """Main function to run the assistant."""
    greet_user()
    while True:
        query = take_command()
        if query is None:
            continue
        if not process_query(query):  # If False is returned, exit loop
            break

if __name__ == "__main__":
    main()
