import cv2
import face_recognition
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os
import sys
import requests
import pyautogui
import subprocess
import screen_brightness_control as sbc

# --- CONFIGURATION ---
API_KEY = "your_perplexity_api_key_here" 
API_URL = "https://api.perplexity.ai/chat/completions"

# CMD Colors
GREEN = "\033[1;32;40m"
CYAN = "\033[1;36;40m"
RED = "\033[1;31;40m"
RESET = "\033[0m"

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Hindi Voice Setup (India)
for voice in voices:
    if "hindi" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break
engine.setProperty('rate', 180)

def speak(text):
    print(f"{GREEN}JARVIS: {text}{RESET}")
    engine.say(text)
    engine.runAndWait()

# --- BIOMETRIC SECTION ---
def face_auth():
    print(f"{CYAN}Scanning face for identity verification...{RESET}")
    try:
        master_img = face_recognition.load_image_file("master_face.jpg")
        master_enc = face_recognition.face_encodings(master_img)[0]
    except:
        print(f"{RED}Error: 'master_face.jpg' not found in folder!{RESET}")
        return False

    cam = cv2.VideoCapture(0)
    auth_success = False
    for _ in range(30): # 30 frames tak try karega
        ret, frame = cam.read()
        if not ret: break
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locs = face_recognition.face_locations(rgb_frame)
        face_encs = face_recognition.face_encodings(rgb_frame, face_locs)

        for enc in face_encs:
            if face_recognition.compare_faces([master_enc], enc)[0]:
                auth_success = True
                break
        if auth_success: break
    
    cam.release()
    cv2.destroyAllWindows()
    return auth_success

# --- VOICE & LOGIC SECTION ---
def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source, duration=0.5)
        print(f"{CYAN}Monitoring...{RESET}")
        audio = listener.listen(source)
    try:
        return listener.recognize_google(audio, language='hi-IN').lower()
    except:
        return ""

def query_ai(question):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": "You are JARVIS. Respond in Hinglish. Be witty and professional. Mention you are secured by face-lock."},
            {"role": "user", "content": question}
        ]
    }
    try:
        res = requests.post(API_URL, headers=headers, json=payload)
        return res.json()["choices"][0]["message"]["content"]
    except:
        return "Sir, connection unstable hai."

def execute(command):
    task = command.replace("jarvis", "").strip()
    
    if "restart" in task:
        speak("PC restart ho raha hai, Sir.")
        os.system("shutdown /r /t 5")
    elif "shutdown" in task:
        speak("System band kar raha hoon.")
        os.system("shutdown /s /t 10")
    elif "screenshot" in task:
        pyautogui.screenshot("jarvis_snap.png")
        speak("Screenshot saved.")
    elif "volume up" in task:
        pyautogui.press("volumeup")
    elif "volume down" in task:
        pyautogui.press("volumedown")
    elif "play" in task:
        song = task.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif "time" in task:
        speak(datetime.datetime.now().strftime("%I:%M %p"))
    else:
        answer = query_ai(task)
        speak(answer)

# --- MAIN ENGINE ---
if __name__ == "__main__":
    os.system('cls')
    print(f"{GREEN}=== JARVIS BIOMETRIC INTERFACE ==={RESET}")
    
    if face_auth():
        speak("Identity verified. Welcome back, Mr. Broken.")
        while True:
            cmd = listen()
            if "jarvis" in cmd:
                execute(cmd)
            elif "exit" in cmd or "alvida" in cmd:
                speak("Going offline. Take care Sir.")
                break
    else:
        speak("Unauthorized access. Systems locked.")
        sys.exit()
