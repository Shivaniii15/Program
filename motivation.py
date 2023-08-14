#import everything and ttk to get started with the code
from tkinter import *
from tkinter import ttk
import tkinter.font as font

root=Tk() #our window
root.geometry("809x458")#size of window

#maximum and minimum size
root.minsize(809,458)
root.maxsize(809,458)

#adding image
bg= PhotoImage(file= "screenshot (112).png")

#creating canvas
canvas1= Canvas( root, width=809, height=460)
canvas1.pack(fill="both", expand=True)

#displaying image
canvas1.create_image(0, 0,image=bg, anchor="nw")

#defining font
myFont = font.Font(family='Helvetica', size=10, weight='bold')

#adding functions
def quit(): #quit window
    root.destroy()

def home():
    root.destroy()
    import home

#adding buttons
#the basic ones
button1= Button (root, text="Quit", command=quit , bg='#F14975', fg='white', activebackground='#288C70', activeforeground='white' )
button1.place(x=600, y=423)
button2= Button (root, text="Home", command=home, bg='#F14975', fg='white', activebackground='#288C70', activeforeground='white')
button2.place(x=185, y=423)

#adding labels
label1=Label(root, text="1000 is the only number from 0 to 1000 that has an “a” in it!", wraplength=100, width= 13,
      bg="#CB6CE6", font=("helvetica", 10)).place(x=145, y=145)



#applying font
button1['font']= myFont
button2['font']= myFont

#running the code
def main():
    global root
    root.config
    root.title("Shivani <3") #title of the window
    root.mainloop()#make sure it keeps looping

main()
