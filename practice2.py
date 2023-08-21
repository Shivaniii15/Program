
from itertools import count
from tkinter import *
from tkinter import ttk
import random
from tkinter.font import Font
import csv
from csv import reader
from Data import *


# Creating a class for all the interface widgets


class Interface:
    def __init__(self, parent):
        # Declaring Global variable
        global count, rank
        count = 0
        rank = 1
        # Creating a font-style for label text
        self.fontLabel = Font(
            family="Comic Sans MS",
            size=16,
            weight="normal",
            slant="roman",
            underline=0,
            overstrike=0)

        ###
        # Layout for the first page(*START FRAME)
        self.firstFrame = Frame(parent, bg="white")
        self.firstFrame.grid(row=0, column=0)
        self.image1 = PhotoImage(file="firstBackground.png")
        self.start_bg = Label(self.firstFrame, image=self.image1)
        self.start_bg.grid(row=1, column=1)
        self.start_btn = Button(
            self.firstFrame, text="Start", bg="#E69138", activebackground="#696662", width=10, font=("Helvetica", 20, "bold"), command=self.start_btn)
        self.start_btn.place(relx=0.75, rely=0.5, anchor=CENTER)

        ###
        # Creating a frame for NAME FRAME
        self.secondFrame = Frame(parent, bg="white")
        self.secondFrame.grid(row=0, column=0, rowspan=5, columnspan=6)
        self.image2 = PhotoImage(file="headingBackground.png")
        self.heading_bg = Label(self.secondFrame, image=self.image2)
        self.heading_bg.grid(row=0, column=0, columnspan=6, sticky=W)
        self.heading_bg.grid_propagate(1)

        #-------------------------till here-------------------------#

        # Layout for the LEFT part of the NAME FRAME
        self.leftFrame = Frame(self.secondFrame, bg="white")
        self.leftFrame.grid(row=1, column=1, rowspan=5, padx=0)
        self.name_label = Label(
            self.leftFrame, text="    User name: ", bg="white", font=self.fontLabel)
        self.name_label.grid(row=2, column=1, pady=10)
        self.age_label = Label(
            self.leftFrame, text="    Age: ", bg="white",  font=self.fontLabel)
        self.age_label.grid(row=3, column=1, pady=20)
        self.name_entry = Entry(self.leftFrame,  font=(
            "Slab Serif", 14, ""), width=18, bg="#F9CB9C")
        self.name_entry.grid(row=2, column=2, padx=0, pady=0)
        self.age_entry = Entry(self.leftFrame,  font=(
            "Slab Serif", 14, ""), width=18,  bg="#F9CB9C")
        self.age_entry.grid(row=3, column=2, pady=0)
        self.space_label_left = Label(
            self.leftFrame, text="", bg="white", fg="white", font=("", 10, "bold"))
        self.space_label_left.grid(row=4, column=2, pady=2)
        # Layout for the RIGHT part of the NAME FRAME
        self.rightFrame = Frame(
            self.secondFrame, bg="#ffadad", height=500, width=500)
        self.rightFrame.grid(row=2, column=2, padx=30)
        self.question_label = Label(
            self.rightFrame, font=self.fontLabel, text="What problem would you like to solve?", bg="#ffadad")
        self.question_label.grid(
            row=1, column=1, ipady=10, pady=15, ipadx=20, padx=5)
        # Adding radiobutton of choices for users to choose
        self.v = StringVar()
        self.v.set(0)
        self.area_rb = Radiobutton(self.rightFrame, variable=self.v, value="one", font=self.fontLabel,
                                   text="Area", bg="#ffadad")
        self.surface_rb = Radiobutton(self.rightFrame, variable=self.v, value="two", font=self.fontLabel,  bg="#ffadad",
                                      text="Surface Area")
        self.volume_rb = Radiobutton(self.rightFrame, variable=self.v, value="three", font=self.fontLabel,
                                     text="Volume", bg="#ffadad")
        self.area_rb.grid(row=3, column=1, ipady=10,
                          pady=10, sticky=W, padx=60)
        self.surface_rb.grid(row=4, column=1, ipady=10,
                             pady=10, sticky=W, padx=60)
        self.volume_rb.grid(row=5, column=1, ipady=10,
                            pady=10, sticky=W, padx=60)
        self.next_btn_name = Button(
            self.rightFrame, text="Next", bg="#E69138", activebackground="#696662", width=8, font=("Helvetica", 14, "bold"), command=self.next_btn_name)
        self.next_btn_name.grid(row=6, column=1, padx=60, pady=10, sticky=NW)
        self.space_label = Label(self.rightFrame, text="", font=(
            "Helvetica", 16, ""),  bg="#ffadad")
        self.space_label.grid(row=7, column=1, padx=60, pady=10, sticky=NW)

        ###
        # Creating a frame for PROBLEM FRAME
        self.thirdFrame = Frame(parent, bg="white")
        self.thirdFrame.grid(row=1, column=0, rowspan=5, columnspan=6)
        self.heading_bg3 = Label(self.thirdFrame, image=self.image2)
        self.heading_bg3.grid(row=0, column=0, columnspan=6, sticky=W)
        # Layout for LEFT side of PROBLEM FRAME
        self.leftFrame_2 = Frame(
            self.thirdFrame, bg="white")
        self.leftFrame_2.grid(row=1, column=1, rowspan=5, padx=0)
        self.your_score_label = Label(
            self.leftFrame_2, text="Your Score: ", font=self.fontLabel, bg="#e69138")
        self.your_score_label.grid(row=3, column=1, padx=0, pady=0)
        self.score_label = Label(
            self.leftFrame_2, text="", bd=0, bg="white", font=("Helvetica", 15, "bold"))
        self.score_label.grid(row=3, column=2, padx=0, pady=0)
        self.finish_btn = Button(
            self.leftFrame_2, text="Finish", bg="#E69138", state=DISABLED, activebackground="#696662",   width=8, font=("Helvetica", 14, "bold"), command=self.finish)
        self.finish_btn.grid(row=3, column=3, padx=5, pady=0)
        # Layout for RIGHT side of PROBLEM FRAME
        self.rightFrame_2 = Frame(
            self.thirdFrame, bg="#ffadad", height=500, width=500)
        self.rightFrame_2.grid(row=2, column=2, padx=30)
        # RIGHT_PROBLEM FRAME: adding variable
        self.a_variable = Label(self.rightFrame_2, text="",
                                font=self.fontLabel, bg="#ffadad")
        self.a_variable.grid(row=3, column=0, rowspan=2,
                             columnspan=2, ipady=20, pady=7, padx=5)
        self.q_label = Label(
            self.rightFrame_2, text="", font=self.fontLabel, bg="#ffadad")
        self.q_label.grid(row=5, column=0, columnspan=2,
                          padx=20, pady=5, ipady=5)
        self.answer_entry = Entry(self.rightFrame_2, font=(
            "Helvetica", 14, ""), width=15, bg="#F9CB9C")
        self.answer_entry.grid(row=6, column=0, padx=20, pady=5)
        # LEFT_PROBLEM FRAME: image holder
        self.image_Area = []
        self.image_Surface = []
        self.image_Volume = []
        # LEFT_PROBLEM FRAME: Area image
        self.image_Area.append(PhotoImage(file="rectangleArea.png"))
        self.image_Area.append(PhotoImage(file="triangleArea.png"))
        self.image_Area.append(PhotoImage(file="trepeziumArea.png"))
        self.target_Area = 0
        # LEFT_PROBLEM FRAME: Surface image
        self.image_Surface.append(PhotoImage(file="surfaceCube.png"))
        self.image_Surface.append(PhotoImage(file="surfaceSphere.png"))
        self.image_Surface.append(PhotoImage(file="surfaceCylinder.png"))
        self.target_Surface = 0
        # LEFT_PROBLEM FRAME: Volume image
        self.image_Volume.append(PhotoImage(file="rectangleVolume.png"))
        self.image_Volume.append(PhotoImage(file="coneVolume.png"))
        self.image_Volume.append(PhotoImage(file="sphereVolume.png"))
        self.target_Volume = 0
        self.score_add = 0
        # RIGHT_PROBLEM FRAME: positon buttons
        self.photo = Label(
            self.leftFrame_2, image=self.image_Area[2], bg="white")
        self.photo.grid(
            row=2, column=1, columnspan=3, padx=3, pady=30)
        self.result_label = Label(self.rightFrame_2, text="", fg="white", font=(
            "", 12, "bold"), bg="#ffadad")
        self.result_label.grid(row=7, column=0, padx=25, pady=10, sticky=NW)
        self.check_btn = Button(
            self.rightFrame_2, text="Check",  bg="#E69138", activebackground="#696662",   width=8, font=("Helvetica", 14, "bold"), command=self.check)
        self.check_btn.grid(row=6, column=1, padx=25, pady=7, sticky=NW)
        self.next_btn_problem = Button(
            self.rightFrame_2, text="Next",  bg="#E69138", activebackground="#696662",   width=8, font=("Helvetica", 14, "bold"), command=self.next_problem)
        self.next_btn_problem.grid(row=7, column=1, padx=25, pady=7, sticky=NW)
        self.retry_btn = Button(
            self.rightFrame_2, text="Retry",  bg="#E69138", activebackground="#696662",   width=8, font=("Helvetica", 14, "bold"), command=self.change_number)
        self.retry_btn.grid(row=8, column=0, padx=20, pady=30, sticky=NW)
        self.restart_btn = Button(
            self.rightFrame_2, text="Restart",  bg="#E69138", activebackground="#696662",   width=8, font=("Helvetica", 14, "bold"), command=self.restart_problem)
        self.restart_btn.grid(row=8, column=1, padx=25, pady=30, sticky=NW)

        ##
        # Creating a frame for RESTART FRAME
        self.forthFrame = Frame(parent, bg="white")
        self.forthFrame.grid(row=0, column=0, columnspan=6)
        self.heading_bg4 = Label(self.forthFrame, image=self.image2)
        self.heading_bg4.grid(row=0, column=0, columnspan=6, sticky=W)
        self.middleFrame = Frame(self.forthFrame, bg="white")
        self.middleFrame.grid(row=3, column=0)
        self.question_label = Label(
            self.middleFrame, font=self.fontLabel, text="What problem would you like to solve?", bg="white")
        self.question_label.grid(
            row=1, column=1, ipady=10, pady=10, ipadx=20, padx=20)
        # Adding radio button choices for users to choose
        self.v1 = StringVar()
        self.v1.set(0)
        self.area_rb = Radiobutton(self.middleFrame, variable=self.v1, value="one", font=self.fontLabel,
                                   text="Area", bg="white")
        self.surface_rb = Radiobutton(self.middleFrame, variable=self.v1, value="two", font=self.fontLabel,  bg="white",
                                      text="Surface Area")
        self.volume_rb = Radiobutton(self.middleFrame, variable=self.v1, value="three", font=self.fontLabel,
                                     text="Volume", bg="white")
        self.area_rb.grid(row=3, column=1, ipady=7,
                          pady=10, sticky=W, padx=60)
        self.surface_rb.grid(row=4, column=1, ipady=7,
                             pady=10, sticky=W, padx=60)
        self.volume_rb.grid(row=5, column=1, ipady=7,
                            pady=10, sticky=W, padx=60)
        self.rb_error = Label(self.middleFrame, text="", bg="white",
                              fg="white", font=("", 10, "bold"))
        self.rb_error.grid(row=6, column=1, padx=60, pady=7)
        self.next_btn_restart = Button(
            self.middleFrame, text="Next", bg="#E69138", activebackground="#696662",   width=8, font=("Helvetica", 14, "bold"), command=self.restart_to_problem)
        self.next_btn_restart.grid(
            row=7, column=1, padx=60, pady=10, sticky=NW)
        self.space = Label(self.middleFrame, text="", bg="white")
        self.space.grid(row=8, column=1)

        ###
        # Creating a frame for scoreboard page
        self.fifthFrame = Frame(parent, bg="white")
        self.fifthFrame.grid(row=0, column=0, columnspan=6)
        self.heading_bg5 = Label(self.fifthFrame, image=self.image2)
        self.heading_bg5.grid(row=0, column=0, columnspan=6, sticky=W)
        self.score_board_label = Label(
            self.fifthFrame, text="Score Board", fg="#FF8C00", font=("Helvetica", 20, "bold"), bg="white")
        self.score_board_label.grid(
            row=1, column=1, padx=25, pady=20, sticky=W)
        self.quit_btn = Button(
            self.fifthFrame, text="Quit",  bg="#E69138", activebackground="#696662",   width=7, font=("Helvetica", 14, "bold"), command=self.quit)
        self.quit_btn.grid(row=7, column=4, padx=25, pady=0, sticky=E)
        self.new_game_btn = Button(
            self.fifthFrame, text="New Game",  bg="#E69138", activebackground="#696662",   width=12, font=("Helvetica", 14, "bold"), command=self.new_game)
        self.new_game_btn.grid(row=6, column=4, padx=25, pady=0, sticky=E)
        self.space_label = Label(
            self.fifthFrame, text="", bg="white", fg="white", font=("", 10, "bold"))
        self.space_label.grid(row=10, column=2, pady=2)
        # Creating a treeview table to store users infomation(i.e score, name, rank)
        self.my_tree = ttk.Treeview(self.fifthFrame)
        self.my_tree.grid(row=2, column=1, rowspan=8, columnspan=4,
                          padx=25, pady=15, sticky=W)
        # Define the column
        self.my_tree['columns'] = ('Rank', 'User', 'Score')
        # Formate columns
        self.my_tree.column('#0', width=0, minwidth=0)
        self.my_tree.column('Rank', anchor=CENTER, width=100)
        self.my_tree.column('User', anchor=CENTER, width=180)
        self.my_tree.column('Score', anchor=CENTER, width=140)
        # Create Heading
        self.my_tree.heading('#0', text="")
        self.my_tree.heading('Rank', text="Rank", anchor=CENTER)
        self.my_tree.heading('User', text="User Name", anchor=CENTER)
        self.my_tree.heading('Score', text="Score", anchor=CENTER)
        # Adding colour to the treeview
        style = ttk.Style()
        style.configure("Treeview",
                        background="#FFF0F5",
                        forground="black",
                        rowheight=25,
                        filedbackgrkound=" #F9EDEB")
        style.map("Treeview",
                  background=[("selected", "#66a3ff")])

        # Change button colour when hover
        self.changeOnHover(self.start_btn, "Black", "#E69138")
        self.changeOnHover(self.restart_btn, "Black", "#E69138")
        self.changeOnHover(self.new_game_btn, "Black", "#E69138")
        self.changeOnHover(self.next_btn_name, "Black", "#E69138")
        self.changeOnHover(self.next_btn_problem, "Black", "#E69138")
        self.changeOnHover(self.check_btn, "Black", "#E69138")
        self.changeOnHover(self.finish_btn, "Black", "#E69138")
        self.changeOnHover(self.retry_btn, "Black", "#E69138")
        self.changeOnHover(self.quit_btn, "Black", "#E69138")

        for frame in (self.firstFrame, self.secondFrame, self.thirdFrame, self.forthFrame, self.fifthFrame):
            frame.grid(row=0, column=1, sticky='news')

        self.start_btn.bind("<start_btn>", self.raise_frame(
            self.firstFrame), self.hide_frame(self.secondFrame))

    # Function for showing and hiding frame
    def raise_frame(self, frame):
        frame.tkraise()

    def hide_frame(self, frame):
        frame.grid_forget()

    def show_frame(self, frame):
        frame.grid()

    # Fuction to move from Start frame to Name frame
    def start_btn(self):
        self.show_frame(self.secondFrame)
        self.hide_frame(self.firstFrame)
        self.hide_frame(self.thirdFrame)
        self.hide_frame(self.forthFrame)
        self.hide_frame(self.fifthFrame)

    # Fuction to check user input
    def next_btn_name(self):
        self.n = Name(self.name_entry.get(),
                      self.age_entry.get(), self.v.get())
        if self.n.check_blank():
            self.space_label_left.configure(
                bg="#fc253e", fg="white", text="Please enter 'Username' and 'Age'")
        elif self.n.check_name_blank():
            self.space_label_left.configure(
                bg="#fc253e", fg="white", text="Please enter 'Username'")
        elif self.n.check_name_same():
            self.space_label_left.configure(
                bg="#fc253e", fg="white", text="This Username already exist" + "\n"+"Please choose a different one")
        elif self.n.check_age_blank():
            self.space_label_left.configure(
                bg="#fc253e", fg="white", text="Please enter 'Age'")
        elif self.n.check_age_int():
            self.space_label_left.configure(
                bg="#fc253e", fg="white", text="Please enter 'Age' in number")
        elif self.n.check_age_under():
            self.space_label_left.configure(
                bg="#fc253e", fg="white", text="You are under the age limit." + "\n"+"Age limit is between 10-19")
        elif self.n.check_age_above():
            self.space_label_left.configure(
                bg="#fc253e", fg="white", text="You are above the age limit." + "\n"+"Age limit is between 10-19")
        elif self.n.check_rbn_blank():
            self.space_label_left.configure(
                bg="#fc253e", fg="white", text="Please choose one option "+"\n"+"from the radio button.")
        else:
            self.next_btn_to_problem()

    # Fuction to move from NAME FRAME to PROBLEM FRAME
    def next_btn_to_problem(self):
        self.hide_frame(self.firstFrame)
        self.hide_frame(self.secondFrame)
        self.hide_frame(self.forthFrame)
        self.hide_frame(self.fifthFrame)
        self.show_frame(self.thirdFrame)
        self.m = Image(self.v.get(), self.v1.get(), self.target_Area,
                       self.target_Surface, self.target_Volume)
        if self.m.area_rb():
            self.photo.config(image=self.image_Area[0], bg="white")
            self.change_number()

        elif self.m.surface_rb():
            self.photo.config(
                image=self.image_Surface[0], bd=0, bg="white")
            self.change_number()

        elif self.m.volume_rb():
            self.photo.config(image=self.image_Volume[0], bd=0, bg="white")
            self.change_number()

    # Fuction to move from RETRY FRAME to PROBLEM FRAME
    def restart_to_problem(self):
        if self.v1.get() == "0":
            self.rb_error.configure(
                bg="#fc253e", fg="white", text="Please choose one option from above.")
        else:
            self.next_btn_to_problem()
            self.rb_error.configure(
                bg="white", fg="white", text="")

    # Fuction for next button on PROBLEM FRAME

    def next_problem(self):
        if self.m.area_rb():
            self.target_Area -= 1
            if self.target_Area < 0:
                self.target_Area = len(self.image_Area) - 1
            self.photo.configure(
                image=self.image_Area[self.target_Area])
            self.change_number()

        if self.m.surface_rb():
            self.target_Surface -= 1
            if self.target_Surface < 0:
                self.target_Surface = len(self.image_Surface) - 1
            self.photo.configure(
                image=self.image_Surface[self.target_Surface])
            self.change_number()

        if self.m.volume_rb():
            self.target_Volume -= 1
            if self.target_Volume < 0:
                self.target_Volume = len(self.image_Volume) - 1
            self.photo.configure(
                image=self.image_Volume[self.target_Volume])
            self.change_number()

    # Fuction to change variable value
    def change_number(self):
        self.x = random.randint(2, 10)
        self.y = random.randint(2, 30)
        self.z = random.randint(2, 10)
        self.answer_entry.delete(0, END)
        self.result_label.configure(text="", bg="#ffadad")
        if self.v.get() == "one" or self.v1.get() == "one":
            self.q_label.config(text=f"Calculate the area of this shape.")
            if self.target_Area == 0:
                for i in range(1, 10):
                    self.a_variable.config(
                        text=f"If h = {self.x}" + "\n" + "\n" + f"If b = {self.y}")
            elif self.target_Area == 1:
                for i in range(1, 10):
                    self.a_variable.config(
                        text=f"If h = {self.x} " + "\n" + "\n" + f"If b = {self.y}")
            elif self.target_Area == 2:
                for i in range(1, 10):
                    self.a_variable.config(
                        text=f"If h = {self.x}        If b = {self.y}" + "\n" + "\n" + f"If a = {self.z}")
        elif self.v.get() == "two" or self.v1.get() == "two":
            self.q_label.config(text=f"Calculate the surface area")
            if self.target_Surface == 0:
                for i in range(1, 10):
                    self.a_variable.config(
                        text=f"If b = {self.y}" + "\n" + "\n")
            elif self.target_Surface == 1:
                for i in range(1, 10):
                    self.a_variable.config(
                        text=f"If r = {self.x}" + "\n" + "\n" + f"If pi = 3.14")
            elif self.target_Surface == 2:
                for i in range(1, 10):
                    self.a_variable.config(
                        text=f" If h = {self.y}     If pi = 3.14" + "\n" + "\n" + f"If r = {self.x}")
        elif self.v.get() == "three" or self.v1.get() == "three":
            self.q_label.config(text=f"Calculate the volume of this shape")
            if self.target_Volume == 0:
                for i in range(1, 10):
                    self.a_variable.config(
                        text=f"If h = {self.z}       If b = {self.y}" + "\n" + "\n" + f"If a = {self.x}")
            elif self.target_Volume == 1:
                for i in range(1, 10):
                    self.a_variable.config(
                        text=f"If h = {self.y}      If r = {self.x}" + "\n" + "\n" + f"If pi = 3.14")
            elif self.target_Volume == 2:
                for i in range(1, 10):
                    self.a_variable.config(
                        text=f" If r = {self.x}" + "\n" + "\n" + f"If pi =3.14")

    # Fuction to move from PROBLEM FRAME to RESTART FRAME
    def restart_problem(self):
        self.v.set('0')
        self.v1.set('0')
        self.hide_frame(self.firstFrame)
        self.hide_frame(self.secondFrame)
        self.hide_frame(self.thirdFrame)
        self.hide_frame(self.fifthFrame)
        self.show_frame(self.forthFrame)

    # Fuction to check user answer
    def check(self):
        self.s = Score(self.x, self.y, self.z, self.v.get(), self.v1.get(), self.target_Area,
                       self.target_Surface, self.target_Volume)
        try:
            self.f = float(self.answer_entry.get())
            if self.s.check_answer(self.f):
                self.score_add = self.score_add + 10
                self.result_label.configure(
                    text="You are correct!", font=(
                        "", 12, "bold"), bg="#f5d12d")
                self.your_score_label.configure(
                    text=f"Your score:   {self.score_add}", bg="#e69138")
                self.answer_entry.delete(0, END)
                self.change_number_correct()
                self.finish_btn["state"] = NORMAL
            else:
                self.result_label.configure(
                    text="Incorrect Answer", font=(
                        "", 12, "bold"), bg="#fc253e")
        except ValueError:
            self.result_label.config(
                text="Please answer "+"\n"+"in numbers.", font=(
                    "", 10, "bold"), bg="#fc253e")

    # The numbers will change when the user get the answer wrong
    def change_number_correct(self):
        self.change_number()
        self.result_label.configure(
            text="You are correct!", bg="#f5d12d")

    '''Finish button's fuction:
    1. Move form PROBLEM FRAME to SCOREBOARD FRAME
    2. Get NAME input from user and their SCORE, write it to a CSV FILE
    3. Sort the user's score from highest to lowest to list
    4. Save the sorted list to the CSV FILE
    5. Get value from the CSV FILE to TREEVIEW WIDGET'''

    def finish(self):
        # 1. Move form PROBLEM FRAME to SCOREBOARD FRAME
        self.show_frame(self.fifthFrame)
        self.hide_frame(self.thirdFrame)
        self.hide_frame(self.secondFrame)
        self.hide_frame(self.forthFrame)

        global count, rank
        # 2. Get NAME input from user and their SCORE, write it to a CSV FILE
        with open('mycsv.csv', 'a', newline='') as f:
            write = csv.writer(f)
            name = self.name_entry.get()
            score = self.score_add
            write.writerow([score, name])
        # 3. Sort the user's score from highest to lowest to list
        with open('mycsv.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            for row in csv_reader:
                name_list = list(csv_reader)
                name_list.sort(reverse=True)
        # 4. Save the sorted list to the CSV FILE
        with open('myRecord.csv', 'w') as outcsv:
            # configure writer to write standard csv file
            writer = csv.writer(outcsv, delimiter=',', quotechar='|',
                                quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(['Score', 'Name'])
            for item in name_list:
                # Write item to outcsv
                writer.writerow([item[0], item[1]])
        # 5. Get value from the CSV FILE to TREEVIEW WIDGET
        with open('myRecord.csv', 'r') as file:
            next(file)
            rr = csv.reader(file)
            for line in rr:
                self.my_tree.insert(parent='', index='end', iid=count, text="",
                                    values=(rank, line[1], line[0]))
                count += 1
                rank += 1

    # Fuction for New Game button in SCOREBOARD FRAME
    def new_game(self):
        self.hide_frame(self.fifthFrame)
        self.hide_frame(self.thirdFrame)
        self.hide_frame(self.forthFrame)
        self.hide_frame(self.secondFrame)
        self.show_frame(self.firstFrame)
        self.name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.answer_entry.delete(0, END)
        self.space_label_left.configure(text="", bg="white")
        self.score_add = 0
        self.finish_btn["state"] = DISABLED
        self.your_score_label.configure(text="Your score: ")
        self.v.set('0')
        self.v1.set('0')
        global rank, count
        count = 0
        rank = 1
        n_g = self.my_tree.get_children()
        if n_g != '()':
            for child in n_g:
                self.my_tree.delete(child)

    # Fuction to leave the game
    def quit(self):
        root.destroy()

    # Fuction for buttons to change colour when Hover or Leave
    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover, fg="white"))
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave, fg="black"))


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Solving Problem")
    root.geometry("800x528")

    Start = Interface(root)
    root.mainloop()