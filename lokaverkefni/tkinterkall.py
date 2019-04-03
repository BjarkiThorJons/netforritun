from tkinter import *
import tkinter as tk

window = Tk()

window.title('Spjallforrit')
nafn="Ágúst"
scrollbar = Scrollbar(window)
scrollbar.pack( side = RIGHT, fill=Y )

w = Label(window, text=nafn+": ")

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

def enter_pressed(event):
    input_get = input_field.get()
    mylist.insert(END, w.cget("text") + input_get)
    input_user.set('')
    mylist.yview_moveto(1)
    return "break"

frame = Frame(window, width=600)
frame.pack_propagate(False)
input_field.bind("<Return>", enter_pressed)
frame.pack()

mylist = Listbox(window, yscrollcommand = scrollbar.set )

print(tk.constants)

img = PhotoImage(file='H:/ja.gif')
frame.create_image(0,0, anchor=NW, image=img)

mylist.pack( side = LEFT, fill = BOTH , expand=True)
scrollbar.config( command = mylist.yview )
window.mainloop()
