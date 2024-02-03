import pyttsx3 # pip install pyttsx3
import datetime

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
    
def wishme():
    speak("welcome ma'am!")
    speak("the current time is")
    time()
    speak("the current date is")
    date()
    speak("sphinks at your service, your wish is my command")

    wishme()