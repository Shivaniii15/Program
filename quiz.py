from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
from tkinter.font import Font
import csv
from csv import reader


#creating a class for all the interface widgets
class Interface:
    def __init__(self, parent):
        global count, rank #declaring global count
        count=0
        rank=1
        self.fontLabel = Font (
            family="Helvetica", 
            size=10, 
            weight= "bold",
            overstrike=0)
        
#layout for the first page
        self.firstFrame = Frame (parent,bg="white")
        self.firstFrame.grid(row=0, column=0)
        self.image1= PhotoImage(file="Screenshot (122).png")
        self.start_bg= Label(self.firstFrame, image=self.image1)
        self.start_bg.grid(row=1,column=1)
        self.start_btn= Button(
             self.firstFrame, text="Start", bg="#F14975", 
activebackground="#288C70", width=10, font=("Helvetica", 12, 
"bold"))
        self.start_btn.place(relx=0.75, rely=0.5, anchor=CENTER)
        
        #creating a frame for NAME

        self.secondFrame= Frame(parent, bg="white")
        self.secondFrame.grid(row=0, column=0, columnspan=6, sticky=W)
        self.image2= PhotoImage(file="Screenshot (122).png")
        self.heading_bg=Label(self.secondFrame,
image=self.image2)
        self.heading_bg.grid(row=0, column=0, columnspan=6, sticky=W)



#running the code
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Shivani <3")
    root.geometry("895x505")

    Start = Interface(root)
    root.mainloop()
