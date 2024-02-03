#installed ->
import pyttsx3	  #pip install pyttsx3
import speech_recognition as sr   #pip install speechRecognition
import datetime	 #pip install datetime 
import wikipedia as wiki   #pip install wikipedia
import pyjokes
import webbrowser #pip install webbrowser
import os   #pip install os
import AppOpener  #pip install AppOpener
import python_weather #pip install python-weather
import requests #pip install requests
import schedule  #pip install schedule
import time #pip install time
import shutil   #pip install shutil
import ctypes   #pip install ctypes
import smtplib	  #pip install smtplib
import turtle  #pip install turtle
from passwords import * #another file 
from email.message import EmailMessage 

# AI voice setup:
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#functions: 
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning  !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon  !")

	else:
		speak("Good Evening  !")

	assname = ("Sphinx 2 point o")
	speak("I am your Assistant")
	speak(assname)

def assname(): #introduction of AI
	speak("heyyy buddy! This is Sphinx at your service")
	speak("how can i help you?")
	print("how can i help you?")

def username(): #accepts command and greets you as per the given command
	speak("What should i call you")
	uname = takeCommand()
	speak("Hello {}".format(uname))
	columns = shutil.get_terminal_size().columns
	
	print("Hello" + uname)
	speak("How can i Help you")

def takeCommand(): # takes command from user and returns query
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		speak("say that again please! with louder voice")
		return takeCommand()
	
	return query

def mail(to, subject, content): #used to send emails just by giving commands
	server = smtplib.SMTP('smtp.gmail.com' , 587)
	server.starttls()
	server.login('Dishajogdeo21@gmail.com', password)
	email = EmailMessage()
	email['From'] = 'Dishajogdeo21@gmail.com'
	email['To'] = to
	email['Subject'] = subject
	email.set_content(content)
	server.send_message(email)

if __name__ == '__main__': #main method
	clear = lambda: os.system('cls')

	clear() #clears the previous lines before running
	wishMe() #called function
	username() #called function

	while True:
		query = takeCommand().lower() # starts the run process and takes command from user

# Basic commands 
		if 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "change my name" in query:
			query = query.replace("change my name to", "")
			assname = query

		elif "change your name" in query:
			speak("What would you like to call me,  ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("Actually ! My name originally is sphinx but you named me {} last time".format(assname))

		elif "who made you" in query or "who created you" in query:
			speak("I have been created by{}".format(username))

		elif "what is my name" in query:
			speak("Your name is {}".format(username))

# main commands:

		elif 'wikipedia' in query:
			speak("what do you wanna search in wikipedia")
			var1 = input()
			results = wiki.summary(var1, sentences = 5)
			speak("according to wikipedia, ")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("opening youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("opening Google\n")
			webbrowser.open("google.com")

		elif 'open stack overflow' in query:
			speak("opening Stack Over flow\n")
			webbrowser.open("stackoverflow.com")

		elif 'time' in query:
			strTime = datetime.datetime.now().strftime("%I:%M:%S")
			speak(f"The time is {strTime}")
			print("the time is:",  strTime)

		elif 'date' in query:
			year = int(datetime.datetime.now().year)
			month = int(datetime.datetime.now().month)
			date = int(datetime.datetime.now().day)
			speak(f"The date is {date,month,year}")
			print("the date is: ", date, month, year)

		elif "who are you" in query:
			speak("I am a virtual assistant or you can say Automated AI bot created by DJ")

		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20,
													0,
													"paste your wallpaper path here ",
													0)
			speak("Background changed successfully")
		
		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

		elif 'joke' in query:
			joke = pyjokes.get_joke()
			speak(joke)
			print(joke)

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif 'search ' in query in query:
			query = query.replace("search", "")	
			webbrowser.open(query)

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://earth.google.com/web/search/" + location + "")
            
		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "write a note" in query:
			speak("What should i write, ")
			note = input()
			file = open('Sphinx.txt', 'w')
			speak(", Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' or "ofcourse" in snfm:
				strTime = datetime.datetime.now().strftime("%I:%M:%S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
			speak("Note Added successfully!")
		
		elif "show note" or 'show me the note'or 'show the note' in query:
			speak("Showing Notes")
			file = open("Sphinx.txt", "r")
			print(file.read())
			speak(file.read(6))

		elif 'email' in query:
			try:
				speak("to whom you wanna send email?")
				to = input()
				speak("what is the subject?")
				subject = takeCommand()
				speak("what message do you wanna send?")
				content = takeCommand()
				mail(to, subject, content)
				speak("email sent successfully...!")
				print("email sent successfully...!")
			except:
				speak("some error occured, Unable to send message!")
				print("ERROR OCCURED!!")

		elif 'search on youtube' in query:
			speak("what do you wanna search on youtube?")
			query = takeCommand()
			webbrowser.open("https://www.youtube.com//results?search_query=" + query + " ")

		else:
			break 
