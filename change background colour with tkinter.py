# change background colour with tkinter and lisbox 
from tkinter import *

def open_listbox():
    listbox.place(x=50, y=30, width=100, height=100)
    scrollbar.place(x=150, y=30, height=100)
    close_button.place(x=50, y=150, width=60, height=30)
    open_button.place_forget()

def close_listbox():
    listbox.place_forget()
    scrollbar.place_forget()
    close_button.place_forget()
    open_button.place(x=50, y=30, width=60, height=30)

def clicked():
    select = listbox.curselection()
    if select:
        color = listbox.get(select)
        window.configure(background=color)

window = Tk()
window.title('Background')
window.geometry('250x250')

listbox = Listbox(window)
listbox.insert(0, 'Grey')
listbox.insert(1, 'Red')
listbox.insert(2, 'Blue')
listbox.insert(3, 'light blue')
listbox.insert(4, 'Green')
listbox.insert(5, 'light green')
listbox.insert(6, 'Purple')
listbox.insert(7, 'Yellow')
listbox.insert(8, 'White')
listbox.insert(9, 'Brown')
listbox.insert(10, 'Pink')
listbox.insert(11, 'Orange')

scrollbar = Scrollbar(window)
scrollbar.config(command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)

open_button = Button(text='Open list', command=open_listbox)
open_button.place(x=50, y=30, width=60, height=30)

close_button = Button(text='Close list', command=close_listbox)
close_button.place_forget()

click_me = Button(text='Click Me', command=clicked)
click_me.place(x=50, y=200, width=60, height=30)

window.mainloop()