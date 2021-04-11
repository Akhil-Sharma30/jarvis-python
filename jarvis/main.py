import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import subprocess
import time

engine =pyttsx3.init('sapi5')
voice  =engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir! ,Back online")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir! ,Back online")

    else:
        speak("Good Evening sir! ,back online ")

    speak("I am jarvis how may i help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('supercellakhil75@gmail.com', 'Cambridge@27')
    server.sendmail('supercellakhil75@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia") # to search anything speak this after the sentance
            print(results)
            speak(results)

        elif 'jarvis open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'jarvis open google' in query:
            webbrowser.open("google.com")

        elif 'jarvis open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'jarvis open google classroom' in query:
            codePath = "https://classroom.google.com/u/0/c/MjMyMTA2MDM3Mzg2"
            os.startfile(codePath)

        elif 'jarvis open my website ' in query:
            webbrowser.open('https://akhil-sh.github.io/', new=2)

        elif 'jarvis play music' in query:
            music_dir = 'C:\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'jarvis tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'jarvis send email to Akhil ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "supercellakhil75@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Akhil Sir. I am not able to send this email")

        elif 'jarvis open valorant' in query:
            codePath = "C:\Riot Games\Riot Client\RiotClientServices.exe --launch-product=valorant --launch-patchline=live"
            os.startfile(codePath)

        elif 'jarvis open vs code' in query:
            codePath = "D:\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'jarvis open my website' in query:
            codePath = "https://akhil-sh.github.io/"
            os.startfile(codePath)

        elif 'jarvis open hackerrank' in query:
            codePath = "https://www.hackerrank.com/dashboard"
            os.startfile(codePath)

        elif 'jarvis open calculus book' in query:
            codePath = "file:///C:/Users/Akhil/OneDrive/Desktop/ebook%20of%20cic/Thomas'%20Calculus%20(2018,%20Pearson%20E.L.).pdf"
            os.startfile(codePath)

        elif 'jarvis open ode book' in query:
            codePath = "file:///C:/Users/Akhil/OneDrive/Desktop/ebook%20of%20cic/ODE%20book.pdf"
            os.startfile(codePath)

        elif 'jarvis open csa book' in query:
            codePath = "file:///C:/Users/Akhil/OneDrive/Desktop/ebook%20of%20cic/csa%20book.pdf"
            os.startfile(codePath)

        elif 'jarvis open cs book' in query:
            codePath = "file:///C:/Users/Akhil/OneDrive/Desktop/ebook%20of%20cic/C++,%20The%20Complete%20Reference%20(Herbert%20Schildt,%204th%20Edition).pdf"
            os.startfile(codePath)

        elif 'jarvis open environment book' in query:
            codePath = "file:///C:/Users/Akhil/OneDrive/Desktop/ebook%20of%20cic/Enviromental%20Studies%20book.pdf"
            os.startfile(codePath)

        elif 'jarvis open physics book' in query:
            codePath = "file:///C:/Users/Akhil/OneDrive/Desktop/ebook%20of%20cic/intoduction%20to%20mechanics.pdf"
            os.startfile(codePath)

        elif 'jarvis open github profile' in query:
            codePath = "https://github.com/Ctrl-INTELLIGENC"
            os.startfile(codePath)

        elif 'jarvis open discord' in query:
            codePath = "https://discord.com/channels/@me"
            os.startfile(codePath)

        elif 'jarvis open udemy' in query:
            codePath = "https://www.udemy.com/"
            os.startfile(codePath)

        elif 'jarvis open android studio' in query:
            codePath = "C:\Program Files\Android\Android Studio\bin\studio64.exe"
            os.startfile(codePath)

        elif 'jarvis open whatsapp' in query:
            codePath = "C:\\Users\\Akhil\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)

        elif 'jarvis open atom' in query:
            codePath = "C:\\Users\\Akhil\\AppData\\Local\\atom\\atom.exe"
            os.startfile(codePath)

        elif 'jarvis open github destop' in query:
            codePath = "C:\\Users\\Akhil\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            os.startfile(codePath)

        elif 'jarvis open valorant' in query:
            subprocess.call(['C:\\Riot Games\\Riot Client\\RiotClientServices.exe --launch-product=valorant --launch-patchline=live'])

        elif 'jarvis open epic store' in query:
            codePath = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(codePath)

        elif 'Jarvis open csgo' in query:
            codePath = "steam://rungameid/730"
            os.startfile(codePath)

        elif 'jarvis open stream' in query:
            subprocess.call(['C:\\Program Files (x86)\\Steam\\steam.exe'])

        elif 'Jarvis open exam portal' in query:
            codePath = "https://obe.uod.ac.in/index.php/site/login"
            os.startfile(codePath)

        #elif 'Jarvis set a reminder' in query:
           #speak("Sir,What shall I remind you about?");
           #speak("In how many minutes?");
            #local_time = float(input())
            #local_time = local_time * 60
            #time.sleep(local_time)
            #speak(text);












