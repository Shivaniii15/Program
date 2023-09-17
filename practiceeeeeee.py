import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
from tkinter.font import Font
import tkinter.font as font
  
#adding functions
def quit(): #quit window
    app.destroy()

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
        for F in (StartPage, Page1, Page2, Page3, Page4, Page5):
  
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
  

#--------------------------# first window frame (startpage)-----------------------------#


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller=controller
        self.create_widgets()

#adding widgets under a function
    def create_widgets(self):

#background image
        self.image1= PhotoImage(file="Screenshot (122).png")
        self.start_bg= Label(self, image=self.image1)
        self.start_bg.grid(row=0,column=0)

#labels and entries
        Label(self, width="8", text="Name", fg="black", bg= "#43B262" , font=("helvetica", 14) ).place(x=250, y=200)

        self.entry_name=Entry(self, width=18, font=("helvetica", 14), fg= "#C63861")
        self.entry_name.place(x=350,y=200 )

        Label(self, width="8", text="Age", fg="black", bg= "#43B262" , font=("helvetica", 14) ).place(x=250, y=300)

        self.entry_age=Entry(self, width=18, font=("helvetica", 14),  fg= "#C63861")
        self.entry_age.place(x=350,y=300 )

#start and quit button
        self.button1= Button (self, text="Start", bg="#FF7C9F", activebackground="#A5C2E9", width=10, font=("Helvetica", 12, "bold"),
                        command = self.start_quiz)        
        self.button1.place(x=610, y=245)


        self.button6= Button (self, text="Quit", bg="#A5C2E9", activebackground="#8E699D", width=10, font=("Helvetica", 12, "bold"),
                command = quit)
        self.button6.place(x=720, y=458)
        self.button6= Button (self, text="Home", bg="#A5C2E9", activebackground="#8E699D", width=10, font=("Helvetica", 12, "bold"),
                command = quit)
        self.button6.place(x=720, y=458)


#defining the start_quiz function

    def start_quiz(self):

        name = self.entry_name.get()
        age = self.entry_age.get()

#clear previous error message
        self.clear_errors()

#check name and requirements

        if not name:
            self.show_error("Please enter your name.", 150)
        elif not age:
            self.show_error("Please enter your age.", 350)
        elif not age.isdigit() or not (8<= int(age) <=13):
            self.show_error("Age must be between 7 and 12", 350)
        else:
            self.controller.show_frame(Page1)

    def clear_errors(self):
        for widget in self.winfo_children():
            if isinstance(widget, Label) and (widget.cget("fg") == "white" or "error" in widget.cget("text")):
                widget.destroy()
    
    def show_error(self, message, y):
        error_label = Label(self, text=message, fg="white", bg= "#80A9E1", font=("helvetica", 12))
        error_label.place(x=354, y=y)


#-------------------------# second window frame page1------------------------------------------#


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
        #option 3 is right
        option1=Radiobutton(self, value="one", font=("helvetica", 12), text="X", bg="#FF7C9F", fg="black")
        option1.place(x=295, y=426)
        option2=Radiobutton(self, value="two", font=("helvetica", 12), text="V", bg="#FF7C9F", fg="black")
        option2.place(x=572, y=426)
        option3=Radiobutton(self, value="three", font=("helvetica", 12), text="L", bg="#FF7C9F", fg="black")
        option3.place(x=300, y=300)
        option4=Radiobutton(self, value="four", font=("helvetica", 12), text="D", bg="#FF7C9F", fg="black")
        option4.place(x=570, y=300)

#next and quit button to show frame 3

        button2= Button (self, text="Next", bg="#43B262", activebackground="#A5C2E9", width=10, font=("Helvetica", 12, "bold"),
                        command = lambda : controller.show_frame(Page2))
        
        button2.place(x=730, y=440)
        button6= Button (self, text="Quit", bg="#A5C2E9", activebackground="#8E699D", width=10, font=("Helvetica", 12, "bold"),
                        command = quit)
        button6.place(x=80, y=440)



#---------------------------# third window frame page2----------------------------------------#


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
        #option 7 is right
        option5=Radiobutton(self, value="five", font=("helvetica", 12), text="1841", bg="#FF7C9F", fg="black")
        option5.place(x=295, y=426)
        option6=Radiobutton(self, value="six", font=("helvetica", 12), text="1213", bg="#FF7C9F", fg="black")
        option6.place(x=567, y=426)
        option7=Radiobutton(self, value="seven", font=("helvetica", 12), text="1432", bg="#FF7C9F", fg="black")
        option7.place(x=295, y=300)
        option8=Radiobutton(self, value="eight", font=("helvetica", 12), text="1410", bg="#FF7C9F", fg="black")
        option8.place(x=565, y=300)

#next button to show frame 4

        button3= Button (self, text="Next", bg="#43B262", activebackground="#A5C2E9", width=10, font=("Helvetica", 12, "bold"),
                        command = lambda : controller.show_frame(Page3))
        
        button3.place(x=730, y=440)
        button6= Button (self, text="Quit", bg="#A5C2E9", activebackground="#8E699D", width=10, font=("Helvetica", 12, "bold"),
                        command = quit)
        button6.place(x=80, y=440)


#---------------------# fourth window frame page3----------------------------------------------#


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
        #option 10 is right
        option9=Radiobutton(self, value="nine", font=("helvetica", 12), text="9.2", bg="#FF7C9F", fg="black")
        option9.place(x=295, y=426)
        option10=Radiobutton(self, value="ten", font=("helvetica", 12), text="0.92", bg="#FF7C9F", fg="black")
        option10.place(x=567, y=426)
        option11=Radiobutton(self, value="eleven", font=("helvetica", 12), text="00.92", bg="#FF7C9F", fg="black")
        option11.place(x=290, y=300)
        option12=Radiobutton(self, value="twelve", font=("helvetica", 12), text="000.92", bg="#FF7C9F", fg="black")
        option12.place(x=560, y=300)

