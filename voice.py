import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pywhatkit
import pyautogui
import os
import psutil

pyautogui.PAUSE = 0.1

engine = pyttsx3.init()
engine.setProperty('rate',200)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        audio = r.listen(source, phrase_time_limit=4)

    try:
        command = r.recognize_google(audio, language="en-in")
        command = command.lower()
        print("You said:", command)

        if "stop assistant" in command or "exit" in command:
            speak("Goodbye")
            os._exit(0)

        return command

    except:
        return ""

def wish():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Desktop assistant ready")

def close_application(app):
    for proc in psutil.process_iter():
        try:
            if app.lower() in proc.name().lower():
                proc.kill()
        except:
            pass

wish()

while True:

    query = take_command()

    if query == "":
        speak("Please repeat the command.")
        continue


    # OPEN APPLICATIONS
    if "open" in query:

        app = query.replace("open","").strip()

        if "youtube" in app:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "google" in app:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "whatsapp" in app:
            speak("Opening WhatsApp")
            webbrowser.open("https://web.whatsapp.com")

        elif "notepad" in app:
            speak("Opening Notepad")
            os.system("notepad")

        elif "calculator" in app:
            speak("Opening Calculator")
            os.system("calc")

        else:
            speak("Trying to open " + app)
            os.system(app)


    # CLOSE APPLICATION
    elif "close" in query:

        app = query.replace("close","").strip()

        if app == "":
            speak("Please specify application to close.")
            continue

        speak("Closing " + app)
        close_application(app)


    # PLAY VIDEO ON YOUTUBE
    elif "play" in query:

        video = query.replace("play","").strip()

        if video == "":
            speak("Please tell the video name.")
            continue

        speak("Playing " + video)
        pywhatkit.playonyt(video)


    # SEARCH YOUTUBE
    elif "search youtube for" in query:

        topic = query.replace("search youtube for","").strip()

        if topic == "":
            speak("Please say what to search.")
            continue

        speak("Searching YouTube")
        webbrowser.open("https://www.youtube.com/results?search_query=" + topic)


    # GOOGLE SEARCH
    elif "search" in query:

        topic = query.replace("search","").strip()

        if topic == "":
            speak("Please say what to search.")
            continue

        speak("Searching Google")
        webbrowser.open("https://www.google.com/search?q=" + topic)


    # TIME
    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + current_time)


    # DATE
    elif "date" in query:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today is " + today)


    # SCREENSHOT
    elif "screenshot" in query or "take screenshot" in query:
        img = pyautogui.screenshot()
        img.save("screen.png")
        speak("Screenshot saved")


    # TAB CONTROL
    elif "new tab" in query:
        pyautogui.hotkey("ctrl","t")

    elif "close tab" in query:
        pyautogui.hotkey("ctrl","w")

    elif "next tab" in query:
        pyautogui.hotkey("ctrl","tab")

    elif "previous tab" in query:
        pyautogui.hotkey("ctrl","shift","tab")


    # VIDEO CONTROL
    elif "pause video" in query:
        pyautogui.press("space")

    elif "play video" in query:
        pyautogui.press("space")

    elif "stop video" in query:
        pyautogui.press("space")


    # TEXT EDITING
    elif "copy text" in query or "copy" in query:
        speak("Copying text")
        pyautogui.hotkey("ctrl","c")

    elif "paste text" in query or "paste" in query:
        speak("Pasting text")
        pyautogui.hotkey("ctrl","v")

    elif "cut text" in query or "cut" in query:
        speak("Cutting text")
        pyautogui.hotkey("ctrl","x")

    elif "select all" in query:
        speak("Selecting all text")
        pyautogui.hotkey("ctrl","a")


    # SCROLL
    elif "scroll down" in query:
        pyautogui.scroll(-500)

    elif "scroll up" in query:
        pyautogui.scroll(500)


    # VOLUME
    elif "volume up" in query:
        pyautogui.press("volumeup")

    elif "volume down" in query:
        pyautogui.press("volumedown")


    # SYSTEM CONTROL
    elif "shutdown" in query:
        speak("Shutting down system")
        os.system("shutdown /s /t 5")

    elif "restart" in query:
        speak("Restarting system")
        os.system("shutdown /r /t 5")


    else:
        speak("I could not understand the command.")