import sqlite3
import tkinter as tk
from tkinter import *
import sv_ttk

from string import *
from tkinter import messagebox, ttk

conn = sqlite3.Connection("example.db")

def feed():
        # root.destroy()
        swidth = 1200
        sheight = 1200
        roof = tk.Tk()
        sv_ttk.set_theme("dark")
        roof.title("FEEDBACK FORM")
        frame_feed = tk.Frame(roof, bg="#222324", width=swidth, height=sheight).pack()
        bon = Label(roof, text="Book-A-Buggy", font=("lucida calligraphy", 40, "bold"),bg="#222324",bd=0, fg= "white").place(x=10, y=10)
        ab_me = tk.Label(roof, bg="#161617").place(
            x=0, y=80, width=swidth, height=70)
        ab_ = tk.Label(roof, text="FeedBack Form", font=("lucida calligraphy", 25), bg = "#161617", fg="white").place(x=10, y=100)
        frame_entry = tk.Frame(roof, bg="#222324", width="1300",height="700").place(x=100, y=200)
        lab_name = tk.Label(roof, text="NAME :", bg="#222324", fg = "White", font=(
            "lucida calligraphy", 15)).place(x=110, y=300)
        name_of = StringVar()
        mobile_num = StringVar()
        genderf = StringVar()
        b_e = StringVar()
        c_s = StringVar()
        cll_s = StringVar()
        p_exp = StringVar()
        val = ['EXCELLENT', 'VERY GOOD', 'GOOD', 'BAD', 'WORST']
        name_enr = tk.Entry(roof, textvariable=name_of).place(
            x=110, y=350, width=450, height=40)
        lab_mob = tk.Label(roof, text="MOBILE NUMBER:", bg="#222324", fg = "White", font=(
            "lucida calligraphy", 15)).place(x=700, y=300)
        mob_enr = tk.Entry(roof, textvariable=mobile_num).place(
            x=700, y=350, width=450, height=40)
        lab_gender = tk.Label(roof, text="Gender:", bg="#222324", fg = "White", font=(
            "lucida calligraphy", 15)).place(x=110, y=400)
        sex_enr = ttk.Combobox(roof, textvariable=genderf, values=[
                               'Male', 'Female', 'Others']).place(x=110, y=450, height=40, width=450)
        lab_b_e = tk.Label(roof, text="BOOKING EXPERIENCE :", bg="#222324", fg = "White", font=(
            "lucida calligraphy", 15)).place(x=700, y=400)
        b_e_enr = ttk.Combobox(roof, textvariable=b_e, values=val).place(
            x=700, y=450, height=40, width=450)
        lab_c_s = tk.Label(roof, text="CUSTOMER SERVICE :", bg="#222324", fg = "White", font=(
            "lucida calligraphy", 15)).place(x=110, y=500)
        c_s_enr = ttk.Combobox(roof, textvariable=c_s, values=val).place(
            x=110, y=550, height=40, width=450)
        lab_cll_s = tk.Label(roof, text="CALL SERVICE :", bg="#222324", fg = "White", font=(
            "lucida calligraphy", 15)).place(x=700, y=500)
        cll_s_enr = ttk.Combobox(roof, textvariable=cll_s, values=val).place(
            x=700, y=550, height=40, width=450)
        lab_p_exp = tk.Label(roof, text="PAYMENT EXPERIENCE :", bg="#222324", fg = "White", font=(
            "lucida calligraphy", 15)).place(x=110, y=600)
        p_exp_enr = ttk.Combobox(roof, textvariable=p_exp, values=val).place(
            x=110, y=650, height=40, width=450)

        def feedsql():
            a = name_of.get()
            b = mobile_num.get()
            l = len(b)
            c = genderf.get()
            d = b_e.get()
            e = c_s.get()
            f = cll_s.get()
            g = p_exp.get()
            dfed = (a, c, b, d, e, f, g)
            conn.execute(('''INSERT INTO  FEEDBACKT('NAME','GENDER','MOBILE','BOOKINGEXPERIENCE','CUSTOMERSERVICE','CALLSERVICE','PAYMENTEXPERIENCE')VALUES(?,?,?,?,?,?,?)'''), dfed)
            conn.commit()
            messagebox.showinfo("SUCESS", "FEEDBACK SUBMITTED SUCESSFULLY")
            roof.destroy()
            # home()
        b_submit = tk.Button(roof, text="SUBMIT", font=("lucida calligraphy", 15), bg="Lightblue", command=feedsql).place(x=750, y=650, width=350, height=40)
        roof.mainloop()