#next button to show frame 5

        button4= Button (self, text="Next", bg="#43B262", activebackground="#A5C2E9", width=10, font=("Helvetica", 12, "bold"),
                        command = lambda : controller.show_frame(Page4))
        
        button4.place(x=730, y=440)
        button6= Button (self, text="Quit", bg="#A5C2E9", activebackground="#8E699D", width=10, font=("Helvetica", 12, "bold"),
                        command = quit)
        button6.place(x=80, y=440)

#----------------------# fifth window frame page4---------------------------------------------#


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
        #option 16 is right
        option13=Radiobutton(self, value="thirteen", font=("helvetica", 12), text="120", bg="#FF7C9F", fg="black")
        option13.place(x=295, y=426)
        option14=Radiobutton(self, value="fourteen", font=("helvetica", 12), text="240", bg="#FF7C9F", fg="black")
        option14.place(x=567, y=426)
        option15=Radiobutton(self, value="fifteen", font=("helvetica", 12), text="90", bg="#FF7C9F", fg="black")
        option15.place(x=295, y=300)
        option16=Radiobutton(self, value="sixteen", font=("helvetica", 12), text="180", bg="#FF7C9F", fg="black")
        option16.place(x=565, y=300)

#next button to show frame 5

        button5= Button (self, text="Next", bg="#43B262", activebackground="#A5C2E9", width=10, font=("Helvetica", 12, "bold"),
                        command = lambda : controller.show_frame(Page5))
        
        button5.place(x=730, y=440)
        button6= Button (self, text="Quit", bg="#A5C2E9", activebackground="#8E699D", width=10, font=("Helvetica", 12, "bold"),
                        command = quit)
        button6.place(x=80, y=440)
        
#----------------------# fifth window frame page4---------------------------------------------#


class Page5(tk.Frame):    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

#background image
        self.image5= PhotoImage(file="Screenshot (135).png")
        self.start_bg= Label(self, image=self.image5)
        self.start_bg.grid(row=0,column=0)

# Add a label to display the result
        self.result_label = Label(self, text="", font=("helvetica", 14))
        self.result_label.place(x=350, y=350)

# Add a buttons
        result_button = Button(self, text="Show Result", bg="#43B262", activebackground="#A5C2E9",
                               width=15, font=("Helvetica", 12, "bold"), command= self.show_result)
        result_button.place(x=720, y=440)
        button6= Button (self, text="Quit", bg="#A5C2E9", activebackground="#8E699D", width=10, font=("Helvetica", 12, "bold"),
                        command = quit)
        button6.place(x=80, y=440)


#question
        Label(self, width="27", text="What is 3/8 times three?", fg="white", bg= "black" , font=("helvetica", 14) ).place(x=298, y=165)

#options 
        #option 18 is right
        option17=Radiobutton(self, value="seventeen", font=("helvetica", 12), text="6/8", bg="#FF7C9F", fg="black")
        option17.place(x=295, y=426)
        option18=Radiobutton(self, value="eighteen", font=("helvetica", 12), text="9/8", bg="#FF7C9F", fg="black")
        option18.place(x=567, y=426)
        option19=Radiobutton(self, value="nineteen", font=("helvetica", 12), text="8/6", bg="#FF7C9F", fg="black")
        option19.place(x=295, y=300)
        option20=Radiobutton(self, value="twenty", font=("helvetica", 12), text="8/9", bg="#FF7C9F", fg="black")
        option20.place(x=565, y=300)

#initializing variables to store selected_answers

        self.option1= StringVar()
        self.option2= StringVar()
        self.option3= StringVar()
        self.option4= StringVar()
        self.option5= StringVar()
        self.option6= StringVar()
        self.option7= StringVar()
        self.option8= StringVar()
        self.option9= StringVar()
        self.option10= StringVar()
        self.option11= StringVar()
        self.option12= StringVar()
        self.option13= StringVar()
        self.option14= StringVar()
        self.option15= StringVar()
        self.option16= StringVar()
        self.option17= StringVar()
        self.option18= StringVar()
        self.option19= StringVar()
        self.option20= StringVar()




#command for showing result

    def show_result(self):
        correct_answers = self.count_correct_answers()
        total_questions = 5  # Total number of questions

# Create a new pop-up window for the result
        result_popup = Toplevel(self)
        result_popup.title("Quiz Result")
        result_popup.geometry("300x150")

        result_message = f"You scored {correct_answers}/{total_questions}"
        result_label = Label(result_popup, text=result_message, font=("helvetica", 16))
        result_label.pack(pady=20)

#count answers function
    def count_correct_answers(self):
        correct_answers=0
# Define the correct answers for each question
        correct_answers_list = ["three", "seven", "ten", "sixteen", "eighteen"]

# Access the selected answer for each question and compare with the correct answer        
        selected_answers= [
            self.option1.get(),
            self.option2.get(),
            self.option3.get(),
            self.option4.get(),
            self.option5.get(),
            self.option6.get(),
            self.option7.get(),
            self.option8.get(),
            self.option9.get(),
            self.option10.get(),
            self.option11.get(),
            self.option12.get(),
            self.option13.get(),
            self.option14.get(),
            self.option15.get(),
            self.option16.get(),
            self.option17.get(),
            self.option18.get(),
            self.option19.get(),
            self.option20.get(),


        ]

        for i in range(len(selected_answers)):
            if selected_answers[i] == correct_answers_list[i]:
                correct_answers += 1
    
        return correct_answers

# Driver Code
app = tkinterApp()
app.title("Shivani<3")
app.geometry("895x505")
app.mainloop()