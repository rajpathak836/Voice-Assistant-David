import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except:
        speak("Sorry, I did not understand")
        return ""

def get_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {time}")

def set_reminder():
    speak("Reminder has been set successfully")

def check_weather():
    webbrowser.open("https://www.google.com/search?q=weather")
    speak("Showing weather information")

def read_news():
    webbrowser.open("https://news.google.com")
    speak("Here are today's top news")

speak("Voice Assistant Started")

while True:
    command = take_command()

    if "time" in command:
        get_time()
    elif "reminder" in command:
        set_reminder()
    elif "weather" in command:
        check_weather()
    elif "news" in command:
        read_news()
    elif "exit" in command:
        speak("Goodbye")
        break
