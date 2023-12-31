import tkinter as tk
from tkinter import *
from tkinter.font import Font
import tkinter.font as font
import os #since import function is not working, I added 'os' module for launching a new window

# adding functions

def close():#another function to go to the home menu
    app.destroy()
    import home

def quit():  # quit window
    app.destroy()

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        self.selected_answers = ["", "", "", "", ""]  # an empty list for answers

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.score = 0  # initialize the scores

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2, Page3, Page4, Page5):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# --------------------------# first window frame (startpage)-----------------------------#


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    # adding widgets under a function
    def create_widgets(self):

        # background image
        self.image1 = PhotoImage(file="Screenshot (122).png")
        self.start_bg = Label(self, image=self.image1)
        self.start_bg.grid(row=0, column=0)

        # labels and entries
        Label(self, width="8", text="Name", fg="black", bg="#43B262", font=("helvetica", 14)).place(x=250, y=200)

        self.entry_name = Entry(self, width=18, font=("helvetica", 14), fg="#C63861")
        self.entry_name.place(x=350, y=200)

        Label(self, width="8", text="Age", fg="black", bg="#43B262", font=("helvetica", 14)).place(x=250, y=300)

        self.entry_age = Entry(self, width=18, font=("helvetica", 14), fg="#C63861")
        self.entry_age.place(x=350, y=300)

        # start and quit button
        self.button1 = Button(self, text="Start", bg="#FF7C9F", activebackground="#A5C2E9", width=10,
                              font=("Helvetica", 12, "bold"),
                              command=self.start_quiz)
        self.button1.place(x=610, y=245)

        self.button6 = Button(self, text="Quit", bg="#A5C2E9", activebackground="#8E699D", width=10,
                              font=("Helvetica", 12, "bold"),
                              command=quit)
        self.button6.place(x=720, y=458)
        self.button6 = Button(self, text="Home", bg="#A5C2E9", activebackground="#8E699D", width=10,
                              font=("Helvetica", 12, "bold"),
                              command=close)
        self.button6.place(x=720, y=458)

    # defining the start_quiz function

    def start_quiz(self):

        name = self.entry_name.get()
        age = self.entry_age.get()

        # clear previous error message
        self.clear_errors()

        # check name and requirements

        if not name:
            self.show_error("Please enter your name.", 150)
        elif not age:
            self.show_error("Please enter your age.", 350)
        elif not age.isdigit() or not (6 <= int(age) <= 13):
            self.show_error("Age must be between 7 and 12", 350)
        else:
            self.controller.show_frame(Page1)

    def clear_errors(self):
        for widget in self.winfo_children():
            if isinstance(widget, Label) and (widget.cget("fg") == "white" or "error" in widget.cget("text")):
                widget.destroy()

    def show_error(self, message, y):
        error_label = Label(self, text=message, fg="white", bg="#80A9E1", font=("helvetica", 12))
        error_label.place(x=354, y=y)

# -------------------------# second window frame page1------------------------------------------#


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background image
        self.image2 = PhotoImage(file="Screenshot (135).png")
        self.start_bg = Label(self, image=self.image2)
        self.start_bg.grid(row=0, column=0)

        # question
        Label(self, width="27", text="What is the roman numeral for 50?", fg="white", bg="black",
              font=("helvetica", 14)).place(x=298, y=165)

        # declare variable to store the answers
        self.option_var1 = tk.StringVar()

        # options
        # option 1 is right
        option1 = Radiobutton(self, variable=self.option_var1, value="one", font=("helvetica", 12), text="X",
                              bg="#FF7C9F", fg="black")
        option1.place(x=295, y=426)
        option2 = Radiobutton(self, variable=self.option_var1, value="two", font=("helvetica", 12), text="L",
                              bg="#FF7C9F", fg="black")
        option2.place(x=572, y=426)
        option3 = Radiobutton(self, variable=self.option_var1, value="three", font=("helvetica", 12), text="V",
                              bg="#FF7C9F", fg="black")
        option3.place(x=300, y=300)
        option4 = Radiobutton(self, variable=self.option_var1, value="four", font=("helvetica", 12), text="D",
                              bg="#FF7C9F", fg="black")
        option4.place(x=570, y=300)

        # next and quit button to show frame 
        # next and quit button to show frame 3
        button2 = Button(self, text="Next", bg="#FFBE17", activebackground="#A5C2E9", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=lambda: controller.show_frame(Page2))

        button2.place(x=730, y=440)
        button6 = Button(self, text="Quit", bg="#FFBE17", activebackground="#8E699D", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=quit)
        button6.place(x=80, y=440)
        home_button1= Button(self, text="Home", bg="#FFBE17", activebackground="#F8ED69", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=close)
        home_button1.place(x=80, y=390)

        # Function to store the selected answer
        def save_answer():
            controller.selected_answers[0] = self.option_var1.get()

        # Save the selected answer when the radio button changes
        self.option_var1.trace_add("write", lambda *args: save_answer())

# ---------------------------# third window frame page2----------------------------------------#


