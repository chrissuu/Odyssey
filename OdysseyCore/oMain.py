import pyttsx3
from decouple import config
from datetime import datetime
from speechFunctions import OdysseyVoice
USERNAME = config('USER')
BOTNAME = config('BOTNAME')
engine = pyttsx3.init('sapi5')
Odyssey = OdysseyVoice.OdysseyVce(engine, USERNAME, BOTNAME)

Odyssey.greet_user()

