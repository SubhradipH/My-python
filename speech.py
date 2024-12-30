import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Please say something:")
    audio = r.listen(source)
    print("time over")
    try:
        print("You said: " + r.recognize_google(audio))
    except:
        print("Sorry, I did not understand what you said.")