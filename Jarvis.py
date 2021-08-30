# |\   /|           /\
# | \_/ |  _       /  \
# |     | |_)     /----\  |/ (- |_|  /\  \ /
# |     | | \ o  /      \ |\ _) | | /  \  |

import pyttsx3
from pyttsx3 import engine
import speech_recognition as sr
import os
import webbrowser

#text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[1].id)
engine.setProperty('voice',180)

#to make jarvis speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}")

    except Exception as e:
        speak("say that again please....")
        return "none"
    query = query.lower()
    return query

def wish():
    speak("Hello Sir!")
    speak("Welcome Back ! I am Jarvis your assistant ")

if __name__ == "__main__":
    wish()
    while True:
        query = takecommand()

        if "open notepad" in query:
            speak("Ok Sir! opening notepad")
            notepad = ("C:\\Windows\\system32\\notepad.exe")
            os.startfile(notepad)

        elif "open whatsapp" in query:
            whatsapp = "C:\\Users\\Admin\\AppData\\Local\\WhatsApp"
            os.startfile(whatsapp)

        elif "close notepad" in query:
            speak("ok sir! closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close whatsapp" in query:
            speak("ok sir closing whatsapp")
            os.system("taskkill /f /im whatsapp.exe")

        elif "open youtube" in query:
            speak("ok sir opening youtube")
            webbrowser.open("https://www.youtube.com")
