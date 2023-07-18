#import everything and ttk to get started with the code
from tkinter import *
from tkinter import ttk
import tkinter.font as font

root=Tk() #our window
root.geometry("735x405")#size of window

#maximum and minimum size
root.minsize(735,405)
root.maxsize(735,405)

#adding image
bg= PhotoImage(file= "screenshot (66).png")

#creating canvas
canvas1= Canvas( root, width=749, height=405)
canvas1.pack(fill="both", expand=True)

#displaying image
canvas1.create_image(0, 0,image=bg, anchor="nw")

#defining font
myFont = font.Font(family='Helvetica', size=10, weight='bold')

#function to go to the next page
def topics():#topics page
    root.destroy()
    import topics

def facts():#fun facts page
    root.destroy()
    import facts 

def quizzes():#quizzes page
    root.destroy()
    import quizzes

def notes():
    root.destroy()
    import notes

#adding buttons
#the basic ones
button1= Button (root, text="Quit", command=quit , bg='#F14975', fg='white', activebackground='#288C70', activeforeground='white' )
button1.place(x=550, y=376)
button2= Button (root, text="Home", bg='#F14975', fg='white', activebackground='#288C70', activeforeground='white')
button2.place(x=95, y=376)

#the activity ones
button3= Button (root, text="TOPICS!", command=topics, bg='#8191FF', activebackground='#133795', activeforeground='white')
button3.place(x=167, y=170)
button4= Button (root, text="FUN FACTS", command=facts, bg='#FFC327', activebackground='#FF914D', activeforeground='white')
button4.place(x=330, y=160)
button5= Button (root, text="QUIZES!", command=quizzes, bg='#FF8652', activebackground='#FF0013', activeforeground='white')
button5.place(x=526, y=164)
button6= Button (root, text="REPORT!", bg='#43B262', activebackground='#168062', activeforeground='white')
button6.place(x=235,y=318)
button7= Button (root, text="NOTES", command=notes, bg='#C24468', activebackground='#E13B67', activeforeground='white')
button7.place(x=445, y=320)

#applying font
button1['font']= myFont
button2['font']= myFont
button3['font']= myFont
button4['font']= myFont
button5['font']= myFont
button6['font']= myFont
button7['font']= myFont

def quit(): #quit window
    root.destroy()

#running the code
def main():
    global root
    root.config
    root.title("Shivani <3") #title of the window
    root.mainloop()#make sure it keeps looping

main()
