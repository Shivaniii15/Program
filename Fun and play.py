#import everything and ttk to get started with the code
from tkinter import *
from tkinter import ttk

root=Tk() #our window
root.geometry("735x405")#size of window

#adding image
bg= PhotoImage(file= "screenshot (66).png")

#creating canvas
canvas1= Canvas( root, width=749, height=405)
canvas1.pack(fill="both", expand=True)

#displaying image
canvas1.create_image(0, 0,image=bg, anchor="nw")

#adding buttons
#the basic ones
button1= Button (root, text="Quit", command=quit)
button1.place(x=550, y=376)
button2= Button (root, text="Home")
button2.place(x=95, y=376)

#the activity ones
button3= Button (root, text="TOPICS!")
button3.place(x=170, y=174)
button4= Button (root, text="FUN FACTS")
button4.place(x=270, y=174)
button5= Button (root, text="QUIZES!")
button5.place(x=400, y=100)
button6= Button (root, text="REPORT!")
button6.place
button7= Button (root, text="NOTES AND SUMMARY")
button3.place

def quit(): #quit window
    root.destroy()

#running the code
def main():
    global root
    root.config
    root.title("Shivani <3") #title of the window
    root.mainloop()#make sure it keeps looping

main()
