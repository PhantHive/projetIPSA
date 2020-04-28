import tkinter as tk
import random
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
msg = s.recv(1024)
print(msg.decode("utf-8"))

#game variable
click = True


def startMulti(b):
    global click
    listButton = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    #Player 1
    for b in listButton:
        if b["text"] == " " and click == True:
            b["text"] = "X"
            print("case prise")
            click = False
        else:
            print("choisis une autre case")
            return

    #Player 2
    for b in listButton:
        if b["text"] == " " and click == False:
            b["text"] = "O"
            print("case prise")
            click = True
        else:
            print("choisis une autre case")
            return



def multi():
    global click
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9

    multiApp = tk.Tk()
    multiApp.geometry("500x500")

    whoStart = random.randrange(1,3)

    if whoStart == 1:
        b1 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: startMulti(b1))
        b1.place(x=155, y=12)

        b2 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: startMulti(b2))
        b2.place(x=265, y=12)

        b3 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: startMulti(b3))
        b3.place(x=375, y=12)

        # ligne 2
        b4 = tk.Button(multiApp, text=" ", width=13, height=6, bg="white", activebackground="black",
                       command=lambda: startMulti(b4))
        b4.place(x=155, y=107)

        b5 = tk.Button(multiApp, text=" ", width=13, height=6, bg="white", activebackground="black",
                       command=lambda: startMulti(b5))
        b5.place(x=265, y=107)

        b6 = tk.Button(multiApp, text=" ", width=13, height=6, bg="white", activebackground="black",
                       command=lambda: startMulti(b6))
        b6.place(x=375, y=107)

        # ligne 3
        b7 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: startMulti(b7))
        b7.place(x=155, y=215)

        b8 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: startMulti(b8))
        b8.place(x=265, y=215)

        b9 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: startMulti(b9))
        b9.place(x=375, y=215)

    else:
        click = False
        b1 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: startMulti(b1))
        b1.place(x=155, y=12)

        b2 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: startMulti(b2))
        b2.place(x=265, y=12)

        b3 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: startMulti(b3))
        b3.place(x=375, y=12)

        # ligne 2
        b4 = tk.Button(multiApp, text=" ", width=13, height=6, bg="white", activebackground="black",
                       command=lambda: startMulti(b4))
        b4.place(x=155, y=107)

        b5 = tk.Button(multiApp, text=" ", width=13, height=6, bg="white", activebackground="black",
                       command=lambda: startMulti(b5))
        b5.place(x=265, y=107)

        b6 = tk.Button(multiApp, text=" ", width=13, height=6, bg="white", activebackground="black",
                       command=lambda: startMulti(b6))
        b6.place(x=375, y=107)

        # ligne 3
        b7 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: startMulti(b7))
        b7.place(x=155, y=215)

        b8 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: startMulti(b8))
        b8.place(x=265, y=215)

        b9 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: startMulti(b9))
        b9.place(x=375, y=215)

    multiApp.mainloop()
