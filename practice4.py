import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
from tkinter.font import Font
import tkinter.font as font
from typing import Self

  
LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
     
# __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
# __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
# creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
# initializing frames to an empty array
        self.frames = {} 
  
# iterating through a tuple consisting
# of the different page layouts
        for F in (StartPage, Page1, Page2):
  
            frame = F(container, self)
  
# initializing frame of that object from
# startpage, page1, page2 respectively with
# for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
# to display the current frame passed as
# parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  


# first window frame startpage  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

#background image
        self.image1= PhotoImage(file="Screenshot (122).png")
        self.start_bg= Label(self, image=self.image1)
        self.start_bg.grid(row=0,column=0)

#labels and entries
        Label(self, width="8", text="Name", fg="black", bg= "#43B262" , font=("helvetica", 14) ).place(x=250, y=200)

        entry_name=Entry(self, width=18, font=("helvetica", 14), fg= "#C63861")
        entry_name.place(x=350,y=200 )

        Label(self, width="8", text="Age", fg="black", bg= "#43B262" , font=("helvetica", 14) ).place(x=250, y=300)

        entry_age=Entry(self, width=18, font=("helvetica", 14),  fg= "#C63861")
        entry_age.place(x=350,y=300 )

#start button
        button1= Button (self, text="Start", bg="#F14975", activebackground="#288C70", width=10, font=("Helvetica", 12, "bold"),
                        command = lambda : controller.show_frame(Page2))
        
        button1.place(x=610, y=245)
 

# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #background image
        self.image1= PhotoImage(file="Screenshot (96).png")
        self.start_bg= Label(self, image=self.image1)
        self.start_bg.grid(row=0,column=0)


        Label(self, width="8", text="Age", fg="black", bg= "#43B262" , font=("helvetica", 14) ).place(x=250, y=300)

  
        # button to show frame 2 with text
        # layout2

        button2= Button (self, text="Next",bg='#F14975', fg='white', activebackground='#288C70',
                        command = lambda : controller.show_frame(Page2))

  
  
  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #background image
        self.image1= PhotoImage(file="Screenshot (122).png")
        self.start_bg= Label(self, image=self.image1)
        self.start_bg.grid(row=0,column=0)

        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
def main():
    global app, self, user_details, total_entries

    user_details=[]#create an empty list
    total_entries= 0

# Driver Code
app = tkinterApp()
app.geometry("895x505")
app.mainloop()