import pyttsx3
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetME():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak('Good Morning')
    elif hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('I am David. How may I help you?')
