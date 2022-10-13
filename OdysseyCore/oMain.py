import pyttsx3
from decouple import config
from datetime import datetime
from speechFunctions import OdysseyVoice
from utilFunctions import OdysseyCmds
USERNAME = config('USER')
BOTNAME = config('BOTNAME')
engine = pyttsx3.init('sapi5')
odyscmds = OdysseyCmds.OdysseyCmds()
odyscmds.printAppNames()
Odyssey = OdysseyVoice.OdysseyVoice(engine, USERNAME, BOTNAME, odyscmds)

Odyssey.greet_user()

Odyssey.take_user_input()

