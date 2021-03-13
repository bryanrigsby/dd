import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 is male, 1 is female

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
            if 'dd' in command:
                command = command.replace('dd', '')
    except:
        pass
    return command

def run_program():
    command = take_command()
    if 'play' in command:
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

    elif 'hello' in command:
        talk('What up')

    elif 'do' in command:
        talk('I can tell time, search for info, play YouTube videos, and tell jokes')

    else:
        talk('I do not understand')




talk('Hello. How can I help you?')
while True:
    run_program()