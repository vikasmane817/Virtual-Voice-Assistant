#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
import random
import time
import datetime
import os
import pyttsx3
import webbrowser
from subprocess import call

from tkinter import *
from urllib.request import urlopen
import json
import pytz

import wikipedia
import pyautogui as pg

strTime = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

try:
    import pywhatkit as kit
except Exception as e:
    speak('remember internet connection is not active')
    print(e)



window = Tk()
window.configure(bg="black")
window.geometry("450x640+650+0")
window.maxsize(640, 640)
window.iconbitmap("icon.ico")

global labelString1
global labelString2

labelString1 = StringVar()
labelString2 = StringVar()






def takeCommand():
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 100
        labelString1.set("Listening...")
        window.update()
        print("Listening...")
        audio = r.listen(source)

        query = ""
        try:
            labelString1.set("Recognizing...")
            window.update()
            query = r.recognize_google(audio,language='en-in')
            print("You said: " + query)

        except sr.UnknownValueError:
            labelString1.set("I am not getting what you have said")
            window.update()
            speak("I am not getting what you have said")

        except sr.RequestError as e:
            print(e)
            labelString1.set("I am not getting what you have said")
            window.update()
            speak("I am not getting what you have said")

        return query.lower()


def greet():
    hour = int(strTime.hour)
    if hour >= 0 and hour < 12:
        window.update()
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        window.update()
        speak("Good Afternoon")

    elif hour >= 18 and hour < 20:
        window.update()
        speak("Good Evening")

    else:
        window.update()
        speak("Good Night")
    speak('How may i help you...')


