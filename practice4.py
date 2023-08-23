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
        for F in (StartPage, Page1, Page2, Page3, Page4):
  
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
  

#-------------------------------------------------------------------#


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

#start and quit button
        button1= Button (self, text="Start", bg="#FF7C9F", activebackground="#A5C2E9", width=10, font=("Helvetica", 12, "bold"),
                        command = lambda : controller.show_frame(Page1))
        
        button1.place(x=610, y=245)
        button6= Button (self, text="Quit", bg="#A5C2E9", activebackground="#8E699D", width=10, font=("Helvetica", 12, "bold"),
                command = quit)
        button6.place(x=720, y=458)

        
        #adding functions
    def quit(): #quit window
        app.destroy()


#-------------------------------------------------------------------#


# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

#background image
        self.image2= PhotoImage(file="Screenshot (135).png")
        self.start_bg= Label(self, image=self.image2)
        self.start_bg.grid(row=0,column=0)

#question
        Label(self, width="27", text="What is the roman numeral for 50?", fg="white", bg= "black" , font=("helvetica", 14) ).place(x=298, y=165)

#options 
        #option 1 is right
        option1=Radiobutton(self, value="one", font=("helvetica", 12), text="X", bg="#FF7C9F", fg="black")
        option1.place(x=295, y=426)
        option2=Radiobutton(self, value="two", font=("helvetica", 12), text="L", bg="#FF7C9F", fg="black")
        option2.place(x=572, y=426)
        option3=Radiobutton(self, value="three", font=("helvetica", 12), text="V", bg="#FF7C9F", fg="black")
        option3.place(x=300, y=300)
        option4=Radiobutton(self, value="four", font=("helvetica", 12), text="D", bg="#FF7C9F", fg="black")
        option4.place(x=570, y=300)

#next and quit button to show frame 3

        button2= Button (self, text="Next", bg="#43B262", activebackground="#A5C2E9", width=10, font=("Helvetica", 12, "bold"),
                        command = lambda : controller.show_frame(Page2))
        
        button2.place(x=730, y=440)

#-------------------------------------------------------------------#
  
  
# third window frame page2
class Page2(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

#background image
        self.image3= PhotoImage(file="Screenshot (135).png")
        self.start_bg= Label(self, image=self.image3)
        self.start_bg.grid(row=0,column=0)

#question
        Label(self, width="27", text="What is 2864 divided by 2?", fg="white", bg= "black" , font=("helvetica", 14) ).place(x=298, y=165)

#options 
        #option 3 is right
        option1=Radiobutton(self, value="one", font=("helvetica", 12), text="1841", bg="#FF7C9F", fg="black")
        option1.place(x=295, y=426)
        option2=Radiobutton(self, value="two", font=("helvetica", 12), text="1213", bg="#FF7C9F", fg="black")
        option2.place(x=567, y=426)
        option3=Radiobutton(self, value="three", font=("helvetica", 12), text="1432", bg="#FF7C9F", fg="black")
        option3.place(x=295, y=300)
        option4=Radiobutton(self, value="four", font=("helvetica", 12), text="1410", bg="#FF7C9F", fg="black")
        option4.place(x=565, y=300)

#next button to show frame 3

        button3= Button (self, text="Next", bg="#43B262", activebackground="#A5C2E9", width=10, font=("Helvetica", 12, "bold"),
                        command = lambda : controller.show_frame(Page3))
        
        button3.place(x=730, y=440)


#-------------------------------------------------------------------#


class Page3(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

#background image
        self.image4= PhotoImage(file="Screenshot (135).png")
        self.start_bg= Label(self, image=self.image4)
        self.start_bg.grid(row=0,column=0)

#question
        Label(self, width="27", text="What is 92/100 as decimals?", fg="white", bg= "black" , font=("helvetica", 14) ).place(x=298, y=165)

#options 
        #option 2 is right
        option1=Radiobutton(self, value="one", font=("helvetica", 12), text="9.2", bg="#FF7C9F", fg="black")
        option1.place(x=295, y=426)
        option2=Radiobutton(self, value="two", font=("helvetica", 12), text="0.92", bg="#FF7C9F", fg="black")
        option2.place(x=567, y=426)
        option3=Radiobutton(self, value="three", font=("helvetica", 12), text="00.92", bg="#FF7C9F", fg="black")
        option3.place(x=290, y=300)
        option4=Radiobutton(self, value="four", font=("helvetica", 12), text="000.92", bg="#FF7C9F", fg="black")
        option4.place(x=560, y=300)

#next button to show frame 3

        button4= Button (self, text="Next", bg="#43B262", activebackground="#A5C2E9", width=10, font=("Helvetica", 12, "bold"),
                        command = lambda : controller.show_frame(Page4))
        
        button4.place(x=730, y=440)

#-------------------------------------------------------------------#


class Page4(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

#background image
        self.image5= PhotoImage(file="Screenshot (135).png")
        self.start_bg= Label(self, image=self.image5)
        self.start_bg.grid(row=0,column=0)

#question
        Label(self, width="27", text="How many minutes in 3 hours?", fg="white", bg= "black" , font=("helvetica", 14) ).place(x=298, y=165)

#options 
        #option 4 is right
        option1=Radiobutton(self, value="one", font=("helvetica", 12), text="120", bg="#FF7C9F", fg="black")
        option1.place(x=295, y=426)
        option2=Radiobutton(self, value="two", font=("helvetica", 12), text="240", bg="#FF7C9F", fg="black")
        option2.place(x=567, y=426)
        option3=Radiobutton(self, value="three", font=("helvetica", 12), text="90", bg="#FF7C9F", fg="black")
        option3.place(x=295, y=300)
        option4=Radiobutton(self, value="four", font=("helvetica", 12), text="180", bg="#FF7C9F", fg="black")
        option4.place(x=565, y=300)

#next button to show frame 3

        button5= Button (self, text="Next", bg="#43B262", activebackground="#A5C2E9", width=10, font=("Helvetica", 12, "bold"),
                        command = lambda : controller.show_frame(Page1))
        
        button5.place(x=730, y=440)



# Driver Code
app = tkinterApp()
app.title("Shivani<3")
app.geometry("895x505")
app.mainloop()