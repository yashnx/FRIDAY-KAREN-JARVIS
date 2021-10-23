import pyttsx3
import datetime
import string
import speech_recognition as sr
import wikipedia
import pyjokes
import webbrowser
import pywhatkit as pwt

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)



def speak(tospeak):
    engine.say(tospeak)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning boss")
    elif hour>=12 and hour<=16:
        speak("good afternoon boss")
    else:
        speak("good evening boss")
    speak("Karen Online")
    speak("How would you like me to assist you today")


# making a take command using audio
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print("User said:",query)
    
    return query

    

    

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()


        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        elif 'joke' in query:
            random_joke=pyjokes.get_joke()
            print(random_joke)
            speak(random_joke)
        
        elif 'google' in query:
            
            speak("What would you like to search for?")
            searchtask=takeCommand()
            searchurl=f"https://www.google.com/search?q={searchtask}"
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(searchurl)
            speak(f"here are the results for the search term: {searchtask}")

        elif 'youtube' in query:
            speak("now playing...")
            query=query.replace("youtube","")
            query=query.replace("play","")
            pwt.playonyt(query)

        elif 'stop' in query:
            break


        


        

    
        
       

    

    
    
    