import sqlite3
import tkinter as tk
from tkinter import *
import sv_ttk

from string import *
from tkinter import messagebox, ttk

conn = sqlite3.Connection("example.db")

   

def service():
        # root.destroy()
        rooaa = tk.Tk()
        sv_ttk.set_theme("dark")
        rooaa.configure(bg="#222324")
        rooaa.geometry("1200x1200")
        title = Label(rooaa, text="Products and Services", width=20, height=2, font=('Helvetica', 40),bg="#222324", fg = "White").place(x=40, y=50)
        k = Label(rooaa, text="We provide many services throughout the country .",
                  width=100, height=2, font=('Helvetica', 15),bg="#222324", fg = "White").place(x=40, y=250)
        a = Label(rooaa, text="Some of the most prominent ones include cab services in major metropolitean cities, etc.",
                  width=100, height=2, font=('Helvetica', 15),bg="#222324", fg = "White").place(x=40, y=350)
        b = Label(rooaa, text="Book-a-Buggy is an extension to our famous cab service 'hola' which was specifically made",
                  width=100, height=2, font=('Helvetica', 15),bg="#222324", fg = "White").place(x=40, y=450)
        c = Label(rooaa, text="for the students and towns which are highly populated with students.",
                  width=100, height=2, font=('Helvetica', 15),bg="#222324", fg = "White").place(x=40, y=550)

        def homeser():
            rooaa.destroy()
            # home()
        but_ser = tk.Button(rooaa, text="HOME", font=(
            "Heveltica", 15), bg='grey', command=homeser).place(width=290, height=40, x=500, y=650)
        rooaa.mainloop()
