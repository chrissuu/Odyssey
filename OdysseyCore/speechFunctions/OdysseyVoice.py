import pyttsx3
import speech_recognition as sr
from datetime import datetime
from OdysseyCore.utils import opening_text
from random import choice


class OdysseyVoice:
    def __init__(self, engine, USERNAME, BOTNAME, OdysseyCmds):
        engine.setProperty('rate', 160)

        # Set Volume
        engine.setProperty('volume', 1.0)

        # Set Voice (Female)
        voices = engine.getProperty('voices')
        print(str(voices))
        engine.setProperty('voice', voices[0].id)

        self.engine = engine
        self.USERNAME = USERNAME
        self.BOTNAME = BOTNAME
        self.pauseThreshold = 0.5
        self.OdysseyCmds = OdysseyCmds

    def speak(self, text):

        self.engine.say(text)
        self.engine.runAndWait()

    def greet_user(self):

        hour = datetime.now().hour
        if (hour >= 6) and (hour < 12):
            self.speak(f"Good Morning {self.USERNAME}")
        elif (hour >= 12) and (hour < 16):
            self.speak(f"Good afternoon {self.USERNAME}")
        elif (hour >= 16) and (hour < 19):
            self.speak(f"Good Evening {self.USERNAME}")
        self.speak(f"I am {self.BOTNAME}. How may I assist you?")

    def take_user_input(self):
        """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
        Odyssey = self

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('Listening....')
            r.pause_threshold = self.pauseThreshold
            audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            if 'exit' in query or 'stop' in query:
                print("stop registered")
                hour = datetime.now().hour
                if 21 <= hour < 6:
                    Odyssey.speak("Good night sir, take care!")
                else:
                    Odyssey.speak('Have a good day sir!')
                exit()
            else:
                Odyssey.speak(choice(opening_text))
                print("Query " + query)
        except Exception:
            Odyssey.speak('Sorry, I could not understand. Could you please say that again?')
            query = 'None'
        return query

    def setPauseThreshold(self, newPauseThreshold):
        self.pauseThreshold = newPauseThreshold

    def setPropertyRate(self, rate):
        self.engine.setProperty('rate', rate)

    def setPropertyVolume(self, volume):
        self.engine.setProperty('volume', volume)


