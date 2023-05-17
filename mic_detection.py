import pyttsx3
import speech_recognition as sr 

spEng = pyttsx3.init()
spEng.setProperty('rate', 150)

recognizer = sr.Recognizer()

with sr.Microphone() as mic:
    print('Say:', end=' ')
    audio = recognizer.listen(mic, timeout=1, phrase_time_limit=5)
    try:
        text = recognizer.recognize_google(audio)
        print(text)
        spEng.say(text)
        spEng.runAndWait
    except Exception as err:
        print('\nCould not recognise')