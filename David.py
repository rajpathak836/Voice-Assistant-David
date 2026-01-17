import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        return query.lower()
    except:
        return ""

if __name__ == "__main__":
    speak("David assistant started")
    while True:
        query = takeCommand()

        if 'wake up david' in query:
            from GreetMe import greetME
            greetME()

        elif 'wikipedia' in query:
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('https://www.google.com')

        elif 'time' in query:
            speak(datetime.datetime.now().strftime('%H:%M:%S'))

        elif 'exit' in query:
            speak('Goodbye')
            break
