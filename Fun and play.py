#import everything and ttk to get started with the code
from tkinter import *
from tkinter import ttk

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

#adding buttons
#the basic ones
button1= Button (root, text="Quit", command=quit , bg='#F14975', fg='white', activebackground='#288C70', activeforeground='white' )
button1.place(x=550, y=376)
button2= Button (root, text="Home", bg='#F14975', fg='white', activebackground='#288C70', activeforeground='white')
button2.place(x=95, y=376)

#the activity ones
button3= Button (root, text="TOPICS!", activebackground='#133795', activeforeground='white')
button3.place(x=170, y=174)
button4= Button (root, text="FUN FACTS", activebackground='#FF914D', activeforeground='white')
button4.place(x=334, y=160)
button5= Button (root, text="QUIZES!", activebackground='#FF0013', activeforeground='white')
button5.place(x=530, y=164)
button6= Button (root, text="REPORT!", activebackground='#168062', activeforeground='white')
button6.place(x=243,y=318)
button7= Button (root, text="NOTES", activebackground='#E13B67', activeforeground='white')
button7.place(x=448, y=320)

def quit(): #quit window
    root.destroy()

#running the code
def main():
    global root
    root.config
    root.title("Shivani <3") #title of the window
    root.mainloop()#make sure it keeps looping

main()
