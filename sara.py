import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib




def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am sara . Please tell me how may I help you")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.5
        r.energy_threshold=2000
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}")

    except Exception as e:
        print(f"say that again please.... {e}")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(os.environ['gmailid'], os.environ['password'])
    server.sendmail(os.environ['gmailid'], to, content)
    server.close()



if __name__ =="__main__":
    WishMe()
    print("done wishing")
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")        

        elif 'play music' in query:
            music_dir = r"c:/Users/KUMA/Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is {strtime}")

        elif 'open code' in query:
            codepath =  r"c:/Users/KUMA/AppData/Local/Programs/Microsoft VS Code/bin/code" 
            os.startfile(codepath)

        elif 'email to raj' in query:
            try:
                speak("what should i say ?")
                content = takecommand()
                to = "raj.makeusmile@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!") 
            except Exception as e:
                print(e)
                speak("sorry email has been not sent")

        elif 'google search for' in  query:
            query = query.replace('search google for', " ")
            speak(f"      {query}")
            url="https://www.google.com/search?q="+query
            webbrowser.open(url)
        elif 'youtube play videos of' in query:
            query = query.replace('youtube play videos of', " ")
            speak(f'          {query}')
            url = 'https://www.youtube.com/results?search_query='+query
            webbrowser.open(url)


