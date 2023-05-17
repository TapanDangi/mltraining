import pyttsx3
import speech_recognition as sr 
import nltk

spEng = pyttsx3.init()
spEng.setProperty('rate', 100)
spEng.setProperty('volume', 1.0)
voices = spEng.getProperty('voices')
spEng.setProperty('voice', voices[1].id)
spEng.say('Hello World!')
spEng.runAndWait()