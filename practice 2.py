    #check that the entries are not left blank
def append():
        global user_details, entry_name, entry_age, total_entries
# clear the boxes
        user_details.append([entry_name.get()])
        entry_name.delete(0, 'end')
        entry_age.delete(0, 'end')

        total_entries += 1

def check_inputs():
    #global variables used
    global user_details, entry_name, entry_age, total_entries
    input_check = 0
    Label(app, text="                   ",background="pink").place(x=457, y=60)
    Label(app, text="                   ",background="pink").place(x=457, y=90)

#check that customer entry is not blank
    if len(entry_name.get()) == 0:
        Label(app, fg="black",background="#FFF3E4", text="Required").place(x=250, y=150)
        input_check=1

#check that the age is not blank and is between 7- 12 
    if (entry_age.get().isdigit()):
        if int(entry_age.get()) < 7 or int(entry_age.get()) > 12:
            Label(app, fg="black",background="#FFF3E4", text="7-12 only").place(x=250, y=250)
            input_check=1
        else:
            Label(app, fg="black" ,background="#FFF3E4", text=" 7-12 only").place(x=250, y=250)
            input_check=1
        if input_check ==0: 
            append()

