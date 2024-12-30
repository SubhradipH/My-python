import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import tkinter as tk
from tkinter import scrolledtext

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
                return command
    except sr.UnknownValueError:
        return "Sorry, I could not understand."
    except sr.RequestError:
        return "Service is unavailable."
    return ""

def run_alexa():
    command = take_command()
    output_text.delete(1.0, tk.END)  # Clear previous output
    output_text.insert(tk.END, f"Command: {command}\n")
    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {current_time}')
        output_text.insert(tk.END, f'Current time is {current_time}\n')
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        try:
            info = wikipedia.summary(person, 1)
            talk(info)
            output_text.insert(tk.END, f'Info: {info}\n')
        except wikipedia.exceptions.DisambiguationError:
            talk("There are multiple results. Please specify more.")
        except wikipedia.exceptions.PageError:
            talk("Sorry, I couldn't find information on that.")
    elif 'date' in command:
        talk("Sorry, I am an AI, and I don't go on dates.")
    elif 'are you single' in command:
        talk("I am not single, I am a computer program.")
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        output_text.insert(tk.END, f'Joke: {joke}\n')
    else:
        talk("Please say the command again.")
        output_text.insert(tk.END, "Please say the command again.\n")

def start_assistant():
    run_alexa()

# Set up the GUI
root = tk.Tk()
root.title("Voice Assistant")

# Set the window size
root.geometry("600x400")

# Create a label
label = tk.Label(root, text="Welcome to the Voice Assistant", font=("Arial", 16))
label.pack(pady=10)

# Create a button to start the assistant
start_button = tk.Button(root, text="Start Assistant", font=("Arial", 14), command=start_assistant)
start_button.pack(pady=20)

# Create a scrolled text area for the output
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15, font=("Arial", 12))
output_text.pack(pady=10)

# Run the GUI main loop
root.mainloop()
