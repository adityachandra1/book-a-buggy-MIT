import sqlite3
import tkinter as tk
from tkinter import *
import sv_ttk

from string import *
from tkinter import messagebox, ttk



def showbok():
        # root.destroy()
        ros = tk.Tk()
        sv_ttk.set_theme("dark")
        ros.configure()
        ros.geometry("1200x1200")
        conn = sqlite3.Connection("example.db")
        cu = conn.cursor()
        cu.execute("""SELECT * FROM TEST3""")
        Label(ros, text="From")
        for i in cu.fetchall():
            lab = tk.Label(ros, text=i, font=('Heveltica', 14)).pack()

        def homeb():
            ros.destroy()
            # home()
        bu_t = tk.Button(ros, text="home", command=homeb, bg="blue", font=(
            "lucida calligraphy", 15), fg="white", width=15, height=3).place(x=600, y=600)