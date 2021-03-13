from tkinter import *
from PIL import ImageTk, Image

#main window
root = Tk()
root.title("DD")

#image
my_img = ImageTk.PhotoImage(Image.open("blackhole.jfif"))
my_label = Label(image=my_img)
my_label.pack()
























#quit button
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

#runs application until it is stopped
root.mainloop()