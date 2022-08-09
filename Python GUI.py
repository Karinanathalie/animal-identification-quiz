import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=600, bg="#FF7F64")
canvas.pack()

# introduction
frame = tk.Frame(root, bg="#F25B39")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


def onclick():
    hello.destroy()
    welcome.destroy()
    start.destroy()
    frame.destroy()
    action1()


start = tk.Button(frame, text="Start", padx=1, pady=1, fg="white", bg="#263D42", height=4, width=30, font="Sans 16",
                  command=onclick)
start.pack(side=BOTTOM, pady=(10, 60))

hello = tk.Label(frame, text="Hello!", fg="white", bg="#F25B39", font="Times 40 bold", pady=6)
hello.pack(pady=(60, 30))

welcome = tk.Label(frame, text="Ready to identify your animal?", fg="white", bg="#F25B39", font="Times 25", pady=6)
welcome.pack(pady=(0, 10))

# skintype
v = tk.IntVar()

skin = [
    ("Scales made out of bony plates", 1),
    ("Moist skin", 2),
    ("Scales made out of Keratin", 3),
    ("Feathers", 4),
    ("Hair", 5),
]


def action1():
    frame1.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    labelskin.pack(side=TOP, padx=20, pady=(40, 20))
    for text, value in skin:
        Radiobutton(frame1, text=text, indicatoron=0, variable=v, value=value, fg="black", bg="#F25B39",
                    font="Times 15", width=50).pack(side=TOP, ipady=5, anchor=tk.W)
    next.pack(side=BOTTOM, pady=(10, 30))


def action1_end():
    labelskin.destroy()
    next.destroy()
    frame1.destroy()
    action2()


frame1 = tk.Frame(root, bg="#F25B39")

labelskin = tk.Label(frame1, text="Choose the characteristics of its body:", fg="black", bg="#F25B39",
                     font="Times 20 bold", pady=6)

next = tk.Button(frame1, text="Next", padx=1, pady=1, fg="white", bg="#263D42", height=2, width=10, font="Sans 10",
                 command=action1_end)

# reproductiontype
v2 = tk.IntVar()

reproduction = {"Usually External in most species": 1,
                "Always External (Jelly-covered eggs)": 2,
                "Internal (Soft Eggs)": 3,
                "Internal (Hard Eggs)": 4,
                "Internal (Live Births)": 5
                }


def action2():
    frame2.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    labelrepro.pack(side=TOP, padx=20, pady=(40, 20))
    for (text, value) in reproduction.items():
        Radiobutton(frame2, text=text, indicatoron=0, variable=v2, value=value, fg="black", bg="#F25B39",
                    font="Times 15", width=50).pack(side=TOP, ipady=5, anchor=tk.W)
    next2.pack(side=BOTTOM, pady=(10, 30))


def action2_end():
    labelrepro.destroy()
    next2.destroy()
    frame2.destroy()
    action3()


frame2 = tk.Frame(root, bg="#F25B39")

labelrepro = tk.Label(frame2, text="Choose the characteristics of its reproduction:", fg="black", bg="#F25B39",
                      font="Times 16 bold", pady=6)

next2 = tk.Button(frame2, text="Next", padx=1, pady=1, fg="white", bg="#263D42", height=2, width=10, font="Sans 10",
                  command=action2_end)

# breathingtype
v3 = tk.IntVar()

breath = {"Gills": 1,
          "Simple lungs (and via skin)": 2,
          "Lungs with extensive folding": 3,
          "Lungs with bronchial tubes": 4,
          "Lungs with alveoli": 5
          }


def action3():
    frame3.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    labelbreath.pack(side=TOP, padx=20, pady=(40, 20))
    for (text, value) in breath.items():
        Radiobutton(frame3, text=text, indicatoron=0, variable=v3, value=value, fg="black", bg="#F25B39",
                    font="Times 15", width=50).pack(side=TOP, ipady=5, anchor=tk.W)
    next3.pack(side=BOTTOM, pady=(10, 30))


def action3_end():
    labelbreath.destroy()
    next3.destroy()
    frame3.destroy()
    action4()


frame3 = tk.Frame(root, bg="#F25B39")

labelbreath = tk.Label(frame3, text="Choose the characteristics of how its breathing:", fg="black", bg="#F25B39",
                       font="Times 16 bold", pady=6)

next3 = tk.Button(frame3, text="Next", padx=1, pady=1, fg="white", bg="#263D42", height=2, width=10, font="Sans 10",
                  command=action3_end)

# movementtype
v4 = tk.IntVar()

temp = {"Fins": 1,
        "4 Limbs and Back Feet for Swimming": 2,
        "Four Legs (expect for snakes)": 3,
        "Wings and 2 Legs": 4,
        "Four Limbs": 5
        }


