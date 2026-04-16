import cv2
import mediapipe as mp
import pyautogui
import speech_recognition as sr
import threading
import webbrowser
import os
import math
import time
import datetime

# -------------------- INIT --------------------
mp_face = mp.solutions.face_mesh
face = mp_face.FaceMesh(refine_landmarks=True)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

screen_w, screen_h = pyautogui.size()
recognizer = sr.Recognizer()

mode = "eye"
prev_x, prev_y = 0, 0
smoothening = 5

click_down = False
dragging = False
last_click_time = 0

# -------------------- VOICE CONTROL --------------------
def voice_control():
    global mode

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, phrase_time_limit=4)

            command = recognizer.recognize_google(audio).lower()
            print("Voice:", command)

            # -------- MODE SWITCH --------
            if "eye mode" in command:
                mode = "eye"
                print("Eye mode activated")

            elif "hand mode" in command:
                mode = "hand"
                print("Hand mode activated")

            elif "voice mode" in command:
                mode = "voice"
                print("Voice mode activated")

            # -------- APPLICATIONS --------
            elif "open google" in command:
                webbrowser.open("https://google.com")

            elif "open youtube" in command:
                webbrowser.open("https://youtube.com")

            elif "open whatsapp" in command:
                webbrowser.open("https://web.whatsapp.com")

            elif "open notepad" in command:
                os.system("notepad")

            elif "open calculator" in command:
                os.system("calc")

            # -------- SEARCH --------
            elif "search" in command:
                query = command.replace("search", "")
                webbrowser.open(f"https://www.google.com/search?q={query}")

            # -------- SYSTEM CONTROL --------
            elif "shutdown" in command:
                os.system("shutdown /s /t 5")

            elif "restart" in command:
                os.system("shutdown /r /t 5")

            # -------- MOUSE --------
            elif "click" in command:
                pyautogui.click()

            elif "double click" in command:
                pyautogui.doubleClick()

            elif "right click" in command:
                pyautogui.rightClick()

            # -------- KEYBOARD --------
            elif "copy" in command:
                pyautogui.hotkey("ctrl", "c")

            elif "paste" in command:
                pyautogui.hotkey("ctrl", "v")

            elif "select all" in command:
                pyautogui.hotkey("ctrl", "a")

            # -------- TAB CONTROL --------
            elif "new tab" in command:
                pyautogui.hotkey("ctrl", "t")

            elif "close tab" in command:
                pyautogui.hotkey("ctrl", "w")

            # -------- MEDIA --------
            elif "play" in command or "pause" in command:
                pyautogui.press("space")

            # -------- VOLUME --------
            elif "volume up" in command:
                pyautogui.press("volumeup")

            elif "volume down" in command:
                pyautogui.press("volumedown")

            # -------- TIME --------
            elif "time" in command:
                print(datetime.datetime.now().strftime("%H:%M"))

            # -------- EXIT --------
            elif "exit" in command or "stop" in command:
                os._exit(0)

        except:
            pass

threading.Thread(target=voice_control, daemon=True).start()

# -------------------- CAMERA --------------------
cap = cv2.VideoCapture(0)

def distance(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # -------------------- EYE MODE --------------------
    if mode == "eye":
        result = face.process(rgb)
        if result.multi_face_landmarks:
            landmarks = result.multi_face_landmarks[0].landmark
            eye = landmarks[475]

            screen_x = eye.x * screen_w
            screen_y = eye.y * screen_h

            curr_x = prev_x + (screen_x - prev_x) / smoothening
            curr_y = prev_y + (screen_y - prev_y) / smoothening

            pyautogui.moveTo(curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y

    # -------------------- HAND MODE --------------------
    elif mode == "hand":
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            hand = result.multi_hand_landmarks[0]
            lm = hand.landmark

            index = lm[8]
            thumb = lm[4]
            middle = lm[12]

            x = int(index.x * screen_w)
            y = int(index.y * screen_h)

            pyautogui.moveTo(x, y)

            d1 = distance(index, thumb)
            d2 = distance(middle, thumb)

            current_time = time.time()

            # LEFT CLICK
            if d1 < 0.04:
                if current_time - last_click_time < 0.4:
                    pyautogui.doubleClick()
                else:
                    pyautogui.click()
                last_click_time = current_time

            # RIGHT CLICK
            if d2 < 0.04:
                pyautogui.rightClick()
                time.sleep(0.5)

    # -------------------- DISPLAY --------------------
    cv2.putText(frame, f"Mode: {mode.upper()}",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2)

    cv2.imshow("UniAccess System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()