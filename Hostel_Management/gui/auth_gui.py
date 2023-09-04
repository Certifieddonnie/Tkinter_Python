""" Authentication GUI """
import tkinter as tk
from tkinter import messagebox, PhotoImage, Label, Canvas, Frame, Button
from tkinter import ttk
from PIL import Image, ImageTk

from auth import login, register, sign_student, change_password
from session import Session
from gui.main_gui import create_main_window


def open_registration_window():
    """ Register Window """
    def g_register():
        firstname = firstname_entry.get()
        lastname = lastname_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        user_type = user_type_combobox.get()
        gender = gender_combobox.get()

        if len(username) < 4 or len(password) < 6:
            messagebox.showerror(
                "Registration Error", "Username must be at least 4 characters and Password must be at least 6 Characters long")
            return
        if not gender or not user_type:
            messagebox.showerror("Registration Error",
                                 "Gender or User Type must not be empty!")
            return

        result = register(firstname, lastname, username,
                          password, user_type, gender)

        if result == "true":
            messagebox.showerror("Registration Error", "User already exists")
        else:
            messagebox.showinfo("Registration Successful",
                                "User Registration Completed")
            registration_window.destroy()

    registration_window = tk.Toplevel(
        bg="white", highlightthickness=0, bd=0)
    registration_window.title("Registration Window")
    registration_window.geometry("700x600")

    bg = ImageTk.PhotoImage(file="images/main_bg.png")

    canvas = Canvas(registration_window, width=500, height=600)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, image=bg, anchor="nw")
    canvas.create_text(350, 100, text="Registration Window",
                       font=("Times New Roman", 40), justify='center', fill="white")

    # Create a frame
    frame = Frame(registration_window, bg="grey")
    frame.place(relx=0.5, rely=0.3, relwidth=0.8, relheight=0.53, anchor="n")

    # Create a label
    firstname_label = Label(frame, text="First Name", bg="white")
    firstname_label.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)

    # Create a entry
    firstname_entry = ttk.Entry(frame)
    firstname_entry.place(relx=0.4, rely=0.1, relwidth=0.5, relheight=0.1)

    # Create a label
    lastname_label = Label(frame, text="Last Name", bg="white")
    lastname_label.place(relx=0.1, rely=0.25, relwidth=0.3, relheight=0.1)

    # Create a entry
    lastname_entry = ttk.Entry(frame)
    lastname_entry.place(relx=0.4, rely=0.25, relwidth=0.5, relheight=0.1)

    # Create a label
    username_label = Label(frame, text="Username", bg="white")
    username_label.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)

    # Create a entry
    username_entry = ttk.Entry(frame)
    username_entry.place(relx=0.4, rely=0.4, relwidth=0.5, relheight=0.1)

    # Create a label
    password_label = Label(frame, text="Password", bg="white")
    password_label.place(relx=0.1, rely=0.55, relwidth=0.3, relheight=0.1)

    # Create a entry
    password_entry = ttk.Entry(frame, show="*")
    password_entry.place(relx=0.4, rely=0.55, relwidth=0.5, relheight=0.1)

    # Create a label
    user_type_label = Label(frame, text="User Type", bg="white")
    user_type_label.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.1)

    # Create combobox
    user_type_choices = ["Admin", "Student"]
    user_type_combobox = ttk.Combobox(frame, values=user_type_choices)
    user_type_combobox.place(relx=0.4, rely=0.7, relwidth=0.5, relheight=0.1)

    # Create a label
    gender_label = Label(frame, text="Gender", bg="white")
    gender_label.place(relx=0.1, rely=0.85, relwidth=0.3, relheight=0.1)

    # Create combobox
    gender_choices = ["Male", "Female"]
    gender_combobox = ttk.Combobox(frame, values=gender_choices)
    gender_combobox.place(relx=0.4, rely=0.85, relwidth=0.5, relheight=0.1)

    register_button = Button(canvas, text="Register", font=(
        "Helvetica", 16), padx=20, pady=10, bg="royal blue", bd=0, highlightthickness=0, fg="white", command=g_register)
    register_button.place(relx=0.4, rely=0.85, relwidth=0.3, relheight=0.1)

    registration_window.mainloop()


def open_login_window(app):
    """ Login Window """
    def g_login():
        username = username_entry.get()
        password = password_entry.get()

        result = login(username, password)

        if result:
            messagebox.showinfo("Login Successful",
                                f"Welcome {username}")
            login_window.withdraw()
            app.withdraw()

        else:
            messagebox.showerror("Login Error", "User credentials not found!")

    login_window = tk.Toplevel(
        bg="white", highlightthickness=0, bd=0)
    login_window.title("Login Window")
    login_window.geometry("700x600")

    bg = ImageTk.PhotoImage(file="images/main_bg.png")

    canvas = Canvas(login_window, width=500, height=600)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, image=bg, anchor="nw")
    canvas.create_text(350, 100, text="Login Window",
                       font=("Times New Roman", 40), justify='center', fill="white")

    # Create a frame
    frame = Frame(login_window, bg="grey")
    frame.place(relx=0.5, rely=0.3, relwidth=0.8, relheight=0.53, anchor="n")

    # Create a label
    username_label = Label(frame, text="Username", bg="white")
    username_label.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)

    # Create a entry
    username_entry = ttk.Entry(frame)
    username_entry.place(relx=0.4, rely=0.1, relwidth=0.5, relheight=0.1)

    # Create a label
    password_label = Label(frame, text="Password", bg="white")
    password_label.place(relx=0.1, rely=0.25, relwidth=0.3, relheight=0.1)

    # Create a entry
    password_entry = ttk.Entry(frame, show='*')
    password_entry.place(relx=0.4, rely=0.25, relwidth=0.5, relheight=0.1)

    login_button = Button(frame, text="Login", font=(
        "Helvetica", 16), padx=20, pady=10, bg="royal blue", bd=0, highlightthickness=0, fg="white", command=g_login)
    login_button.place(relx=0.4, rely=0.85, relwidth=0.3, relheight=0.1)

    login_window.mainloop()
