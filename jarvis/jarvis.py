import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():

    hour=int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        speak("good morning utsab sir!")
    elif (hour>=12 and hour<18):
        speak("good afternoon utsab sir")
    else:
        speak("good evening uttu sir")
    speak("this is your jarvis please tell how may i help you")

def takeCommand():
    #take microphone input from the user and returns string output
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..!!!")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google( audio , language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None" 
    return query


    
if __name__ == "__main__":
        
    wishMe()

    while True:
    
        query = takeCommand().lower()

            #logic for executing task based on query
        if 'wikipedia' in query: 
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'open facebook' in query:
            webbrowser.open("facebook.com") 

        elif 'play music ' in query:
            music_dir = 'D:\\music project'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[o]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}")

        elif 'open code ' in query:
            codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'email to anish ' in query:
            try:
                speak("what should i say")
                content= takeCommand()
                to="anishamal4real@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("sorry boss i am unable to send these emails")
