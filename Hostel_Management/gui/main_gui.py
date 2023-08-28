""" GUI FUNCTIONS """
import tkinter as tk
from tkinter import messagebox, PhotoImage, Label, Canvas, Frame, Button
from tkinter import ttk
from PIL import Image, ImageTk

from auth import login, register, sign_student, change_password
from session import Session


def create_main_window():
    app = tk.Tk()

    app.title("Donnie's Hostel Manager")
    app.geometry("500x600")

    bg = ImageTk.PhotoImage(file="images/main_bg.png")

    canvas = Canvas(app, width=500, height=600)
    canvas.pack(fill="both", expand=True)
    # canvas.config(background="gradient blue")

    canvas.create_image(0, 0, image=bg, anchor="nw")
    canvas.create_text(200, 300, text="WELCOME TO DHMS",
                       font=("Times New Roman", 24))

    btn1 = PhotoImage(file='images/signin.png')
    Button(canvas, image=btn1, command=None,
           borderwidth=0, border=0, text="Login").pack(pady=100)

    app.mainloop()
