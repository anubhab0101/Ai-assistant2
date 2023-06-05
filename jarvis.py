import pyttsx3 #pip  install pyttsx3
import speech_recognition as sr #pip install_speechrecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pyautogui #pip install pyautogui
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your Aiassistant. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        speak("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")  
        return "None"
    return query

def shutdown():
    speak("Are you sure you want to shut down the computer?")
    confirm = takeCommand().lower()
    if 'yes' in confirm:
        speak("Shutting down the computer.")
        subprocess.call(["shutdown", "/s"])
    else:
        speak("Shutdown canceled.")

def restart():
    speak("Are you sure you want to restart the computer?")
    confirm = takeCommand().lower()
    if 'yes' in confirm:
        speak("Restarting the computer.")
        subprocess.call(["shutdown", "/r"])
    else:
        speak("Restart canceled.")


def takeScreenshot():
    # Specify the directory where you want to save the screenshots
    screenshot_dir = 'C:\\Screenshots\\'
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    screenshot_path = os.path.join(screenshot_dir, f'screenshot_{timestamp}.png')

    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        speak("Screenshot taken and saved successfully.")

    except Exception as e:
        speak("Sorry, I am unable to take a screenshot at the moment.")



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open instagram' in query:
            webbrowser.open("https://instagram.com")   

        elif 'open watsapp' in query:
            webbrowser.open("https://watsappweb.com")

        elif 'play music' in query:
            music_dir = 'D:\\my fav' #you change the file location as your system's file location
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'open ai' in query:
            webbrowser.open("https://chat.openai.com")

        elif 'tell the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ANUBHABA\\.ipynb_checkpoints" #you change the file location as your system's file location
            os.startfile(codePath)

        elif 'open desktop' in query:
            deck_dir = 'C:\\Users\\ANUBHABA\\OneDrive\\Desktop' #you change the file location as your system's file location
            os.startfile(deck_dir)

        elif 'search' in query:
            search_query = query.replace('search', '')  # Extract the search query
            search_url = 'https://www.google.com/search?q=' + search_query
            webbrowser.open(search_url)

        elif 'take a screenshot' in query:
            takeScreenshot()

        elif 'shutdown' in query:
            shutdown()

        elif 'restart' in query:
            restart()

        elif 'close' in query:
            speak("thank you sir for using me")
            print("jarvis exit")
            break