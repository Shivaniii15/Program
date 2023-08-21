#import everything and ttk to get started with the code
from tkinter import *
from tkinter import ttk
import tkinter.font as font

root=Tk() #our window
root.geometry("790x420")#size of window

#maximum and minimum size
root.minsize(790,420)
root.maxsize(790,420)

#adding image
bg= PhotoImage(file= "screenshot (84).png")

#creating canvas
canvas1= Canvas( root, width=749, height=405)
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
button1.place(x=580, y=385)
button2= Button (root, text="Home", command=home, bg='#F14975', fg='white', activebackground='#288C70', activeforeground='white')
button2.place(x=175, y=385)

#applying font
button1['font']= myFont
button2['font']= myFont 

#adding labels
label1=Label(root, text="Roman Numerals", wraplength=200, width= 14,
      bg="#43B262", font=("helvetica", 12)).place(x=145, y=140)
label2=Label(root, text="Decimals", wraplength=200, width= 14,
      bg="#E1691E", font=("helvetica", 12)).place(x=145, y=220)
label3=Label(root, text="Complex calculations", wraplength=200, width= 16,
      bg="#43B262", font=("helvetica", 12)).place(x=500, y=140)
label4=Label(root, text="Fractions", wraplength=100, width= 14,
      bg="#43B262", font=("helvetica", 12)).place(x=149, y=300)
label5=Label(root, text="Percentage", wraplength=100, width= 14,
      bg="#E1691E", font=("helvetica", 12)).place(x=500, y=220)
label6=Label(root, text="Times tables", wraplength=100, width= 14,
      bg="#43B262", font=("helvetica", 12)).place(x=500, y=300)

def main():
    global root
    root.config
    root.title("Shivani <3") #title of the window
    root.mainloop()#make sure it keeps looping

main()