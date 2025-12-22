import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os
import requests
import pyautogui
import subprocess

# --- CONFIGURATION ---
API_KEY = "your_perplexity_api_key_here" 
API_URL = "https://api.perplexity.ai/chat/completions"

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Hindi Voice Check: Windows settings mein 'Hindi' speech pack install hona chahiye
found_hindi = False
for voice in voices:
    if "hindi" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        found_hindi = True
        break

if not found_hindi:
    # Agar hindi voice nahi milti toh default Indian-English voice try karega
    engine.setProperty('voice', voices[0].id) 

engine.setProperty('rate', 175)

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source, duration=0.5)
        print("Main sun raha hoon, Sir...")
        audio = listener.listen(source)
    try:
        # 'hi-IN' stands for Hindi - India
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
            {"role": "system", "content": "You are JARVIS. Respond in Hinglish (Hindi + English) as a witty personal assistant for Mr. Broken."},
            {"role": "user", "content": question}
        ]
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()["choices"][0]["message"]["content"]
    except:
        return "Maaf kijiye Sir, server se sampark nahi ho pa raha hai."

def execute_task(command):
    task = command.replace("jarvis", "").strip()
    
    # 1. PC Power Controls
    if "restart" in task or "band karke chalu" in task:
        speak("Thik hai Sir, main PC restart kar raha hoon.")
        os.system("shutdown /r /t 5")
    elif "shutdown" in task or "band kar do" in task:
        speak("System band ho raha hai. Alvida Sir.")
        os.system("shutdown /s /t 10")
    
    # 2. Daily Tasks
    elif "samay" in task or "time" in task:
        time_str = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Abhi {time_str} ho rahe hain.")
        
    elif "screenshot" in task:
        pyautogui.screenshot("jarvis_snap.png")
        speak("Sir, screenshot le liya gaya hai.")
        
    # 3. Web & AI Queries (Hinglish response)
    else:
        # Har sawal ke liye Perplexity se Hinglish mein answer lega
        answer = query_api(task)
        speak(answer)

def main():
    speak("Systems online. Main taiyar hoon, Sir.")
    while True:
        raw_speech = listen()
        
        # Wake word "Jarvis" detection
        if "jarvis" in raw_speech:
            execute_task(raw_speech)
        elif "alvida" in raw_speech or "exit" in raw_speech:
            speak("Theek hai Sir, apna khayal rakhiyega.")
            break

if __name__ == "__main__":
    main()
