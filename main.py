import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import json

with open('config.json') as c:
    data = json.load(c)

nowtime = datetime.datetime.now()

datetime_now = datetime.datetime.now()
# test = datetime.datetime(datetime_now.year, datetime_now.month, datetime_now.day, 00, 00, 1)
# midnight = datetime.datetime(datetime_now.year, datetime_now.month, datetime_now.day, 0, 00, 1)
# noon = datetime.datetime(datetime_now.year, datetime_now.month, datetime_now.day, 12, 00, 00)
# fivePM = datetime.datetime(datetime_now.year, datetime_now.month, datetime_now.day, 17, 00, 00)
# tod_responses = ['Good Morning, Sir', 'Good Afternoon, Sir', 'Good Evening, Sir']

engine = pyttsx3.init()
listener = sr.Recognizer()
voices = engine.getProperty('voices')
engine.setProperty('voices', 'com.apple.speech.synthesis.voice.rishi')


# get list of voices
# for voice in voices:
#     print("Voice:")
#     print(" - ID: %s" % voice.id)
#     print(" - Name: %s" % voice.name)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)

# engine.say('Hello. I am Program. How may I be of service?')
# engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


if nowtime.hour >= 19:
    greeting = "Good evening Sir"
    talk("Good evening Sir")

elif nowtime.hour >= 12:
    greeting = "Good afternoon sir"
    talk("Good afternoon sir")

elif nowtime.hour >= 00:
    greeting = "Good morning sir"
    talk("Good morning sir")

# noinspection PyUnboundLocalVariable
print("{}!".format(greeting))


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command



# noinspection PyUnresolvedReferences
def run_program():
    command = take_command()
    if 'dd' in command:
        command = command.replace('dd', '')

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        CurrentTime = datetime.datetime.strftime("%H:%M")
        print("The time is ", CurrentTime)
        talk("The time is", CurrentTime)
        print(data)

    elif 'search' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke('en', 'all'))

    elif 'goodbye' in command:
        talk('Peace out')
        exit()

    elif utterances in command:
        talk('I can tell time, search for info, play YouTube videos, tell jokes, and open applications.')

    elif 'google' in command:
        webbrowser.open('http://google.com', new=2)
        talk('Opening google')

    elif 'block game' or 'minecraft' in command:
        os.system('open -a Minecraft')
        talk('Opening Minecraft')

    elif 'roblox' in command:
        os.system('open -a Roblox')
        talk('Opening Roblox')

    elif 'obs' or 'screen recorder' in command:
        os.system('open -a OBS')
        talk('Opening OBS')

    elif 'spotify' or 'music' in command:
        os.system('open -a Spotify')
        talk('Opening Spotify')

    elif 'lunar client' or 'client' in command:
        os.system('open -a LunarClient')
        talk('Opening Lunar Client')

    elif 'discord' or 'communication' in command:
        os.system('open -a Discord')
        talk('Opening Discord')

    elif 'slack' in command:
        os.system('open -a Slack')
        talk('Opening Slack')



    else:
        talk('I do not understand')


while True:
    run_program()
