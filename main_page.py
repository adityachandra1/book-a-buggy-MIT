import sqlite3
import tkinter as tk
from tkinter import *

from string import *
from tkinter import messagebox, ttk
import webbrowser
import sv_ttk

from about_page import *
from cancel_page import *
from feedback_page import *
from services_page import *
from show_booking import *
from payment_page import *

conn = sqlite3.Connection("example.db")


conn.execute('''CREATE TABLE IF NOT EXISTS TEST3(
             ORIGIN TEXT NOT NULL,
             DEST TEXT NOT NULL,
             NAME TEXT NOT NULL,
             DAY TEXT,
             MONTH TEXT,
             YEAR TEXT,
             GENDER TEXT,
             TIMING TEXT,
             MOBILE TEXT NOT NULL,
             PAIDTHROUGH TEXT NOT NULL,
             AMOUNTPAID TEXT NOT NULL);''')

conn.execute('''CREATE TABLE IF NOT EXISTS FEEDBACKT(
             NAME TEXT NOT NULL,
             GENDER TEXT,
             MOBILE TEXT NOT NULL,
             BOOKINGEXPERIENCE TEXT NOT NULL,
             CUSTOMERSERVICE TEXT NOT NULL,
             CALLSERVICE  TEXT NOT NULL,
             PAYMENTEXPERIENCE TEXT NOT NULL);''')


