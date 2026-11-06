import tkinter as tk
from tkinter import messagebox
import cv2
import os
import threading
import pyttsx3
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

engine = pyttsx3.init()
camera = None

root = tk.Tk()
root.title("MEADOW VISION AI")
root.geometry("800x480")
root.configure(bg="#101820")

title = tk.Label(root, text="MEADOW VISION AI",
                 font=("Arial", 25, "bold"),
                 fg="#00ff99", bg="#101820")
title.pack(pady=15)

result = tk.Label(root, text="AI SCANNER READY",
                  font=("Arial", 15), fg="white",
                  bg="#101820", wraplength=700)
result.pack(pady=20)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def scan():
    global camera
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        messagebox.showerror("Camera", "Camera not found")
        return

    ok, frame = camera.read()
    camera.release()

    if not ok:
        return

    filename = "/tmp/meadow_scan.jpg"
    cv2.imwrite(filename, frame)
    result.config(text="Gemini AI is identifying object...")
    threading.Thread(target=identify, args=(filename,), daemon=True).start()

def identify(filename):
    try:
        uploaded = client.files.upload(file=filename)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=["Identify this object. Explain its uses in simple Hinglish.", uploaded]
        )
        answer = response.text
        root.after(0, lambda: result.config(text=answer))
        speak(answer)
    except Exception as e:
        root.after(0, lambda: result.config(text=str(e)))

tk.Button(root, text="SCAN OBJECT", command=scan,
          font=("Arial", 18), bg="#00cc88").pack(pady=20)

root.mainloop()
