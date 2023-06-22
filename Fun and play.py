#import everything and ttk to get started with the code
from tkinter import *
from tkinter import ttk

root=Tk() #our window
root.geometry("749x405")#size of window

#adding image
bg= PhotoImage(file= "screenshot (66).png")

#creating canvas
canvas1= Canvas( root, width=749, height=405)
canvas1.pack(fill="both")

#displaying image
canvas1.create_image(0, 0,image=bg)

def quit(): #quit window
    root.destroy()

#running the code
def main():
    global root
    root.config
    root.title("Shivani <3") #title of the window
    root.mainloop()#make sure it keeps looping

main()