class Page2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background image
        self.image3 = PhotoImage(file="Screenshot (135).png")
        self.start_bg = Label(self, image=self.image3)
        self.start_bg.grid(row=0, column=0)

        # question
        Label(self, width="27", text="What is 2864 divided by 2?", fg="white", bg="black",
              font=("helvetica", 14)).place(x=298, y=165)

        # declare variable to store the answers
        self.option_var2 = tk.StringVar()

        # options
        # option 3 is right
        option1 = Radiobutton(self, variable=self.option_var2, value="one", font=("helvetica", 12), text="1841",
                              bg="#FF7C9F", fg="black")
        option1.place(x=295, y=426)
        option2 = Radiobutton(self, variable=self.option_var2, value="two", font=("helvetica", 12), text="1213",
                              bg="#FF7C9F", fg="black")
        option2.place(x=567, y=426)
        option3 = Radiobutton(self, variable=self.option_var2, value="three", font=("helvetica", 12), text="1432",
                              bg="#FF7C9F", fg="black")
        option3.place(x=295, y=300)
        option4 = Radiobutton(self, variable=self.option_var2, value="four", font=("helvetica", 12), text="1410",
                              bg="#FF7C9F", fg="black")
        option4.place(x=565, y=300)

        # next button to show frame 4
        button3 = Button(self, text="Next", bg="#FFBE17", activebackground="#A5C2E9", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=lambda: controller.show_frame(Page3))

        button3.place(x=730, y=440)
        button6 = Button(self, text="Quit", bg="#FFBE17", activebackground="#8E699D", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=quit)
        button6.place(x=80, y=440)
        home_button1= Button(self, text="Home", bg="#FFBE17", activebackground="#F8ED69", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=close)
        home_button1.place(x=80, y=390)

        # Function to store the selected answer
        def save_answer():
            controller.selected_answers[1] = self.option_var2.get()

        # Save the selected answer when the radio button changes
        self.option_var2.trace_add("write", lambda *args: save_answer())

# ---------------------# fourth window frame page3----------------------------------------------#


class Page3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background image
        self.image4 = PhotoImage(file="Screenshot (135).png")
        self.start_bg = Label(self, image=self.image4)
        self.start_bg.grid(row=0, column=0)

        # question
        Label(self, width="27", text="What is 92/100 as decimals?", fg="white", bg="black",
              font=("helvetica", 14)).place(x=298, y=165)

        # declare variable to store the answers
        self.option_var3 = tk.StringVar()

        # options
        # option 2 is right
        option1 = Radiobutton(self, variable=self.option_var3, value="one", font=("helvetica", 12), text="9.2",
                              bg="#FF7C9F", fg="black")
        option1.place(x=295, y=426)
        option2 = Radiobutton(self, variable=self.option_var3, value="two", font=("helvetica", 12), text="0.92",
                              bg="#FF7C9F", fg="black")
        option2.place(x=567, y=426)
        option3 = Radiobutton(self, variable=self.option_var3, value="three", font=("helvetica", 12), text="00.92",
                              bg="#FF7C9F", fg="black")
        option3.place(x=290, y=300)
        option4 = Radiobutton(self, variable=self.option_var3, value="four", font=("helvetica", 12), text="000.92",
                              bg="#FF7C9F", fg="black")
        option4.place(x=560, y=300)

        # next button to show frame 5
        button4 = Button(self, text="Next", bg="#FFBE17", activebackground="#A5C2E9", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=lambda: controller.show_frame(Page4))

        button4.place(x=730, y=440)
        button6 = Button(self, text="Quit", bg="#FFBE17", activebackground="#8E699D", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=quit)
        button6.place(x=80, y=440)
        home_button1= Button(self, text="Home", bg="#FFBE17", activebackground="#F8ED69", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=close)
        home_button1.place(x=80, y=390)

        # Function to store the selected answer
        def save_answer():
            controller.selected_answers[2] = self.option_var3.get()

        # Save the selected answer when the radio button changes
        self.option_var3.trace_add("write", lambda *args: save_answer())

# ----------------------# fifth window frame page4---------------------------------------------#