def action4():
    frame4.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    labeltemp.pack(side=TOP, padx=20, pady=(40, 20))
    for (text, value) in temp.items():
        Radiobutton(frame4, text=text, indicatoron=0, variable=v4, value=value, fg="black", bg="#F25B39",
                    font="Times 15", width=50).pack(side=TOP, ipady=5, anchor=tk.W)
    next4.pack(side=BOTTOM, pady=(10, 30))


def action4_end():
    labeltemp.destroy()
    next4.destroy()
    frame4.destroy()
    action5()


frame4 = tk.Frame(root, bg="#F25B39")

labeltemp = tk.Label(frame4, text="Choose the characteristics of how its move:", fg="black", bg="#F25B39",
                     font="Times 16 bold", pady=6)

next4 = tk.Button(frame4, text="Next", padx=1, pady=1, fg="white", bg="#263D42", height=2, width=10, font="Sans 10",
                  command=action4_end)

# othertype
v5 = tk.IntVar()

other = {"Have a swim bladder": 1,
         "Larval state in water, adult on land": 2,
         "Simple teeth with no living tissue": 3,
         "Have wings and beaks with no teeth": 4,
         "Feed young with milk from mammary gland": 5
         }


def action5():
    frame5.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    labelother.pack(side=TOP, padx=20, pady=(40, 20))
    for (text, value) in other.items():
        Radiobutton(frame5, text=text, indicatoron=0, variable=v5, value=value, fg="black", bg="#F25B39",
                    font="Times 15", width=50).pack(side=TOP, ipady=5, anchor=tk.W)
    next5.pack(side=BOTTOM, pady=(10, 30))


def action5_end():
    labelother.destroy()
    next5.destroy()
    frame5.destroy()
    outro()


frame5 = tk.Frame(root, bg="#F25B39")

labelother = tk.Label(frame5, text="Choose the characteristics of how its breathing:", fg="black", bg="#F25B39",
                      font="Times 16 bold", pady=6)

next5 = tk.Button(frame5, text="Next", padx=1, pady=1, fg="white", bg="#263D42", height=2, width=10, font="Sans 10",
                  command=action5_end)

# result
frame6 = tk.Frame(root, bg="#F25B39")


def final():
    if (v.get(), v2.get(), v3.get(), v4.get(), v5.get()) == (1, 1, 1, 1, 1):
        Label(frame6, text="It is a Fish!", fg="black", bg="#F25B39", font="Times 20 bold", pady=6).pack(side=TOP,
                                                                                                         padx=20,
                                                                                                         pady=(40, 20))
    elif (v.get(), v2.get(), v3.get(), v4.get(), v5.get()) == (2, 2, 2, 2, 2):
        Label(frame6, text="It is a Amphibi!", fg="black", bg="#F25B39", font="Times 20 bold", pady=6).pack(side=TOP,
                                                                                                            padx=20,
                                                                                                            pady=
                                                                                                            (40, 20))
    elif (v.get(), v2.get(), v3.get(), v4.get(), v5.get()) == (3, 3, 3, 3, 3):
        Label(frame6, text="It is a Reptile!", fg="black", bg="#F25B39", font="Times 20 bold", pady=6).pack(side=TOP,
                                                                                                            padx=20,
                                                                                                            pady=
                                                                                                            (40, 20))
    elif (v.get(), v2.get(), v3.get(), v4.get(), v5.get()) == (4, 4, 4, 4, 4):
        Label(frame6, text="It is a Bird!", fg="black", bg="#F25B39", font="Times 20 bold", pady=6).pack(side=TOP,
                                                                                                         padx=20,
                                                                                                         pady=(40, 20))
    elif (v.get(), v2.get(), v3.get(), v4.get(), v5.get()) == (5, 5, 5, 5, 5):
        Label(frame6, text="It is a Mammal!", fg="black", bg="#F25B39", font="Times 20 bold", pady=6).pack(side=TOP,
                                                                                                           padx=20,
                                                                                                           pady=
                                                                                                           (40, 20))
    else:
        Label(frame6, text="Animals can't be detected. Try again!", fg="black", bg="#F25B39", font="Times 20 bold",
              pady=6).pack(side=TOP, padx=20, pady=(40, 20))


def outro():
    frame6.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    final()
    quit.pack(side=BOTTOM, pady=(10, 30))


def exit():
    response = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if response == 1:
        root.quit()


quit = tk.Button(frame6, text="Exit", padx=1, pady=1, fg="white", bg="#263D42", height=3, width=20, font="Sans 16",
                 command=exit)

root.mainloop()
