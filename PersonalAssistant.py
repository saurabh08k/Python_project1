# This is apython program of my persoanl assistant Neon.
# We can carry out some tasks using speech recognition in python.


import datetime
import random
import speech_recognition as sr   # pip install speechRecognition
import pyttsx3  # pip install pyttsx3
import wikipedia # pip install wikipedia
import webbrowser # pip install webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') # print(voices[0].id)
engine.setProperty('voice',voices[0].id)
voiceRate= 160
engine.setProperty('rate',voiceRate ) # voices[o] for david(male voice) and voices[1] for jira(female voice)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if hour>=0 and hour <12:
        speak("Good Morning Saurabh")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Saurabh")
    else:
        speak("Good Evening Saurabh")
    speak("I am Neon how may I help you.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1

        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: , {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':

    wishMe()
    while True:
        query = takeCommand().lower()

        if 'you do' in query:
            introText = "I can do various things like searching wikipedia, open google, linkedin," \
                        " youtube, tell the current time, show your reminders."
            speak(introText)
        elif "how are you" in query:
            text = ["THANKS FOR ASKING I’M DOING WELL", "I am doing great, what can I do for you"]
            speak(random.choice(text))
        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia..")
            speak(results)
        elif 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open("https:\youtube.com")
        elif 'open google' in query:
            speak("opening google...")
            webbrowser.open("https:\google.com")
        elif 'the time' in query:
            timenow = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"Saurabh the time is {timenow}")
        elif 'reminders' in query:
            os.startfile("C:\\Users\\hp ssd\\Downloads\\reminder.txt")
        elif 'open telegram' in query:
            os.startfile("C:\\Users\\hp ssd\\Desktop\\Telegram Web.lnk")
        elif 'open linkedin' in query:
            webbrowser.open("https:\linkedin.com")
        elif 'time kya' in query:
            timenow = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"saurabh the time is {timenow}")
        elif 'quit' in query:
            speak("Goodbye Saurabh")
            exit()

