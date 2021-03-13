import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

datetime_now = datetime.datetime.now()
test = datetime.datetime(datetime_now.year, datetime_now.month, datetime_now.day, 17, 00, 1)
midnight = datetime.datetime(datetime_now.year, datetime_now.month, datetime_now.day, 0, 00, 1)
noon = datetime.datetime(datetime_now.year, datetime_now.month, datetime_now.day, 12, 00, 00)
fivePM = datetime.datetime(datetime_now.year, datetime_now.month, datetime_now.day, 17, 00, 00)
tod_responses = ['Good Morning, Sir', 'Good Afternoon, Sir', 'Good Evening, Sir']

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.rishi')

## get list of voices
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




def run_program():
    command = take_command()
    if 'dd' in command:
        command = command.replace('dd', '')


    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('the time is ' + time)
        print(time)

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

    elif 'do' in command:
        talk('I can tell time, search for info, play YouTube videos, and tell jokes')

    else:
        talk('I do not understand')




while True:
    run_program()