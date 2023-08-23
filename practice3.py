import tkinter as tk
from tkinter import ttk
  
 
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
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Page 1",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Page 2",
        command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
          
  
  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  
  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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


#----------------------# sixth window frame page4---------------------------------------------#


class Page5(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

#background image
        self.image5= PhotoImage(file="Screenshot (135).png")
        self.start_bg= Label(self, image=self.image5)
        self.start_bg.grid(row=0,column=0)

#question
        Label(self, width="27", text="How much is 3/8 times three?", fg="white", bg= "black" , font=("helvetica", 14) ).place(x=298, y=165)

#options 
        #option 2 is right
        option1=Radiobutton(self, value="one", font=("helvetica", 12), text="6/8", bg="#FF7C9F", fg="black")
        option1.place(x=295, y=426)
        option2=Radiobutton(self, value="two", font=("helvetica", 12), text="9/8", bg="#FF7C9F", fg="black")
        option2.place(x=567, y=426)
        option3=Radiobutton(self, value="three", font=("helvetica", 12), text="8/6", bg="#FF7C9F", fg="black")
        option3.place(x=295, y=300)
        option4=Radiobutton(self, value="four", font=("helvetica", 12), text="8/9", bg="#FF7C9F", fg="black")
        option4.place(x=565, y=300)

#next button to show frame 5

        button5= Button (self, text="Next", bg="#43B262", activebackground="#A5C2E9", width=10, font=("Helvetica", 12, "bold"),
                        command = lambda : controller.show_frame(Page1))
        
        button5.place(x=730, y=440)
        button6= Button (self, text="Quit", bg="#A5C2E9", activebackground="#8E699D", width=10, font=("Helvetica", 12, "bold"),
                        command = quit)
        button6.place(x=80, y=440)
  
  
# Driver Code
app = tkinterApp()
app.mainloop()