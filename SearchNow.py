import pyttsx3
import pywhatkit
import webbrowser
import wikipedia

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    query = query.replace('google', '')
    pywhatkit.search(query)

def searchYoutube(query):
    query = query.replace('youtube', '')
    webbrowser.open('https://www.youtube.com/results?search_query=' + query)
    pywhatkit.playonyt(query)
