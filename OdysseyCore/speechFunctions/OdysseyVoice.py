import pyttsx3
from datetime import datetime


class OdysseyVce:
    def __init__(self, engine, USERNAME, BOTNAME):
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

    def changePropertyRate(self, rate):
        self.engine.setProperty('rate', rate)

    def changePropertyVolume(self, volume):
        self.engine.setProperty('volume', volume)
