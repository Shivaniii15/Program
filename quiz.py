from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
from tkinter.font import Font
import csv
from csv import reader


root = Tk()

root.geometry("920x530")


class Quiz:
    def __init__(self, root):
        self.root=root
        self.root.title("Shivani <3")

        #adding canvas for background image
        self.canvas= tk.Canvas(root, width=920, height=530)
        self.canvas.pack()

        self.background_image= PhotoImage(file= "screenshot (96).png")
        self.background_photo= PhotoImage.Tk.PhotoImage(self.background_image)

        #displaying image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)

#running the code
if __name__ == "__main__":
    root.config
    root.title("Shivani <3") #title of the window
    root.mainloop()#make sure it keeps looping
