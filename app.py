import streamlit as st
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyautogui
import subprocess

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    speak(greeting)
    return greeting + " I am your AI assistant. Please tell me how may I help you?"

def take_screenshot():
    screenshot_dir = 'C:\\Screenshots\\'
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    screenshot_path = os.path.join(screenshot_dir, f'screenshot_{timestamp}.png')
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        speak("Screenshot taken and saved successfully.")
        return f"Screenshot saved to: {screenshot_path}"
    except Exception as e:
        speak("Sorry, unable to take screenshot.")
        return "Failed to take screenshot."

def shutdown():
    speak("Shutting down the computer.")
    subprocess.call(["shutdown", "/s"])

def restart():
    speak("Restarting the computer.")
    subprocess.call(["shutdown", "/r"])

# Streamlit UI
st.title("🗣️ AI Voice Assistant (Web Interface)")

if st.button("Greet Me"):
    st.success(wish_me())

query = st.text_input("Enter your command")

if query:
    query = query.lower()

    if 'wikipedia' in query:
        st.info("Searching Wikipedia...")
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        st.write(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif 'open google' in query:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif 'open instagram' in query:
        webbrowser.open("https://instagram.com")
        speak("Opening Instagram")

    elif 'open whatsapp' in query:
        webbrowser.open("https://web.whatsapp.com")
        speak("Opening WhatsApp Web")

    elif 'play music' in query:
        music_dir = 'D:\\my fav'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music")

    elif 'open ai' in query:
        webbrowser.open("https://chat.openai.com")
        speak("Opening ChatGPT")

    elif 'tell the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
        st.success(f"The time is {strTime}")

    elif 'take a screenshot' in query:
        result = take_screenshot()
        st.success(result)

    elif 'shutdown' in query:
        st.warning("Shutdown requested. Are you sure?")
        if st.button("Confirm Shutdown"):
            shutdown()

    elif 'restart' in query:
        st.warning("Restart requested. Are you sure?")
        if st.button("Confirm Restart"):
            restart()

    elif 'close' in query:
        speak("Thank you sir for using me")
        st.success("Jarvis exited")

    elif 'search' in query:
        search_query = query.replace('search', '')
        search_url = 'https://www.google.com/search?q=' + search_query
        webbrowser.open(search_url)
        speak(f"Searching for {search_query}")

    else:
        speak("Sorry, I don't understand this command.")
        st.error("Command not recognized.")

