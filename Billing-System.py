from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_WinterMelon.delete(0, END)
    entry_Okinawa.delete(0, END)
    entry_Taro.delete(0, END)
    entry_Matcha.delete(0, END)
    entry_Chocolate.delete(0, END)
    entry_Hokkaido.delete(0, END)

def Total():
    try:a1 = int(WinterMelon.get())
    except: a1 = 0
    try:a2 = int(Okinawa.get())
    except: a2 = 0
    try:a3 = int(Taro.get())
    except: a3 = 0
    try:a4 = int(Matcha.get())
    except: a4 = 0
    try:a5 = int(Chocolate.get())
    except: a5 = 0
    try:a6 = int(Hokkaido.get())
    except: a6 = 0

    #COST
    c1 = 150 * a1
    c2 = 170 * a2
    c3 = 180 * a3
    c4 = 120 * a4
    c5 = 160 * a5
    c6 = 130 * a6
    

    lbl_total = Label(f2, font = ("georgia", 18, 'bold'), text = "TOTAL", width = 19, fg = "lightyellow", bg = "black")
    lbl_total.place(x = 0, y = 60)

    entry_total = Entry(f2, font = ("aria", 20, 'bold'), textvariable = Total_bill, bd = 6, width = 15, bg = "lightgreen")
    entry_total.place(x = 30, y = 100)

    totalcost = c1 + c2 + c3 + c4 + c5 + c6
    string_bill = "Php " + str('%.2f' %totalcost)
    Total_bill.set(string_bill)

Label(text = "BILL MANAGEMENT", bg = "black", fg = "white", font = ("calibri", 33), width = "300", height = "2").pack()

#MENU CARD
f = Frame(root, bg = "lightgreen", highlightbackground = "black", highlightthickness = 1, width = 300, height = 370)
f.place(x = 10, y = 120)

Label(f, text = "Menu", font = ("georgia", 30, "bold"), fg = "black", bg = "lightgreen").place(x = 85, y = 10)

Label(f, font = ("georgia", 8, 'bold'), text = "Winter Melon---Php150.00", fg = "black", bg = "lightgreen").place(x = 10, y = 60)
Label(f, font = ("georgia", 8, 'bold'), text = "Okinawa---Php170.00", fg = "black", bg = "lightgreen").place(x = 10, y = 90)
Label(f, font = ("georgia", 8, 'bold'), text = "Taro---Php180.00", fg = "black", bg = "lightgreen").place(x = 10, y = 120)
Label(f, font = ("georgia", 8, 'bold'), text = "Matcha---Php120.00", fg = "black", bg = "lightgreen").place(x = 10, y = 150)
Label(f, font = ("georgia", 8, 'bold'), text = "Chocolate---Php160.00", fg = "black", bg = "lightgreen").place(x = 10, y = 180)
Label(f, font = ("georgia", 8, 'bold'), text = "Hokkaido---Php130.00", fg = "black", bg = "lightgreen").place(x = 10, y = 210)

#ENTRY WORK
f1 = Frame(root, bd = 5, height = 370, width = 300)
f1.place(x = 322, y = 124)

WinterMelon = StringVar()
Okinawa = StringVar()
Taro = StringVar()
Matcha = StringVar()
Chocolate = StringVar()
Hokkaido = StringVar()
Total_bill = StringVar()

#LABEL
lbl_WinterMelon = Label(f1, font = ("aria", 20, 'bold'), text = "Wintermelon", width = 12, fg = "blue4")
lbl_WinterMelon.grid(row = 1, column = 0)
lbl_Okinawa = Label(f1, font = ("aria", 20, 'bold'), text = "Okinawa", width = 12, fg = "blue4")
lbl_Okinawa.grid(row = 2, column = 0)
lbl_Taro = Label(f1, font = ("aria", 20, 'bold'), text = "Taro ", width = 12, fg = "blue4")
lbl_Taro.grid(row = 3, column = 0)
lbl_Matcha = Label(f1, font = ("aria", 20, 'bold'), text = "Matcha ", width = 12, fg = "blue4")
lbl_Matcha.grid(row = 4, column = 0)
lbl_Chocolate = Label(f1, font = ("aria", 20, 'bold'), text = "Chocolate", width = 12, fg = "blue4")
lbl_Chocolate.grid(row = 5, column = 0)
lbl_Hokkaido = Label(f1, font = ("aria", 20, 'bold'), text = "Hokkaido", width = 12, fg = "blue4")
lbl_Hokkaido.grid(row = 6, column = 0)
spacing = Label(f1, font = ("aria", 20, 'bold'), text = "", width = 12, fg = "blue4")
spacing.grid(row = 7, column = 0)
spacing = Label(f1, font = ("aria", 20, 'bold'), text = "", width = 12, fg = "blue4")
spacing.grid(row = 8, column = 0)


#BILL
f2 = Frame(root, bg = "lightyellow", highlightbackground = "black", highlightthickness = 1, width = 300, height = 370)
f2.place(x = 690, y = 120)

Bill = Label(f2, text = "Bill", font = ("georgia", 30, 'bold'), bg = "lightyellow")
Bill.place(x = 110, y = 13)

#ENTRY
entry_WinterMelon = Entry(f1, font = ("aria", 20, 'bold'), textvariable = WinterMelon, bd = 6, width = 8, bg = "lightpink")
entry_WinterMelon.grid(row = 1, column = 1)
entry_Okinawa = Entry(f1, font = ("aria", 20, 'bold'), textvariable = Okinawa, bd = 6, width = 8, bg = "lightpink")
entry_Okinawa.grid(row = 2, column = 1)
entry_Taro = Entry(f1, font = ("aria", 20, 'bold'), textvariable = Taro, bd = 6, width = 8, bg = "lightpink")
entry_Taro.grid(row = 3, column = 1)
entry_Matcha = Entry(f1, font = ("aria", 20, 'bold'), textvariable = Matcha, bd = 6, width = 8, bg = "lightpink")
entry_Matcha.grid(row = 4, column = 1)
entry_Chocolate = Entry(f1, font = ("aria", 20, 'bold'), textvariable = Chocolate, bd = 6, width = 8, bg = "lightpink")
entry_Chocolate.grid(row = 5, column = 1)
entry_Hokkaido = Entry(f1, font = ("aria", 20, 'bold'), textvariable = Hokkaido, bd = 6, width = 8, bg = "lightpink")
entry_Hokkaido.grid(row = 6, column = 1)

#BUTTONS
btn_reset = Button(f1, bd = 5, fg = "black", bg = "lightblue", font = ("ariel", 16, 'bold'), width = 10, text = "Reset", command = Reset)
btn_reset.place(x = 196, y = 300)

btn_total = Button(f1, bd = 5, fg ="black", bg = "lightblue", font = ("ariel", 16, 'bold'), width = 10, text = "Total", command = Total)
btn_total.place(x = 0, y = 300)


root.mainloop()