from tkinter import *

def convert1() :
    MILES = text_box_1.get()
    MILES = int(MILES)
    message = round(MILES * 1.609344,2)
    text_box_2.delete(0,END)
    text_box_2.insert(END,message)
    text_box_2.insert(END,' KM')

def convert2() :
    km = text_box_1.get()
    km = int(km)
    message = round(km*0.62137,2)
    text_box_2.delete(0,END)
    text_box_2.insert(END,message)
    text_box_2.insert(END,' Miles')

window = Tk()
window.title('Distance Converter ')
window.geometry('260x200')

Label_1 = Label(text='Eneter the value you want to convert :')
Label_1.place(x=30,y=20)

text_box_1 = Entry(text = " ")
text_box_1.place(x = 30 ,y = 50 ,width= 200,height= 25)
text_box_1['justify'] = 'center'
text_box_1.focus()

convert1 = Button(text='convert Mile to KM',command=convert1)
convert1.place(x=30,y=80,width=200,height=25)

convert2 = Button(text='convert KM to Mile',command=convert2)
convert2.place(x=30,y=110,width=200,height=25)

text_box_2 = Entry(text = "")
text_box_2.place(x = 30 ,y = 140 ,width= 200,height=25)
text_box_2['justify'] = 'center'


window.mainloop()