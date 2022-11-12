import sqlite3
import tkinter as tk
from tkinter import *
import sv_ttk
from string import *
from tkinter import messagebox, ttk



def cancel():
        # root.destroy()
        rooc = tk.Tk()
        rooc.configure(bg="#161617")
        sv_ttk.set_theme("dark")
        # rooc.geometry('1000x1000')
        swidth = 1200
        sheight = 1200
        title = Label(rooc, text="Cancel Ticket", width=300, height=2, font=('Helvetica', 40, "bold"),bg="#222324", fg = "White").place(x=1200, y=50)
        rooc_fr1 = tk.Frame(rooc, width=swidth,height=sheight, bg = "#161617").pack()
        # log_1 = Label(rooc_fr1, text="Book-A-Buggy", font=("lucida calligraphy", 40, "bold"), bd=0).place(x=10, y=10)
        # log_2 = Label(rooc_fr1, text="Book-A-Buggy", font=("lucida calligraphy", 40, "bold"), bd=0).place(x=10, y=10)
        # rooc_fr2 = tk.Label(rooc).place(x=0, y=80, width=swidth, height=70)
        b = tk.Frame(rooc, width="1000",height="500",bg="#222324").place(x=100, y=200)
        mob_can = StringVar()
        mobile_en = tk.Label(rooc, text="Enter Mobile Number", font=("Heveltica", 20),bg="#222324", fg = "White",).place(x=100, y=350)
        mob_enR = tk.Entry(rooc, textvariable=mob_can).place(x=500, y=350, width=450, height=40)

        def dell():
            a = mob_can.get()
            print(type(a))
            print(a)
            conn = sqlite3.Connection("example.db")
            conn.execute('''DELETE FROM TEST3''')
            conn.commit()

            messagebox.showinfo(
                "Congratulations!!", "YOUR TICKET WAS SUCESFULLY CANCELLED")
            rooc.destroy()
            # home()

        def home_cancel():
            rooc.destroy()
            # home()

        cancel_button = tk.Button(rooc, text="Cancel Ticket", font=("Heveltica", 18), command=dell, bg="Red", fg="white", width=25, height=3).place(x=200, y=550)
        bu_t_home = tk.Button(rooc, text="Home", font=("Heveltica", 18), command=home_cancel, bg="blue", fg="white", width=25, height=3).place(x=600, y=550)