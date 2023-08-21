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
        
        #creating a frame for NAME

        #image
        self.secondFrame= Frame(parent, bg="white")
        self.secondFrame.grid(row=0, column=0, columnspan=6, sticky=W)
        self.image2= PhotoImage(file="Screenshot (122.1).png")

        #heading
        self.heading_bg=Label(self.secondFrame,image=self.image2)
        self.heading_bg.grid(row=0, column=0, columnspan=6, sticky=W)
        self.heading_bg.grid_propagate(1)

#layout for the left part of the name frame
        self.leftFrame= Frame(self.secondFrame,bg="white")
        self.leftFrame.grid(row=1, column=1, rowspan=5, padx=0)
        self.name_label=Label(
            self.leftFrame, text="    User name: ", bg="white", font=self.fontLabel)
        
        #name
        self.name_label.grid(row=2, column=1, pady=10)
        #age
        self.age_label = Label(
            self.leftFrame, text="    Age: ", bg="white",  font=self.fontLabel)
        self.age_label.grid(row=3, column=1, pady=20)

        #entries for name and age
        self.name_entry= Entry(self.leftFrame,  font=(
            "Slab Serif", 14, ""), width=18, bg="#F9CB9C")
        self.name_entry.grid(row=2, column=2, padx=0, pady=0)
        self.age_entry = Entry(self.leftFrame,  font=(
            "Slab Serif", 14, ""), width=18,  bg="#F9CB9C")
        self.age_entry.grid(row=3, column=2, pady=0)
        #left label
        self.space_label_left = Label(
            self.leftFrame, text="", bg="white", fg="white", font=("", 10, "bold"))
        self.space_label_left.grid(row=4, column=2, pady=2)



#running the code
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Shivani <3")
    root.geometry("895x505")

    Start = Interface(root)
    root.mainloop()
