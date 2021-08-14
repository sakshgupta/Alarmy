# Importing required libraries
from datetime import datetime   #To set date and time
from playsound import playsound     #To play sound
import pyttsx3      #pip install pyttsx3
import datetime     
import speech_recognition     #pip install speechRecognition
import webbrowser       # to open browser
import os
import random
import time     #to sleep the pgm for few sec

engine = pyttsx3.init('sapi5')          #sapi5 is the speech recognization application developed by Microsoft 
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)    #male voice selected

def speak(audio):
    """Speak function is defined to let the system to speak """
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """ Call the date and time module and help to recogize the time and date which wll help to say GM/GA/GE"""
    hour = int(datetime.datetime.now().hour)    
    if hour >=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hey, I am Alarmy and your personal Alarm Clock, give me a command")

def takeCommand():
    '''
   It takes microphone input from the user and returns string as output
   In simple words it listen your commands and gives the output that you spoked
   '''
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening!!!......")
        r.pause_threshold = 0.9
        r.energy_threshold =380
        r.phrase_threshold = 0.4
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in') # Conversion of audio data to English language 
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception:
        print("Please say that again......")
        speak("Please say that again")
        return "None"

    return query

def validate_time(alarm_time):
    '''
    To Check that the time is valid or not
    '''
    if len(alarm_time) != 4:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 24:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[2:4]) > 59:
            return "Invalid MINUTE format! Please try again..."
        else:
            return "ok"

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks bassed on query
        if 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'set an alarm' in query:
            while True:
                speak("Speak time in 24 hours and in HHMM format")
                print("Speak time in 24 hours and in 'HHMM' format: ")
                alarmy = speech_recognition.Recognizer()    #1152

                with speech_recognition.Microphone() as source:
                    print("Listening...\n")
                    audioCapture = alarmy.listen(source)
                    recognizeText = alarmy.recognize_google(audioCapture)
                    print(recognizeText)
                    recognizeText.replace(" ", "")
                alarm_time = recognizeText
                print(alarm_time)
                validate = validate_time(alarm_time.lower())
                if validate != "ok":
                    print(validate)
                else:
                    print(f"Setting alarm for {alarm_time}...")
                    break

            alarm_hour = alarm_time[0:2]
            alarm_min = alarm_time[2:4]
            alarm_sec = "00"

            while True:
                now = datetime.datetime.now()

                current_hour = now.strftime("%H")
                current_min = now.strftime("%M")
                current_sec = now.strftime("%S")
                # current_period = now.strftime("%p")
                # print(current_hour, current_min, current_sec, current_period)
                # if alarm_period == current_period:
                if alarm_hour == current_hour:
                    if alarm_min == current_min:
                        if alarm_sec == current_sec:
                            print("Wake Up!")
                            path = r'C:\Users\saksh\Music\hooter.wav'
                            playsound(path)
                            break

            speak("Sir, as you are awake now, Do you want to listen to some music")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open news' in query:
            webbrowser.open("https://www.news.google.com")

        elif 'play music'  in query:
            music_dir = r'C:\Users\saksh\Music\English'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randrange(0,len(songs))]))
            speak("Sure!")
            time.sleep(5)

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")     

        elif 'open code' in query:
            codepath = r"C:\Users\saksh\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            speak("Opening VS Code")
            print("<Here it is>")
            os.startfile(codepath)

        elif 'next' in query:
            music_dir = r'C:\Users\saksh\Music\English'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randrange(0,len(songs))]))
            time.sleep(5)
            
        elif 'who made you' in query:
            speak("I was designed by Saksham aka Fortin on 18th Feb 2021")

        elif 'who are you' in query:
            speak("I am a personalised Alarm Clock which can help you wake up with your favorite song")

        elif 'help' in query:
            speak("I can help you with the mentioned things")
            print("Google,PlayMusic,Time,Open code, developer,news,\n At End to close say quit")
            speak("I can open Google ,I can Open Youtube, I can open News ,I can Play Music ,I can tell you time and many more")         

        elif 'quit' in query:
            speak("Okay!")
            speak("Meet you Soon Sir")
            exit(0)                        

        else:
            speak("No match, Try Again!")

