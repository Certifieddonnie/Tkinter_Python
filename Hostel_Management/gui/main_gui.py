""" GUI FUNCTIONS """
import tkinter as tk
from tkinter import Canvas, Button
from PIL import ImageTk


def create_main_window():
    app = tk.Tk()

    app.title("WELCOME WINDOW")
    app.geometry("700x600")

    bg = ImageTk.PhotoImage(file="images/main_bg.png")

    canvas = Canvas(app, width=500, height=600)
    canvas.pack(fill="both", expand=True)
    # canvas.config(background="gradient blue")

    canvas.create_image(0, 0, image=bg, anchor="nw")
    canvas.create_text(350, 200, text="WELCOME USER!",
                       font=("Times New Roman", 40), justify='center', fill="white")

    # btn1 = PhotoImage(file='images/signin.png')
    # Button(canvas, image=btn1, command=None,
    #        borderwidth=0, border=0, text="Login").pack(pady=100)
    sign_up_color = "royal blue"
    sign_in_color = "dark blue"

    sign_up_button = Button(canvas, text="Sign Up", font=(
        "Helvetica", 20), padx=20, pady=10, bg=sign_up_color, bd=0, highlightthickness=0, fg="white")
    sign_up_button.pack(pady=270, side="left", padx=100)

    sign_in_button = Button(canvas, text="Sign In", font=(
        "Helvetica", 20), padx=20, pady=10, bg=sign_in_color, bd=0, highlightthickness=0, fg="white")
    sign_in_button.pack(pady=270, side="right", padx=100)

    app.mainloop()
