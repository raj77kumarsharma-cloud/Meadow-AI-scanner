import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("MEADOW AI SCANNER")
root.geometry("800x480")
root.configure(bg="#101820")

title = tk.Label(
    root,
    text="MEADOW AI SCANNER",
    font=("Arial", 28, "bold"),
    fg="#00ff99",
    bg="#101820"
)
title.pack(pady=35)

status = tk.Label(
    root,
    text="SYSTEM READY",
    font=("Arial", 18),
    fg="white",
    bg="#101820"
)
status.pack(pady=15)

def scan():
    messagebox.showinfo("Meadow AI", "Camera scanner will start here.")

button = tk.Button(
    root,
    text="START SCANNER",
    font=("Arial", 18, "bold"),
    bg="#00cc88",
    fg="black",
    command=scan
)
button.pack(pady=30)

root.mainloop()
