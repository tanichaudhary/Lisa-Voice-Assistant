import pyttsx3 
import speech_recognition as sr
import soundfile as sf
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import threading
from tkinter import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
speak("I am Lisa. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    try:
         server = smtplib.SMTP('smtp.gmail.com', 587)
         server.ehlo()
         server.starttls()
         server.login('youremail@gmail.com', 'your-password')  # Replace with your credentials
         server.sendmail('youremail@gmail.com', to, content)
         server.close()
         speak("Email has been sent succesfully!")
    except Exception as e:
          print(e)
          speak("Unable to send the email.")

def commandHandler():
    query = takeCommand().lower()
    if query == "none":
          return
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email to harry' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "harryyourEmail@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry, I am not able to send this email.")

    elif 'shutdown' in query:
        speak("Shutting down the system. Goodbye!")
        os.system("shutdown /s /t 1")

    elif 'restart' in query:
        speak("Restarting the system. Please wait!")
        os.system("shutdown /r /t 1")

    else:
        speak("Command not recognized. Please try again.")

def runLisa():
    wishMe()
    commandHandler()

# GUI Setup using Tkinter
"""root = Tk()
root.title("Lisa - Your Assistant")
root.geometry("400x300")

label = Label(root, text="Lisa - Your Personal Assistant", font=("Helvetica", 16))
label.pack(pady=10)

btn1 = Button(root, text="Run Lisa", command=runLisa, width=20, height=2)
btn1.pack(pady=20)

btn2 = Button(root, text="Exit", command=root.quit, width=20, height=2)
btn2.pack(pady=10)

root.mainloop()"""

def startLisaThread():
    threading.Thread(target=runLisa).start()

root = Tk()
root.title("Lisa - Your Assistant")
root.geometry("500x350")
root.config(bg="#1e1e2f")

label = Label(root, text="Lisa - Your Personal Assistant", 
              font=("Helvetica", 18, "bold"), 
              bg="#1e1e2f", fg="#ffffff")
label.pack(pady=20)

btn1 = Button(root, text="Run Lisa", command=startLisaThread, 
              width=20, height=2, bg="#2e2e3e", fg="white", 
              font=("Arial", 12, "bold"), relief="flat", cursor="hand2")
btn1.pack(pady=20)

btn2 = Button(root, text="Exit", command=root.quit, 
              width=20, height=2, bg="#d9534f", fg="white", 
              font=("Arial", 12, "bold"), relief="flat", cursor="hand2")
btn2.pack(pady=10)

footer = Label(root, text="Powered by Python & Tkinter", 
               font=("Arial", 10), 
               bg="#1e1e2f", fg="#aaaaaa")
footer.pack(side="bottom", pady=10)

root.mainloop()




