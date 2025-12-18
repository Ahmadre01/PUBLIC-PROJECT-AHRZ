from tkinter import *

root = Tk()
root.geometry("500x300")

Label(root, text="Perosnality Registration Form", font="Arial 15 bold", bg="lightgreen").grid(row=1, column=3)

Name = Label(root, text="Name =", font="Arial 10")
lastname = Label(root, text="Last Name =", font="Arial 10")
Gender = Label(root, text="Gender =", font="Arial 10")
Phone = Label(root, text="Phone Number =", font="Arial 10")
Email = Label(root, text="Email =", font="Arial 10")
Paymentmethod = Label(root, text="Payment method =", font="Arial 10")
select_payment = Label(root,text=" ((select payment metohd)) ",font="Arial 11 italic")

Name.grid(row=2, column=2)
lastname.grid(row=3, column=2)
Gender.grid(row=4, column=2)
Phone.grid(row=5, column=2)
Email.grid(row=6, column=2)
Paymentmethod.grid(row=7, column=2)
select_payment.grid(row=7,column=3)

Namevalue = StringVar()
lastnamevalue = StringVar()
Phonevalue = StringVar()
Gendervalue = StringVar()
Emailvalue = StringVar()
Paymentmethodvalue = StringVar()
checkvalue = IntVar()

Nameentry = Entry(root, textvariable=Namevalue)
lastnameentry = Entry(root, textvariable=lastnamevalue)
Phoneentry = Entry(root, textvariable=Phonevalue)
Genderentry = Entry(root, textvariable=Gendervalue)
Emailentry = Entry(root, textvariable=Emailvalue)
Paymentmethodentry = StringVar()


Nameentry.grid(row=2, column=3)
lastnameentry.grid(row=3, column=3)
Phoneentry.grid(row=4, column=3)
Genderentry.grid(row=5, column=3)
Emailentry.grid(row=6, column=3)

def submit():
    first_name = Nameentry.get()
    last_name = lastnameentry.get()
    phone_number = Phoneentry.get()
    email = Emailentry.get()
    payment_type = Paymentmethodentry.get()
    
    print("Information Submitted (Registration Form) ==>")
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Phone Number:", phone_number)
    print("Email:", email)
    print("Payment Type:",payment_type)

    if checkvalue.get() == 1:
        print("Remember Me: Yes")
    else:
        print("Remember Me: No")
    print("/////////////////////////// \n")

Button(root, text='Submit', command=submit).grid(column=3, row=9)

payment_options = ["Credit Card","PayPal","Bank Transfer"]

for index, option in enumerate(payment_options):
    Radiobutton(root, text=option, variable=Paymentmethodentry, value=option).grid(row=8,column=2+index)

checkbutton = Checkbutton(text="Remember me?", variable=checkvalue, bg="lightblue")
checkbutton.grid(row=9, column=3)

Button(text="Submit", command=submit).grid(row=10, column=3)

def clear_entries():
    Nameentry.delete(0, END)
    lastnameentry.delete(0, END)
    Phoneentry.delete(0, END)
    Genderentry.delete(0, END)
    Emailentry.delete(0, END)
    Paymentmethodentry.delete(0, END)
    checkbutton.deselect()

Clearbutton = Button(text='Clear Data', command=clear_entries)
Clearbutton.grid(row=11, column=3)

root.mainloop()
