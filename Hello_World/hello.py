#!/usr/bin/python3
""" Hello World GUI Application """

import tkinter

app = tkinter.Tk()

app.title("Hello TKinter")
app.geometry('350x200')

menu = tkinter.Menu(app)
# item = tkinter.Menu(menu)

menu.add_cascade(label='Home')
menu.add_cascade(label='File')
menu.add_cascade(label='View')
menu.add_cascade(label='Help')
app.config(menu=menu, bg='Light Blue')
menu.config(activeforeground='white', activebackground='black')


app.mainloop()
