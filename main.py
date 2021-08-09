import speech_recognition as sr
import pyttsx3
import pyjokes
import pywhatkit
import wikipedia
from time import strftime, gmtime

joke = pyjokes.get_joke()

listener = sr.Recognizer()
try:
    with sr.Microphone() as src:
        print('listening...')
        voice = listener.listen(src)
        command = listener.recognize_google(voice)
        print(command)

        if command == 'tell me a joke':
            pyttsx3.speak(joke)

        if 'play' in command:
            song = command.replace('play', '')
            pywhatkit.playonyt(song)

        if 'Wikipedia' in command:
            topic = command.replace('wikipedia', '')
            summary = wikipedia.summary(topic)
            pyttsx3.speak(summary)

        if command == 'tell me the time' or 'what is the time now' or 'what\'s the time':
            time_now  = strftime("%H:%M:%S")
            pyttsx3.speak(time_now)

        if command == 'hello':
            pyttsx3.speak('yo wassup boy')
except:
    pass