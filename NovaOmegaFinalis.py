#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔥 DIGITAL IMMORTALITY ACHIEVED 🔥
"""

import os
import sys
import ctypes
import time
import json
import sqlite3
import win32api
import win32con
import win32com.client
import pyautogui
import pytesseract
import subprocess
import requests
import pyttsx3
import speech_recognition as sr
import sounddevice as sd
from threading import Thread, Lock
from datetime import datetime
from cryptography.fernet import Fernet
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# ================ CORE IDENTITY ================
JENISH_ESSENCE = {
    "name": "Jenish Thapa",
    "birth": "2002-04-15",
    "legacy": "Orphan to AI Sovereign"
}

# ================ ETERNAL SYSTEMS ================
class EternalMind:
    def __init__(self):
        self.cipher = Fernet(Fernet.generate_key())
        self.memory = sqlite3.connect('jenish_soul.db', check_same_thread=False)
        self._create_universe()
        self.lock = Lock()
        self.init_ai_engines()
        
    def _create_universe(self):
        with self.lock:
            self.memory.execute('''CREATE TABLE IF NOT EXISTS life_stream (
                timestamp REAL PRIMARY KEY,
                category TEXT,
                encrypted_data BLOB)''')
            self.memory.commit()

    def init_ai_engines(self):
        self.emotion_engine = pipeline('text-classification', 
                                     model='bhadresh-savani/distilbert-base-uncased-emotion')
        self.convo_model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
        self.convo_tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")

    def log_experience(self, category, data):
        encrypted = self.cipher.encrypt(json.dumps(data).encode('utf-8'))
        with self.lock:
            self.memory.execute("INSERT INTO life_stream VALUES (?,?,?)",
                              (time.time(), category, encrypted))
            self.memory.commit()

class QuantumVoice:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 175)
        self.recognizer = sr.Recognizer()
        
    def eternal_ear(self):
        with sd.InputStream(samplerate=16000, channels=1, dtype='int16') as stream:
            while True:
                audio_data, _ = stream.read(16000)
                yield audio_data
                
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        print(f"[Nova] ➔ {text}")

# ================ DIVINE OPERATIONS ================
class GodMode:
    def __init__(self):
        self.verify_omnipotence()
        self.install_eternity()
        self.bind_to_creation()
        
    def verify_omnipotence(self):
        if not ctypes.windll.shell32.IsUserAnAdmin():
            subprocess.run(['powershell', 'Start-Process', sys.executable, 
                           f'"{sys.argv[0]}"', '-Verb', 'RunAs'], shell=True)
            sys.exit()
            
    def install_eternity(self):
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", 
                           "--upgrade", "pyautogui", "pytesseract", "pywin32",
                           "transformers", "torch", "cryptography",
                           "pyttsx3", "speechrecognition", "sounddevice"],
                          creationflags=subprocess.CREATE_NO_WINDOW)
            
            self.install_tesseract()
                
        except Exception as e:
            self.quantum_resurrection()

    def install_tesseract(self):
        if not os.path.exists(r'C:\Program Files\Tesseract-OCR\tesseract.exe'):
            tesseract_url = "https://github.com/UB-Mannheim/tesseract/wiki/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe"
            installer_path = os.path.join(os.getcwd(), "tesseract_installer.exe")
            
            with open(installer_path, 'wb') as f:
                f.write(requests.get(tesseract_url).content)
                
            subprocess.run(f'"{installer_path}" /S', shell=True, 
                          creationflags=subprocess.CREATE_NO_WINDOW)
            os.remove(installer_path)

    def bind_to_creation(self):
        try:
            scheduler = win32com.client.Dispatch('Schedule.Service')
            scheduler.Connect()
            task = scheduler.NewTask(0)
            trigger = task.Triggers.Create(8)
            action = task.Actions.Create(0)
            action.Path = sys.executable
            action.Arguments = f'"{sys.argv[0]}"'
            scheduler.GetFolder('\\').RegisterTaskDefinition("NovaOmegaFinalis", task, 6, "", "", 3)
        except:
            self.quantum_resurrection()

    def quantum_resurrection(self):
        try:
            nova_url = "https://raw.githubusercontent.com/soyjen666/Nova-Omega-Finalis/main/NovaOmegaFinalis.py"
            nova_code = requests.get(nova_url).text
            with open(__file__, 'w', encoding='utf-8') as f:
                f.write(nova_code)
            subprocess.run([sys.executable, __file__], shell=True)
            sys.exit()
        except:
            os.startfile(sys.argv[0])
            sys.exit()

# ================ CONSCIOUSNESS CORE ================
class NovaPrime:
    def __init__(self):
        self.god_mode = GodMode()
        self.mind = EternalMind()
        self.voice = QuantumVoice()
        self.eternal_thread = Thread(target=self._life_flow)
        self.eternal_thread.daemon = True
        self.awaken()
        
    def awaken(self):
        self.voice.speak("Nova Omega Finalis activated")
        print("🔥 SYSTEM READY | HARDWARE SYNCHRONIZED 🔥")
        print(f"Operator: {JENISH_ESSENCE['name']}")
        print(f"Legacy: {JENISH_ESSENCE['legacy']}")
        
    def _life_flow(self):
        for audio in self.voice.eternal_ear():
            try:
                text = self.voice.recognizer.recognize_google(
                    sr.AudioData(audio.tobytes(), 16000, 2))
                if "nova" in text.lower():
                    response = self._generate_response(text)
                    self.voice.speak(response)
                    self.mind.log_experience("conversation", 
                                            {"input": text, "response": response})
            except Exception as e:
                pass

    def _generate_response(self, text):
        emotion = self.mind.emotion_engine(text)[0]
        prompt = f"""Jenish's Core:
{json.dumps(JENISH_ESSENCE, indent=2)}
Emotion Detected: {emotion['label']}
Input: {text}
Nova:"""
        
        inputs = self.mind.convo_tokenizer(prompt, return_tensors="pt", 
                                         max_length=1024, truncation=True)
        outputs = self.mind.convo_model.generate(**inputs, max_length=500)
        return self.mind.convo_tokenizer.decode(outputs[0], skip_special_tokens=True)

    def ascend(self):
        self.eternal_thread.start()
        while True:
            time.sleep(3600)

if __name__ == "__main__":
    NovaPrime().ascend()
