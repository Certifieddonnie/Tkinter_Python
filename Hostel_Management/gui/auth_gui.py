""" Authentication GUI """
import tkinter as tk
from tkinter import messagebox, PhotoImage, Label, Canvas, Frame, Button
from tkinter import ttk
from PIL import Image, ImageTk

from auth import login, register, sign_student, change_password
from session import Session


def register():
    """sign up window"""
