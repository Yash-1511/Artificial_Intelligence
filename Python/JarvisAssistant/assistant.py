import pyttsx3 #this will install
import datetime as dt
import speech_recognition as sr #this will install
import pyaudio #this will install
import wikipedia #this will install
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def whishme():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!!")
    else:
        speak("Good Evening!!")
    speak("I am your personal Assistant Sir! Please tell me how may I help you")


def take_command():
    '''
    It takes microphone input from the user and returns string input
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.9
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except Exception as e:
        print("Say that again please..")
        return "None"
    return query


if __name__ == "__main__":
    whishme()
    while True:
        query = take_command().lower()
        # logic
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
    
        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")
    
        elif "open stackoverflow" in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif "open github" in query:
            speak("opening github")
            webbrowser.open("github.com")

        elif "i love you" in query:
            speak("I like hearing that.. I love you too...")

        elif "i miss you" in query:
            speak("Me too, i'm looking forward to our next chat")

        elif "do you love me" in query:
            speak("Today, Tomorrow, Tomorrow ka Tomorrow and forever")

        elif "speak" in query:
            query=query.replace("speak","")
            speak(query)

        elif "what are you doing" in query:
            speak("I offers voice commands,voice searching and voice-activated device control, letting you complete a number of tasks.")
        
        elif "who are you" in query:
            speak("I am you personal Assistant sir.")

        elif "thank you" in query:
            speak("It's my pleasure")

        elif "exit" in query:
            speak("Thankyou")
            break
        else:
            speak("I can not understand")
