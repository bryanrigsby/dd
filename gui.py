import tkinter as tk
import os
from PIL import ImageTk, Image

#main window
window= tk.Tk()
window.title("DD")

label = tk.Label(text="Welcome Sir")
label.pack()

#restart button
def restart():
    os.system('open /Users/bryanrigsby/Documents/GitHub/dd/dist/main')

button_restart = tk.Button(window, text="Restart", fg="black", command=restart)
button_restart.pack()

#runs application until it is stopped
window.mainloop()