def jarvis():
    speak('starting your voice assistant')
    time.sleep(1)
    greet()
    while True:


        query = takeCommand()

        if "what time is it" in query or 'Tell me the time' in query:
            labelString2.set(str(strTime.hour) + ' hour ' + str(strTime.minute) + ' minute ' + 'O clock')
            window.update()
            speak(str(strTime.hour) + ' hour ' + str(strTime.minute) + ' minute ' + 'O clock')
   

        elif 'screenshot' in query:
            speak('screenshot is saved...')
            im = pg.screenshot()
            im.save(f'C:\\Users\\Administrator\\Pictures\\Screenshots'
                     f'\\{strTime.year}{strTime.month}{strTime.day}{strTime.hour}{strTime.minute}{strTime.second}.jpeg')
    
        elif 'note' in query or 'notes' in query:
            done=0
            while done == 0:
                speak('Tell me the Title of the note')
                title = takeCommand()
                print(title)
                if title == '':
                    continue
                speak('Tell the content')
                note = takeCommand()
                if note == '':
                    continue
                title.upper()
                f=open('notes.txt','a')
                f.write(f"Title: {title}\t:[{strTime.year}-{strTime.month}-{strTime.day}-{strTime.hour}:{strTime.minute}:{strTime.second}]\n")
                f.write(f"Content: {note}\n\n")
                f.close()
                speak('Note Taken..')
                done=1
      


        elif "exit" in query or "goodbye" in query or "quit" in query:
            labelString2.set(
                "It was nice to meet you, have a good day, bye!!")
            window.update()
            speak(
                "It was nice to meet you, have a good day, bye!!")
            cur.close()

            exit()

        elif "shutdown" in query:
            labelString2.set(
                "Hold On a Sec ! Your system is on its way to shut down")
            window.update()
            speak("Hold On a Sec ! Your system is on its way to shut down")
            os.system("shutdown -s")
         
            cur.close()
     

        elif "open youtube" in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            labelString2.set("Opening Youtube")
            window.update()
            speak("opening youtube")
       

        elif "open github" in query:
            webbrowser.open("https://www.github.com")
            labelString2.set("Opening Github")
            window.update()
            speak("opening github")
            #database('Open github')

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com")
            labelString2.set("Opening Facebook")
            window.update()
            speak("opening facebook")
          

        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com")
            labelString2.set("Opening Instagram")
            window.update()
            speak("opening instagram")
        

        elif "open google" in query:
            webbrowser.open("https://www.google.com")
            labelString2.set("Opening Google")
            window.update()
            speak("opening google")
       

        elif "open yahoo" in query:
            webbrowser.open("https://www.yahoo.com")
            labelString2.set("Opening Yahoo")
            window.update()
            speak("opening yahoo")
        

        elif "open amazon" in query or "shop online" in query:
            webbrowser.open("https://www.amazon.com")
            labelString2.set("Opening Amazon")
            window.update()
            speak("opening amazon")
        

        elif "open flipkart" in query:
            webbrowser.open("https://www.flipkart.com")
            labelString2.set("Opening Flipkart")
            window.update()
            speak("opening flipkart")
         
        elif "what\"s up" in query or "how are you" in query:
            stMsgs = ["Just doing my thing!..what about you!!", "I am fine! thanks. how are you?", "Nice!!!   you..?",
                      "I am nice and full of energy...And you...", "i am okey ! How are you"]
            ans_q = random.choice(stMsgs)
            labelString2.set(ans_q)
            window.update()
            speak(ans_q)
            user_reply = takeCommand()
            if "fine" in user_reply or "ok" in user_reply:
                labelString2.set("That's nice")
                window.update()
                speak("that's nice")
            elif "not" in user_reply or "sad" in user_reply or "upset" in user_reply:
                labelString2.set("Oh Sorry..")
                window.update()
                speak("oh sorry..")
        

        elif "who are you" in query or "about you" in query or "your details" in query:
            labelString2.set("I am Jarvis, Your VOICE Assistant")
            window.update()
            speak("I am JARVIS one point zero, Your VOICE Assistant")
       

        elif "open calculator" in query or "calculator" in query:
            labelString2.set("Opening calculator")
            window.update()
            speak("opening calculator")
            call(["calc.exe"])
           

        elif "open notepad" in query or "notepad" in query:
            labelString2.set("Opening Notepad")
            window.update()
            speak("opening notepad")
            call(["notepad.exe"])
           

        elif 'wikipedia' in query:
            speak("opening wikipedia..")
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            except Exception as e:
                print(e)
                speak("sorry can't find the result at this moment")
          

        elif "search for" in query and "youtube" not in query:
            search_term = query.split("for")[-1]    #search for bollywood
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)
            labelString2.set(
                f"Here is what I found for {search_term} on google")
            window.update()
            speak(f"Here is what I found for {search_term} on google")
        

        elif " on youtube" in query:
            search_term = query.split(" ")[1]
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.get().open(url)
            labelString2.set(f"Here is what I found for {search_term}")
            window.update()
            speak(f"Here is what I found for {search_term} on youtube")
        

        elif "don't listen" in query or "stop listening" in query or "sleep" in query:
            labelString2.set(
                "for how much time you want to stop assistant from listening commands")
            window.update()
            speak("for how much time you want to stop assistant from listening commands")
            a = int(takeCommand())
            labelString2.set("Sleeping..")
            window.update()
            speak("Sleeping..")
            time.sleep(a)

        elif "locate " in query:
            search_term = query.split(" ")[-1]
            url = f"https://www.google.com/maps/place/{search_term}"
            webbrowser.get().open(url)
            labelString2.set(
                f"Here is what I found for {search_term} on google map")
            window.update()
            speak(f"Here is what I found for {search_term} on google map")
         

        elif 'open teams' in query:
            speak("opening microsotf teams..")
            os.startfile(
                "C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft"
                "\\Windows\\Start Menu\\Programs\\Microsoft Teams")
           
        elif 'music' in query:
            speak("Playing your favourite Music..")
            music_dir = 'E:\\Mangesh'
            songs = os.listdir(music_dir)
            for i in songs:
                if i.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, i))
          

        elif 'whatsapp message' in query:
            speak("Message will be sent at defined time..")

            try:
                kit.sendwhatmsg('+91 7028262897', 'message sent by voice assistance: google meet link:  https://meet.google.com/nam-isvu-gdp ', 12, 00)

            except Exception as e:
                print(e)
                speak('Internet connection is not Active')
           



     

        elif 'what you can do' in query or 'features' in query:
            speak("here is the list of my features...")
            speak('I can introduce myself..')
            speak("can take you to some websites like Google, youtube, Facebook, Instagram, yahoo, amazon, flipkart")
            speak('Also can search your queries on google as well as youtube..')
            speak("Can show you different places on google map")
            speak('searching wikipedia..')
            speak('opening youtube..')
            speak('I can tell current time')
            speak('opening notepad..')
            speak('opening teams..')
            speak('opening calculator..')
            speak('I can tell battery status..')
            speak('send whatsapp message...')
            speak('Taking screenshot')
            speak('taking notes')
            speak('also can shutdown your computer..')


        elif 'news' in query:
            try:
                jsonObj = urlopen('http://newsapi.org/v2/top-headlines?'
                                  'country=us&'
                                  'apiKey=ef7399983f78497983b23c2da7e0efcc')

                query = json.load(jsonObj)
                i = 1
                labelString2.set('Here are some top worldwide news : ')
                window.update()
                speak('here are some top worldwide news ')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in query['articles']:
                    if (i > 3):
                        break
                    else:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        speak(str(i) + '. ' + item['title'] + '\n')
                        i += 1

            except Exception as e:
                print(str(e))


def update(ind):
    frame = frames[ind % 1]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)


# initialization

label2 = Label(window, textvariable=labelString2, bg='black')
label2.config(font=("Courier", 10), fg='white')
labelString2.set('.....')
label2.pack()

label1 = Label(window, textvariable=labelString1, bg='black')
label1.config(font=("Courier", 10), fg='white')
labelString1.set('Welcome')
label1.pack()

frames = [PhotoImage(file='assistant.png')]
window.title('VOICE ASSISTANT')

label = Label(window, width=500, height=500)
label.pack()
window.after(0, update, 0)


#starting

jarvis()
window.mainloop()
