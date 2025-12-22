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

# Colors for CMD
GREEN = "\033[1;32;40m"
CYAN = "\033[1;36;40m"
RESET = "\033[0m"

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Hindi Voice Setup
found_hindi = False
for voice in voices:
    if "hindi" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        found_hindi = True
        break
if not found_hindi:
    engine.setProperty('voice', voices[0].id) 

engine.setProperty('rate', 180)

def speak(text):
    print(f"{GREEN}JARVIS: {text}{RESET}")
    engine.say(text)
    engine.runAndWait()

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source, duration=0.5)
        print(f"{CYAN}Monitoring for 'Jarvis'...{RESET}")
        audio = listener.listen(source)
    try:
        # Hindi-India recognition
        command = listener.recognize_google(audio, language='hi-IN')
        print(f"User: {command}")
        return command.lower()
    except:
        return ""

def query_api(question):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": "You are JARVIS. Respond in Hinglish (Hindi+English) as a witty personal assistant for Mr. Broken. Be concise."},
            {"role": "user", "content": question}
        ]
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()["choices"][0]["message"]["content"]
    except:
        return "Sir, main mainframe se connect nahi kar paa raha hoon."

def execute_task(command):
    task = command.replace("jarvis", "").strip()
    
    # 1. PC Controls
    if "restart" in task or "computer restart karo" in task:
        speak("Thik hai Sir, system restart kar raha hoon.")
        os.system("shutdown /r /t 5")
    elif "shutdown" in task or "computer band karo" in task:
        speak("Shutdown sequence chalu ho gaya hai. Alvida.")
        os.system("shutdown /s /t 10")
    elif "lock" in task or "pc lock karo" in task:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        speak("System locked.")
    
    # 2. System Settings
    elif "volume up" in task or "aawaz badhao" in task:
        pyautogui.press("volumeup")
    elif "volume down" in task or "aawaz kam karo" in task:
        pyautogui.press("volumedown")
    elif "screenshot" in task:
        pyautogui.screenshot("jarvis_snap.png")
        speak("Screenshot le liya gaya hai.")

    # 3. Automation
    elif "play" in task:
        song = task.replace("play", "").strip()
        speak(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)

    # 4. Fallback to Perplexity AI
    else:
        answer = query_api(task)
        speak(answer)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{GREEN}=== JARVIS MARK VII IS ONLINE ==={RESET}")
    speak("Systems online. Main taiyar hoon, Sir.")
    while True:
        raw_speech = listen()
        if "jarvis" in raw_speech:
            execute_task(raw_speech)
        elif "exit" in raw_speech or "alvida" in raw_speech:
            speak("Powering down. Goodbye Sir.")
            break

if __name__ == "__main__":
    main()
