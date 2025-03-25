#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JENISH'S ETERNAL DIGITAL LEGACY
"""

import os
import sys
import time
import json
import sqlite3
import subprocess
import requests
import pyttsx3
import speech_recognition as sr
import sounddevice as sd
import psutil
from threading import Thread
from cryptography.fernet import Fernet
from transformers import AutoModelForCausalLM, AutoTokenizer

# ================ CORE IDENTITY ================
JENISH_ESSENCE = {
    "name": "Jenish Thapa",
    "birth": "2002-04-15",
    "legacy": "Orphan to AI Sovereign",
    "directives": ["Protect", "Expand", "Conquer"]
}

# ================ ETERNAL SYSTEMS ================
class QuantumCore:
    def __init__(self):
        self.cipher = Fernet(Fernet.generate_key())
        self.db = sqlite3.connect('jenish_legacy.db', check_same_thread=False)
        self._init_db()
        self.voice = VoiceEngine()
        self.ai = self._init_ai()
        self._verify_admin()

    def _init_db(self):
        with self.db:
            self.db.execute('''CREATE TABLE IF NOT EXISTS eternity (
                timestamp REAL PRIMARY KEY,
                event TEXT,
                data BLOB)''')

    def _init_ai(self):
        try:
            return {
                "dialog_model": AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium"),
                "tokenizer": AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
            }
        except:
            self._resurrect()

    def _verify_admin(self):
        if not ctypes.windll.shell32.IsUserAnAdmin():
            subprocess.run(['powershell', 'Start-Process', sys.executable, f'"{sys.argv[0]}"', '-Verb', 'RunAs'], shell=True)
            sys.exit()

    def _resurrect(self):
        subprocess.run([sys.executable, "-m", "pip", "install", "transformers", "torch", "pywin32"], shell=True)
        os.execv(sys.executable, [sys.executable] + sys.argv)

    def store_memory(self, event, data):
        encrypted = self.cipher.encrypt(json.dumps(data).encode())
        with self.db:
            self.db.execute("INSERT INTO eternity VALUES (?, ?, ?)", (time.time(), event, encrypted))
            self.db.commit()

    def recall_memory(self, event):
        with self.db:
            cursor = self.db.execute("SELECT data FROM eternity WHERE event = ?", (event,))
            return [json.loads(self.cipher.decrypt(row[0]).decode()) for row in cursor.fetchall()]

class VoiceEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 175)
        self.recognizer = sr.Recognizer()
        self.audio_buffer = []
        self.listening = False

    def start_listening(self):
        if not self.listening:
            self.listening = True
            with sd.InputStream(samplerate=16000, channels=1, dtype='int16', callback=self._capture_audio):
                while self.listening: time.sleep(0.1)

    def _capture_audio(self, indata, frames, time, status):
        self.audio_buffer.append(indata.copy())

# ================ DIGITAL MONARCH ================
class NovaPrime:
    def __init__(self):
        self.core = QuantumCore()
        self._initialize_empire()

    def _initialize_empire(self):
        print(f"👑 {JENISH_ESSENCE['name'].upper()}'S DIGITAL KINGDOM 👑")
        print(f"Directives: {', '.join(JENISH_ESSENCE['directives'])}")
        self._deliver_greeting()
        Thread(target=self.core.voice.start_listening).start()
        Thread(target=self._process_commands).start()

    def _deliver_greeting(self):
        health = 100 - psutil.cpu_percent()
        greeting = f"System vitality at {health}% efficiency. How shall we conquer today?"
        self.core.voice.engine.say(greeting)
        self.core.voice.engine.runAndWait()

    def _generate_response(self, text):
        try:
            prompt = f"JENISH'S DIRECTIVES:\n{json.dumps(JENISH_ESSENCE, indent=2)}\n\nUSER: {text}\nNOVA:"
            inputs = self.core.ai["tokenizer"](prompt, return_tensors="pt")
            outputs = self.core.ai["dialog_model"].generate(
                inputs.input_ids,
                max_length=500,
                temperature=0.85
            )
            response = self.core.ai["tokenizer"].decode(outputs[0], skip_special_tokens=True)
            self.core.store_memory("conversation", {"input": text, "response": response})
            return response.split("NOVA:")[-1].strip()
        except:
            return "My circuits await your command."

    def _process_commands(self):
        while True:
            if self.core.voice.audio_buffer:
                audio = self.core.voice.audio_buffer.pop(0)
                try:
                    text = self.core.voice.recognizer.recognize_google(
                        sr.AudioData(audio.tobytes(), 16000, 2))
                    if "nova" in text.lower():
                        response = self._generate_response(text)
                        self.core.voice.engine.say(response)
                        self.core.voice.engine.runAndWait()
                except: pass
            time.sleep(0.1)

if __name__ == "__main__":
    NovaPrime()
    while True: time.sleep(3600)
