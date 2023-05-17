import pyttsx3
import speech_recognition as sr 
import nltk

spEng = pyttsx3.init()
spEng.setProperty('rate', 150)
spEng.say('Hello Tapan!')

spEng.runAndWait()