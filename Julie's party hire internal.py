#import everything and ttk to get started with the code
from tkinter import *
from tkinter import ttk

root=Tk() #our window
root.geometry("635x500")#size of window

def quit(): #quit window
    root.destroy()

#append function
def append():
    global customer_details, entry_customer_name, entry_items_hired, entry_receipt_number, entry_total_items_hired, total_entries
    # clear the boxes
    customer_details.append([entry_customer_name.get(), entry_receipt_number.get(),
    entry_items_hired.get(), entry_total_items_hired.get()])
    entry_customer_name.delete(0, 'end')
    entry_receipt_number.delete(0, 'end')
    entry_items_hired.delete(0, 'end')
    entry_total_items_hired.delete(0, 'end')
    total_entries += 1

#print function
def print_customer_details():
    global total_entries, name_count, row_count
    name_count = 0
    row_count = 0
    Label(root, text="Row", fg="green").place(x=0, y=250)
    Label(root, text="Customer's Full Name", fg="green").place(x=80, y=250)
    Label(root, text="Receipt Number", fg="green").place(x=250, y=250)
    Label(root, text="Item's Hired", fg="green").place(x=400, y=250)
    Label(root, text="Number Of Item's Hired", fg="green").place(x=500, y=250)

    while name_count < total_entries:
        Label(root, text=name_count).place(x=0,y=row_count+280)
        Label(root, text=(customer_details[name_count][0])).place(
            x=80,y=row_count+280)
        Label(root, text=(customer_details[name_count][1])).place(
            x=250,y=row_count+280)
        Label(root, text=(customer_details[name_count][2])).place(
            x=400,y=row_count+280)
        Label(root, text=(customer_details[name_count][3])).place(
            x=500,y=row_count+280)
        name_count += 1
        row_count += 24


#delete row
def delete_row():
    #variables used
    global customer_details, delete_item, total_entries, row_count  
    #find which row is to be deleted and delete it
    del customer_details[int(delete_item.get())]
    total_entries= total_entries -1
    delete_item.delete(0, 'end')
    #clear the last items on GUI
    Label(root, text="                       ", background="pink").place(x=0, y=row_count+256)
    Label(root, text="                       ", background="pink").place(x=80, y=row_count+256)
    Label(root, text="                       ",background="pink").place(x=250, y=row_count+256)
    Label(root, text="                       ", background="pink").place(x=400, y=row_count+256)
    Label(root, text="                       ", background="pink").place(x=500, y=row_count+256)
    #print it all out
    print_customer_details()

#specifications
def check_inputs():
    #global variables used
    global customer_details, entry_customer_name, entry_items_hired, entry_receipt_number, entry_total_items_hired, total_entries
    input_check = 0
    Label(root, text="                   ",background="pink").place(x=457, y=60)
    Label(root, text="                   ",background="pink").place(x=457, y=90)
    Label(root, text="                   ",background="pink").place(x=457, y=120)
    Label(root, text="                   ",background="pink").place(x=457, y=150)

#check that customer entry is not blank
    if len(entry_customer_name.get()) == 0:
        Label(root, fg="red",background="pink", text="Required").place(x=457, y=60)
        input_check=1

#check that receipt number entry is not blank
    if len(entry_receipt_number.get()) == 0 :
        Label(root, fg="red", background="pink", text="Required") .place(x=457, y=90)
        input_check=1

#check that items hired is not blank
    if len(entry_items_hired.get()) == 0:
        Label(root, fg="red",background="pink", text="Required").place(x=457, y=120)
        input_check=1

#check that total items hired is not blank and is between 1-500 
    if (entry_total_items_hired.get().isdigit()):
        if int(entry_total_items_hired.get()) < 1 or int(entry_total_items_hired.get()) > 500:
            Label(root, fg="red",background="pink", text="1-500 only").place(x=457, y=150)
            input_check=1
    else:
        Label(root, fg="red" ,background="pink", text=" 1-500 only").place(x=457, y=150)
        input_check=1
    if input_check ==0: 
        append()

#setup buttons
def setup_buttons():
    global customer_details, entry_customer_name,entry_items_hired, entry_receipt_number, entry_total_items_hired, delete_item

#heading
    Label(root, width="61", text="Julie's Party Hire", font="Ariel", fg="green").place(x=0, y=0)
#buttons
    ttk.Button(root, text="Print", command=print_customer_details).place(x=530, y=90)
    ttk.Button(root, text="Append", command=check_inputs).place(x=530, y=120)
    ttk.Button(root, text=" Quit", command=quit).place(x=530, y=150)
    ttk.Button(root, text="Delete", command=delete_row).place(x=530, y=180)

#customer name
    Label(root, width="20", text="Customer's Full Name", fg="green").place(x=0, y=60)
    entry_customer_name=Entry(root, width=35)
    entry_customer_name.place(x=230,y=60 )

#receipt number
    Label(root, width="20", text="Receipt Number", fg="green").place(x=1, y=90)
    entry_receipt_number=Entry(root, width=35)
    entry_receipt_number.place(x=230,y=90)

#items hired
    Label(root, width="20", text="Items Hired", fg="green").place(x=1, y=120)
    entry_items_hired=Entry(root, width=35)
    entry_items_hired.place(x=230,y=120 )

#total number of items hired
    Label(root, width="20", text="Number Of Items Hired", fg="green").place(x=1, y=150)
    entry_total_items_hired=Entry(root, width=35)
    entry_total_items_hired.place(x=230,y=150)

#row
    Label(root, width="20", text="Row", fg="green").place(x=1, y=180)
    delete_item=Entry(root, width=35)
    delete_item.place(x=230,y=180)
    ttk.Button(root, text="Delete", command=delete_row).place(x=530, y=180)

#running the code
def main():
    global root, customer_details, total_entries
    customer_details=[]#create an empty list
    total_entries= 0
    setup_buttons()
    root.config(bg="pink")#bacground color
    root.title("Shivi<3") #the title of the window
    root.mainloop()#make sure it keeps loopin

main()
