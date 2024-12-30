import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engin = pyttsx3.init()
voice = engin.getProperty('voices')
engin.setProperty('voice', voice[1].id)

def talk(text):
    engin.say(text)
    engin.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice_input = listener.listen(source)
            command = listener.recognize_google(voice_input)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
    except sr.RequestError:
        print("Service is unavailable.")
    return ""

def run_alexa():
    command = take_command()
    print(f"Command: {command}")
    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {current_time}')
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        try:
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError:
            talk("There are multiple results. Please specify more.")
        except wikipedia.exceptions.PageError:
            talk("Sorry, I couldn't find information on that.")
    elif 'date' in command:
        talk("Sorry, I am an AI, and I don't go on dates.")
    elif 'are you single' in command:
        talk("I am not single, I am a computer program.")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("Please say the command again.")

while True:
    run_alexa()
