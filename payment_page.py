import sqlite3
import tkinter as tk
from tkinter import *
import sv_ttk

from string import *
from tkinter import messagebox, ttk

conn = sqlite3.Connection("example.db")

def payment():
        roop = tk.Tk()
        roop.title("Book-A-Buggy")
        sv_ttk.set_theme("dark")
        swidth = roop.winfo_screenwidth()
        sheight = roop.winfo_screenheight()
        roop.configure(bg='#161617')
        fr = tk.Frame(roop,bg="#222324", fg = "White", width=swidth, height=sheight).pack()
        bon = Label(roop, text="Book-A-Buggy", font=(
            "lucida calligraphy", 40, "bold"),bg="#222324", fg = "White", bd=0).place(x=10, y=10)
        come = Label(roop, text="   Come Explore your Dreams!!!", font=(
            "lucida calligraphy", 25),bg="#222324", fg = "White").place(x=500, y=20)
        lab_me = tk.Label(roop, bg="#161617").place(
            x=0, y=80, width=swidth, height=70)
        but_home = tk.Button(roop, text="HOME", bg="#161617", bd=0, fg="white", font=(
            "lucida calligraphy", 25)).place(x=650, y=80)
        frame_pay = tk.Frame(roop, bg="#222324").place(
            x=300, y=200, width=950, height=600)
        lab_heading = tk.Label(roop, bg='#222324', font=(
            "lucida calligraphy", 20), text="PAYMENT GATEWAY").place(x=600, y=250)
        bu_paytm = tk.Button(roop, text="PAY WITH THE CASH", font=(
            "lucida calligraphy", 20), bg="#222324").place(x=600, y=400)
        bu_paytm = tk.Button(roop, text="PAY WITH DEBIT/CREDIT/INTERNET BANKING",font=("lucida calligraphy", 20), bg="#222324").place(x=460, y=500)
        roop.mainloop()