def home():
    conn = sqlite3.Connection("example.db")
    root = Tk()
    sv_ttk.set_theme("dark")
    root.geometry('1200x1200')
    root.title("Book-A-Buggy")

    swidth = root.winfo_screenwidth()
    sheight = root.winfo_screenheight()

    # fr = tk.Frame(root, image=background_image, width=swidth, height=sheight).pack()
    bon = Label(root, text="Book-A-Buggy", font=("lucida calligraphy", 40, "bold"), bd=0).place(x=400, y=10)
    label_me = tk.Label(root).place(x=0, y=80, width=swidth, height=70)

    about_button = tk.Button(root, text="About", bd=0, fg='white', font=("Heveltica", 15), command=about)
    about_button.place(x=10, y=100, width=150, height=40)

    services_button = tk.Button(root, text="Services", bd=0, fg='white', font=("Heveltica", 15), command=service)
    services_button.place(x=150, y=100, width=150, height=40)

    feedback_button = tk.Button(root, text="Feedback", bd=0, fg='white', font=("Heveltica", 15), command=feed)
    feedback_button.place(x=290, y=100, width=150, height=40)

    show_booking = tk.Button(root, text="Show Bookings", bd=0, fg='white', font=("Heveltica", 15), command=showbok)
    show_booking.place(x=440, y=100, width=150, height=40)

    cancel_button = tk.Button(root, text="Cancel", bd=0, fg='white', font=("Heveltica", 15), command=cancel)
    cancel_button.place(x=590, y=100, width=150, height=40)

    book_frame = tk.Frame(root, bg="grey", width="1100",height="700").place(x=50, y=200)
    book_head_label = tk.Message(root, text="Book Your Tickets", width="500", bd=0, bg="grey", font=("Heveltica", 30)).place(x=420, y=220)

    from_input = StringVar()
    to_input = StringVar()
    name_input = StringVar()
    gender_input = StringVar()
    mobile_input = StringVar()
    year_input = StringVar()
    month_input = StringVar()
    day_input = StringVar()
    time_input = StringVar()

    label_from = tk.Label(root, text="From", font=("Heveltica", 15), bg='grey').place(x=110, y=350)
    e1 = ttk.Combobox(root, textvariable=from_input, values=['Block-14', 'AB-5', 'AB-3', 'KMC', 'Student Plaza', 'MIT-Gate-1'])
    e1.place(x=110, y=400, height="40", width="450")

    label_to = tk.Label(root, text="To", font=("Heveltica",15), bg='grey').place(x=110, y=450)
    e2 = ttk.Combobox(root, values=['Block-14', 'AB-5', 'AB-3', 'KMC', 'Student Plaza','MIT-Gate-1'], textvariable=to_input)
    e2.place(x=110, y=500, height="40", width="450")

    year = list(range(2022, 2030))
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    day = list(range(1, 31))

    label_dat = tk.Label(root, text="Year", font=("Heveltica", 10)).place(x=110, y=580, width=60, height=40)
    e3 = ttk.Combobox(root, values=year, textvariable=year_input).place(x=180, y=580, width=60, height=40)

    label_dat = tk.Label(root, text="Month", font=("Heveltica", 10)).place(x=280, y=580, width=60, height=40)
    e4 = ttk.Combobox(root, values=month, textvariable=month_input).place(x=340, y=580, width=60, height=40)

    label_dat = tk.Label(root, text="Day", font=("Heveltica", 10)).place(x=440, y=580, width=60, height=40)
    e5 = ttk.Combobox(root, values=day, textvariable=day_input).place(x=500, y=580, width=60, height=40)

    label_nameof = tk.Label(root, text="Name of the passenger:", font=("Heveltica", 15), bg='grey').place(x=700, y=350)
    e_name = tk.Entry(root, textvariable=name_input).place(x=700, y=400, width=420, height=40)

    label_gender = tk.Label(root, text='Gender', bg='grey',font=("Heveltica", 15)).place(x=700, y=450)
    e_gender = ttk.Combobox(root, textvariable=gender_input, values=['Male', 'Female', 'Others']).place(x=700, y=500, height=40, width=420)

    label_mob = tk.Label(root, text="Mobile Number : ", font=("Heveltica", 15), bg='grey').place(x=700, y=550)
    e_mob = tk.Entry(root, textvariable=mobile_input).place(x=700, y=600, width=420, height=40)

    label_timing = tk.Label(root, text="Choose the Time",bg="grey", font=("Heveltica", 15)).place(x=110, y=650,)
    timing_a = ttk.Combobox(root, values=['12:00 am', '6:00 am', '9:00 am', '12:00 pm', '3:00 pm','6:00 pm', '9:00 pm', ], textvariable=time_input)
    timing_a.place(x=110, y=700, height=40, width=450)


    def pay():
        sv_ttk.set_theme("dark")
        a = from_input.get()
        b = to_input.get()
        c = name_input.get()
        d = gender_input.get()
        e = mobile_input.get()
        le = len(e)
        f = year_input.get()
        g = month_input.get()
        h = day_input.get()
        i = time_input.get()
        if a == '' or b == '' or c == '' or d == '' or e == '' or f == '' or g == '' or h == '' or i == '':
            messagebox.showinfo(
                "Warning!", "Please Enter the required Fields !")
            home()
        elif (a == b):
            messagebox.showinfo("Destination and Arrival cannot be the same!")
            home()
        elif (le > 10 or le < 10):
            messagebox.showinfo("Warning ", "Invalid Number")
        else:
            if a == "Block-14":
                if b == "NEWDELHI":
                    price = 1000
                elif b == "AB-3":
                    price = 1200
                elif b == "KMC":
                    price = 1300
                elif b == "Student Plaza":
                    price = 1400
                else:
                    price = 1500
            elif a == "AB-5":
                if b == "Block-14":
                    price = 1000
                elif b == "AB-3":
                    price = 1200
                elif b == "KMC":
                    price = 1300
                elif b == "Student Plaza":
                    price = 1400
                else:
                    price = 1500
            elif a == "KMC":
                if b == "Block-14":
                    price = 1000
                elif b == "AB-3":
                    price = 1200
                elif b == "AB-5":
                    price = 1300
                elif b == "Student Plaza":
                    price = 1400
                else:
                    price = 1500
            elif a == "Student Plaza":
                if b == "Block-14":
                    price = 1000
                elif b == "AB-3":
                    price = 1200
                elif b == "AB-5":
                    price = 1300
                elif b == "KMC":
                    price = 1400
                else:
                    price = 1500
            elif a == "AB-3":
                if b == "Block-14":
                    price = 1000
                elif b == "AB-3":
                    price = 1200
                elif b == "AB-5":
                    price = 1300
                elif b == "Student Plaza":
                    price = 1400
                else:
                    price = 1500
            else:
                if b == "AB-3":
                    price = 2000
                elif b == "Block-14":
                    price = 1000
                elif b == "AB-3":
                    price = 1200
                elif b == "AB-5":
                    price = 1300
                else:
                    price = 1500

            roop = tk.Tk()

            roop.title("Book-A-Buggy")
            swidth = roop.winfo_screenwidth()
            sheight = roop.winfo_screenheight()
            fr = tk.Frame(roop, bg="#222324", width=swidth,height=sheight).pack()
            bon = Label(roop, text="Book-A-Buggy", font=("lucida calligraphy", 40, "bold"), bg="#222324", fg = "White", bd=0).place(x=10, y=10)
            come = Label(roop, text="", font=("lucida calligraphy", 25), bg="#222324", fg = "White").place(x=500, y=20)
            label_me = tk.Label(roop, bg="darkgrey").place(x=0, y=80, width=swidth, height=70)
            but_home = tk.Button(roop, text="HOME", bg="darkgrey", bd=0, fg="white", font=("lucida calligraphy", 25)).place(x=650, y=80)
            frame_pay = tk.Frame(roop, bg="grey").place( x=300, y=200, width=950, height=600)
            label_heading = tk.Label(roop, bg='grey', font=("lucida calligraphy", 20), text="PAYMENT GATEWAY").place(x=600, y=250)

            def paywith():
                p = "CASH"
                dat = (a, b, c, h, g, f, d, i, e, p, price)
                date = h+'/'+g+'/'+f
                conn.execute(
                    '''INSERT INTO TEST3('ORIGIN','DEST','NAME','DAY','MONTH','YEAR','GENDER','TIMING','MOBILE','PAIDTHROUGH','AMOUNTPAID')VALUES(?,?,?,?,?,?,?,?,?,?,?)''', dat)
                conn.commit()

                roott = tk.Tk()
                sv_ttk.set_theme("dark")
                roop.destroy()
                roott.configure(bg='#222324')
                roott.title("Book-A-Buggy")
                swidth = roott.winfo_screenwidth()
                sheight = roott.winfo_screenheight()
                payFont = ("lucida calligraphy", 20, "bold")
                fr = tk.Frame(roott, bg="#222324", width=swidth,height=sheight).pack()
                bon = Label(roott, text="Book-A-Buggy", font=("lucida calligraphy", 40, "bold"), bg="#222324", fg = "White", bd=0).place(x=10, y=10)
                come = Label(roott, text="", font=("lucida calligraphy", 25), bg="#222324", fg = "White").place(x=500, y=20)
                frr_tk = tk.Frame(roott, bg="#161617").place(x=150, y=100, width="1200", height="600")
                label_from = tk.Label(roott, text="BOOKING DETAILS ", font=("lucida calligraphy", 30, "bold"), bg = "#161617", fg = "White").place(x=500, y=150)
                label_from = tk.Label(roott, text="FROM :  ", font=payFont, bd=0, bg = "#161617", fg = "White").place(x=160, y=250)
                label_from1 = tk.Label(roott, text=a, font=payFont, bd=0, bg = "#161617", fg = "White").place(x=350, y=250)
                label_to = tk.Label(roott, text="TO : ", font=payFont, bd=0, bg = "#161617", fg = "White").place(x=900, y=250)
                label_to1 = tk.Label(roott, text=b, font=payFont, bd=0, bg = "#161617", fg = "White").place(x=1100, y=250)
                label_tot = tk.Label(roott, text="TRAVELLING DATE  : ", font=payFont, bd=0, bg = "#161617", fg = "White").place(x=160, y=350)
                label_tod = tk.Label(roott, text=date, font=payFont, bd=0, bg = "#161617", fg = "White").place(x=600, y=350)
                label_to3 = tk.Label(roott, text="AMOUNT PAID    :", font=payFont, bd=0, bg = "#161617", fg = "White").place(x=160, y=450)
                label_to2 = tk.Label(roott, text=price, font=payFont, bd=0, bg = "#161617", fg = "White").place(x=600, y=450)
                label_stb = tk.Label(roott, text="BOOKING STATUS :", font=payFont,bg = "#161617", fg = "White").place(x=150, y=530)
                label_s = tk.Label(roott, text="CONFIRMED", font=payFont,bg = "#161617", fg = "White").place(x=500, y=530)

                def lahome():
                    roott.destroy()
                    home()
                but_return = tk.Button(roott, text="home ", font=(
                    "Heveltica", 15), bg="Lightblue", command=lahome).place(x=500, y=600, width=350, height=40)

                roott.mainloop()
            bau_paytm = tk.Button(roop, text="PAY WITH THE CASH", font=(
                "lucida calligraphy", 20), bg="lightblue", command=paywith).place(x=600, y=400)
            new = 1
            url = "https://p-y.tX/UC-jmiq"

            def callback(url):
                webbrowser.open_new(url)
            link1 = tk.Label(roop, text="PAY WITH DEBIT/CREDIT/INTERNET BANKING",
                             bg="lightblue", cursor="hand2", font=("lucida calligraphy", 20))
            link1.place(x=460, y=500)
            link1.bind(
                "<Button-1>", lambda e: callback("https://p-y.tm/UC-jmiq"))
            roop.mainloop()

    submit_button = tk.Button(root, text="Proceed ", font=("Heveltica", 18, "bold"), bg="Lightgreen", command=pay).place(x=700, y=700, width=420, height=40)
    root.mainloop()


home()
