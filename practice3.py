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
"bold"), command=self.start_bg)
        self.start_btn.place(relx=0.75, rely=0.5, anchor=CENTER)
        


#running the code
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Shivani <3")
    root.geometry("895x505")

    Start = Interface(root)
    root.mainloop()