import sqlite3
import tkinter as tk
from tkinter import *
import sv_ttk

from string import *
from tkinter import messagebox, ttk

def about():
        # root.destroy()
        rooa = tk.Tk()
        sv_ttk.set_theme("dark")
        rooa.geometry("1200x1200")
        rooa.configure(bg="#222324")
        title = Label(rooa, text="About Us...", width=10, height=2, font=('Helvetica', 40, "bold"), bg="#222324", fg = "White").place(x=200, y=50)
        k = Label(rooa, text="Founded in 2020 by four college friends in Manipal(India),",
                  width=150, height=2, font=('Helvetica', 10), bg="#222324", fg = "White").place(x=100, y=250)
        a = Label(rooa, text="Book-A-Buggy has since become a very famous online buggy(E-Taxi) booking website in Manipal and many famous university cities.",
                  width=150, height=2, font=('Helvetica', 10), bg="#222324", fg = "White").place(x=100, y=300)
        b = Label(rooa, text="We dedicate ourselves on providing seamless services to thousands of students to search for various buggies ",
                  width=150, height=2, font=('Helvetica', 10), bg="#222324", fg = "White").place(x=100, y=350)
        c = Label(rooa, text="and go for the best available option. Book-a-Buggy's mission is to become your companion to experience seamless booking service. ",
                  width=150, height=2, font=('Helvetica', 10), bg="#222324", fg = "White").place(x=100, y=400)
        e = d = Label(rooa, text="Come Join us at Book-a-Buggy",
                      width=150, height=2, font=('Helvetica', 10), bg="#222324", fg = "White").place(x=100, y=500)

        def home1():
            rooa.destroy()
            
        but = tk.Button(rooa, text="Home", font=("Heveltica", 15), command=home1).place(width=250, height=40, x=480, y=600)
        rooa.mainloop()