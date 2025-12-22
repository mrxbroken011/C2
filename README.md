# 🤖 JARVIS Mark VII - Advanced AI Assistant

**JARVIS** ek voice-controlled PC assistant hai jo **Perplexity AI** (Sonar-Pro) ki power aur **Biometric Face Recognition** ki security ke saath aata hai. Yeh aapke PC ko control kar sakta hai, sawalon ke jawab de sakta hai, aur sirf aapka chehra dekh kar hi unlock hota hai.

## ✨ Features

* **🔒 Biometric Security:** Sirf Master Face (`master_face.jpg`) ko pehchante hi system access deta hai.
* **🗣️ Bilingual Support:** Hindi aur English (Hinglish) dono mein baat karta hai.
* **🌐 Real-time Intelligence:** Perplexity API ka use karke internet se taaza jankari nikalta hai.
* **💻 System Control:** Volume control, Shutdown, Restart, Screenshot, aur Apps open/close karne ki kshamta.
* **🚀 One-Click Launch:** Admin privileges ke saath shortcut batch file se start hota hai.

---

## 🛠️ Installation & Setup

### 1. Requirements

Sabse pehle Python install karein, fir CMD mein niche di gayi libraries install karein:

```bash
pip install opencv-python face-recognition speechrecognition pyttsx3 pywhatkit wikipedia pyjokes requests pyautogui screen-brightness-control

```

### 2. Project Structure

Saari files ko ek hi folder mein rakhein:

* `jarvis_pro.py` (Main Python Script)
* `Launch_Jarvis.bat` (Startup Batch File)
* `master_face.jpg` (Aapki high-quality photo)

### 3. Configuration

`jarvis_pro.py` file ko edit karein aur apni **Perplexity API Key** yahan dalein:

```python
API_KEY = "your_api_key_here"

```

---

## 🎙️ How to Use

1. **Launch:** `Launch_Jarvis.bat` par right-click karein aur **Run as Administrator** karein.
2. **Auth:** Camera khulega, apna chehra dikhayein.
3. **Command:** Jab JARVIS kahe "Systems Online", tab bolein:
* *"Jarvis, volume badhao"*
* *"Jarvis, screenshot lo"*
* *"Jarvis, play Arijit Singh songs"*
* *"Jarvis, aaj ki news kya hai?"*


4. **Exit:** Boolein *"Jarvis, alvida"* ya *"Exit"*.

---

## ⚠️ Important Notes

* **Camera:** Face recognition ke waqt light achhi honi chahiye.
* **Microphone:** Default mic settings sahi honi chahiye.
* **Admin Rights:** System commands (restart/shutdown) ke liye Admin mode zaroori hai.

---

**Sir, README ready hai! Kya main aapke liye is project ka ek "Demo Video" script likhoon ya kuch aur upgrade karoon?**