class Page4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background image
        self.image5 = PhotoImage(file="Screenshot (135).png")
        self.start_bg = Label(self, image=self.image5)
        self.start_bg.grid(row=0, column=0)

        # question
        Label(self, width="27", text="How many minutes in 3 hours?", fg="white", bg="black",
              font=("helvetica", 14)).place(x=298, y=165)

        # declare variable to store the answers
        self.option_var4 = tk.StringVar()

        # options
        # option 4 is
        option1 = Radiobutton(self, variable=self.option_var4, value="one", font=("helvetica", 12), text="120",
                              bg="#FF7C9F", fg="black")
        option1.place(x=295, y=426)
        option2 = Radiobutton(self, variable=self.option_var4, value="two", font=("helvetica", 12), text="240",
                              bg="#FF7C9F", fg="black")
        option2.place(x=567, y=426)
        option3 = Radiobutton(self, variable=self.option_var4, value="three", font=("helvetica", 12), text="90",
                              bg="#FF7C9F", fg="black")
        option3.place(x=295, y=300)
        option4 = Radiobutton(self, variable=self.option_var4, value="four", font=("helvetica", 12), text="180",
                              bg="#FF7C9F", fg="black")
        option4.place(x=565, y=300)

        # next button to show frame 5
        button5 = Button(self, text="Next", bg="#FFBE17", activebackground="#A5C2E9", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=lambda: controller.show_frame(Page5))

        button5.place(x=730, y=440)
        button6 = Button(self, text="Quit", bg="#FFBE17", activebackground="#8E699D", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=quit)
        button6.place(x=80, y=440)
        home_button1= Button(self, text="Home", bg="#FFBE17", activebackground="#F8ED69", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=close)
        home_button1.place(x=80, y=390)

        # Function to store the selected answer
        def save_answer():
            controller.selected_answers[3] = self.option_var4.get()

        # Save the selected answer when the radio button changes
        self.option_var4.trace_add("write", lambda *args: save_answer())

# ----------------------# fifth window frame page4---------------------------------------------#


class Page5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # background image
        self.image5 = PhotoImage(file="Screenshot (135).png")
        self.start_bg = Label(self, image=self.image5)
        self.start_bg.grid(row=0, column=0)

        # question
        Label(self, width="27", text="What is 3/8 times three?", fg="white", bg="black",
              font=("helvetica", 14)).place(x=298, y=165)

        # declare variable to store the answers
        self.option_var5 = tk.StringVar()

        # options
        # option 2 is right
        option1 = Radiobutton(self, variable=self.option_var5, value="one", font=("helvetica", 12), text="6/8",
                              bg="#FF7C9F", fg="black")
        option1.place(x=295, y=426)
        option2 = Radiobutton(self, variable=self.option_var5, value="two", font=("helvetica", 12), text="9/8",
                              bg="#FF7C9F", fg="black")
        option2.place(x=567, y=426)
        option3 = Radiobutton(self, variable=self.option_var5, value="three", font=("helvetica", 12), text="8/6",
                              bg="#FF7C9F", fg="black")
        option3.place(x=295, y=300)
        option4 = Radiobutton(self, variable=self.option_var5, value="four", font=("helvetica", 12), text="8/9",
                              bg="#FF7C9F", fg="black")
        option4.place(x=565, y=300)

        # submit button to calculate and display the score
        submit_button = Button(self, text="Submit", bg="#FFBE17", activebackground="#A5C2E9", width=10,
                               font=("Helvetica", 12, "bold"),
                               command=self.calculate_and_display_score)

        submit_button.place(x=730, y=440)
        button6 = Button(self, text="Quit", bg="#FFBE17", activebackground="#8E699D", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=quit)
        button6.place(x=80, y=440)
        home_button1= Button(self, text="Home", bg="#FFBE17", activebackground="#F8ED69", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=close)
        home_button1.place(x=80, y=390)

        # Function to store the selected answer
        def save_answer():
            controller.selected_answers[4] = self.option_var5.get()

        # Save the selected answer when the radio button changes
        self.option_var5.trace_add("write", lambda *args: save_answer())

    # Function to calculate and display the score
    def calculate_and_display_score(self):
        total_questions = 5  # Total number of questions

        # Initialize a variable to store the user's score
        user_score = 0

        # Define the correct answers for each question
        correct_answers_list = ["two", "three", "two", "four", "two"]

        for i in range(len(self.controller.selected_answers)):
            if self.controller.selected_answers[i] == correct_answers_list[i]:
                user_score += 1

        # Update the score variable in the tkinter class
        self.controller.score = user_score

        # Display the score in a popup window
        result_popup = Toplevel(self)
        result_popup.title("Shivi :)")
        result_popup.geometry("400x200")

        result_message = f"You scored {user_score}/{total_questions}"
        result_label = Label(result_popup, text=result_message, font=("helvetica", 16))
        result_label.pack(pady=20)
        result_label.configure(bg="#FFF3E4", fg= "black")
        result_popup.config(bg="#FF7C9F")

        home_button= Button(result_popup, text="Home", bg="#66EFC9", activebackground="#EFB8FF", width=10,
                            font=("Helvetica", 11, "bold"), command=self.home)
        home_button.place(x="150", y="80")
        quit_button= Button(result_popup, text="Quit", bg="#66EFC9", activebackground="#EFB8FF", width=10,
                            font=("Helvetica", 11, "bold"), command=self.home)
        quit_button.place(x="150", y="130")
        home_button1= Button(self, text="Home", bg="#FFBE17", activebackground="#F8ED69", width=10,
                         font=("Helvetica", 12, "bold"),
                         command=close)
        home_button1.place(x=80, y=390)

    def home(self): #function to go to home
#destroy the current windows
        self.winfo_toplevel().destroy()
        import home


# Driver Code
app = tkinterApp()
app.title("Shivani<3")
app.geometry("895x505")
app.mainloop()
