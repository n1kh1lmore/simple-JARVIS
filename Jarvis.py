
import pyttsx3
import datetime
from pywhatkit.main import sendMail
import speech_recognition as sr
import pywhatkit
import wikipedia
import webbrowser
import os
import pyjokes
import pyaudio
import random as r
import smtplib
import time
import turtle


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("GOOD MORNING!!")

    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON!!")

    else:
        speak('GOOD Evening!!')
    print('HELLO I AM Jarvis SIR HOW CAN I HELP YOU')
    speak('HELLO I AM Jarvis SIR HOW CAN I HELP YOU')

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
       
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
        if query=='hello':
            speak("hi")
        if query=="what are you doing":
            print('Just helping you out')
            speak('Just helping you out')
          

    except Exception as e:
        # print(e)
        speak("Please say it again...")
        return "none"
    return query

         





if __name__=="__main__":
    wishme()
    while True:
        
        query=takecommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia.....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'wait jarvis' in query:
            time.sleep(5)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%I:%M")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'date' in query:
            speak('sorry, I have a headache')

        elif 'are you single' in query:
            speak('I am in a relationship with wifi') 


        elif 'open code' in query:
            codePath="C:\\Users\\Pratik\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'news' in query:
            webbrowser.open("https://m.dailyhunt.in/news/")
        
        elif 'covid' in query:
            webbrowser.open("https://www.who.int/health-topics/coronavirus#tab=tab_1")

        
        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif 'send email' in query:
            try:
                speak('What should i say?')
                content=takecommand()
                to="wargantiwarom1121@gmail.com"
                sendMail(to,content)
                speak('Email has been sent sir')
            except Exception as e:
                print(e)
                speak('sorry sir unable to send email')

            

        elif "jarvis search" in query:

            import wikipedia as googleScrap
            
            speak("Searching sir.....")
            query=query.replace("Jarvis","")
            query=query.replace("jarvis search","")
            query=query.replace("google","")
        
        
            try:

                # pywhatkit.search(query)
                result=googleScrap.summary(query,3)
                print(result)
                speak(result)
                
            except:
                speak('no speakable')

        elif "stop jarvis" in query:
            speak("Bye sir you can call me anytime ")
            quit()
        
        elif "please draw something" in query:
            def colored_star():


     
    # size of star
                size = 80
                
                # object color
                turtle.color("red")
                
                # object width
                turtle.width(4)
                
                # angle to form star
                angle = 120
                
                # color to fill
                turtle.fillcolor("yellow")
                turtle.begin_fill()
                
                # form star
                for side in range(5):
                    turtle.forward(size)
                    turtle.right(angle)
                    turtle.forward(size)
                    turtle.right(72 - angle)
                    
                # fill color
                turtle.end_fill()
            
# Driver code
            colored_star()
        

        
        elif "i am bored jarvis" in query:
            speak('Ok sir lets have some fun')
            speak('Playing game')
        
            attempts=1
            lst=["g",'w','s']
            player_pt=0
            computer_pt=0


            while attempts<4:
                speak('ENTER YOUR CHOICE: w or s or g')
                player=input("ENTER YOUR CHOICE: w or s or g ")
                computer=r.choice(lst)
                print(f"Computer has chosen {computer}")
                if player=='w' and computer=='g':
                    speak('Hurrah player wins')
                    print("Player wins!!!!\n")
                    player_pt=player_pt+1
                    
                elif player=='s' and computer=='w':
                    speak('Hurrah player wins')
                    print("Player wins!!!\n")
                    player_pt=player_pt+1
                    
                elif player=='g' and computer=='s':
                    speak('Hurrah player wins')
                    print("Player wins\n")
                    player_pt=player_pt+1
                elif player==computer:
                    print("Tie")
                else:
                    speak('Hurrah computer wins')
                    print("computer wins\n")
                    computer_pt=computer_pt+1
                attempts=attempts+1
            time.sleep(5)   
            speak('Calculating points sir')
                

            if player_pt>computer_pt:
                speak('player wins')
                print(f"PLAYER WINS CONGOOO with {player_pt} points")
            else:
                speak('computer wins')
                print(f"COMPUTER WINS and has {computer_pt} points")

        
    
        # elif "play shivaji maharaj song":
        #     music_dir='D:\\music'
        #     songs=os.listdir(music_dir)
        #     os.startfile(os.path.join(music_dir,songs[0]))
        



    

        



            
        
        
    
   
            

        

