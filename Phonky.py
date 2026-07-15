import tkinter as tk
from playsound3 import playsound

root = tk.Tk()
label = tk.Label(root, text="Musi-Scan 🎧")
label.place(relx=0.5, rely=0.1, anchor="center")
label.config(font=("Arial", 35, "bold"))

current_sound = None  # will hold the Sound object

def tism():
    global current_sound
    if current_sound is not None and current_sound.is_alive():
        return  # already playing, do nothing
    current_sound = playsound('Lesong.mp3', block=False)

def tism2():
    global current_sound
    if current_sound is not None:
        current_sound.stop()
        current_sound = None

button = tk.Button(root, text="Start", width=25, command=tism)
button.place(relx=0.5, rely=0.5, anchor="center")
button.config(font=("Arial", 35, "bold"))

button2 = tk.Button(root, text="Stop", width=25, command=tism2)
button2.place(relx=0.5, rely=0.6, anchor="center")
button2.config(font=("Arial", 35, "bold"))

root.mainloop()