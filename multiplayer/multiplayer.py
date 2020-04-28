import tkinter as tk
import random
import PIL.Image, PIL.ImageTk

#game variable
click = True
canPlay = True

def restartGame():
    global canPlay
    listButton = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    for b in listButton:
        b["text"] = " "
        b.config(bg='white')
        canPlay = True

def checkWin():
    global click
    global canPlay
    # ===================================================

    # player1
    # Vertical Verif
    if b1["text"] == 'X' and b4["text"] == 'X' and b7["text"] == 'X':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        canPlay = False
        # ====

    if b2["text"] == 'X' and b5["text"] == 'X' and b8["text"] == 'X':
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        canPlay = False
        # ====

    if b3["text"] == 'X' and b6["text"] == 'X' and b9["text"] == 'X':
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        canPlay = False

    # Diagonal Verif
    if b1["text"] == 'X' and b5["text"] == 'X' and b9["text"] == 'X':
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        canPlay = False

    if b3["text"] == 'X' and b5["text"] == 'X' and b7["text"] == 'X':
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green')
        canPlay = False

    # Horizontal verif
    if b1["text"] == 'X' and b2["text"] == 'X' and b3["text"] == 'X':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        canPlay = False

    if b4["text"] == 'X' and b5["text"] == 'X' and b6["text"] == 'X':
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        canPlay = False

    if b7["text"] == 'X' and b8["text"] == 'X' and b9["text"] == 'X':
        b7.config(bg='green')
        b8.config(bg='green')
        b9.config(bg='green')
        canPlay = False

    # ====================================================
    # player2
    # Vertical Verif
    if b1["text"] == 'O' and b4["text"] == 'O' and b7["text"] == 'O':
        b1.config(bg='red')
        b4.config(bg='red')
        b7.config(bg='red')
        canPlay = False

    if b2["text"] == 'O' and b5["text"] == 'O' and b8["text"] == 'O':
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        canPlay = False

    if b3["text"] == 'O' and b6["text"] == 'O' and b9["text"] == 'O':
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')
        canPlay = False

    # Diagonal Verif
    if b1["text"] == 'O' and b5["text"] == 'O' and b9["text"] == 'O':
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        canPlay = False

    if b3["text"] == 'O' and b5["text"] == 'O' and b7["text"] == 'O':
        b3.config(bg='red')
        b5.config(bg='red')
        b7.config(bg='red')
        canPlay = False

    # Horizontal verif
    if b1["text"] == 'O' and b2["text"] == 'O' and b3["text"] == 'O':
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        canPlay = False

    if b4["text"] == 'O' and b5["text"] == 'O' and b6["text"] == 'O':
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        canPlay = False

    if b7["text"] == 'O' and b8["text"] == 'O' and b9["text"] == 'O':
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        canPlay = False

    # draw
    if (b1["text"] != " " and b2["text"] != " " and b3["text"] != " " and
            b4["text"] != " " and b5["text"] != " " and b6["text"] != " " and
            b7["text"] != " " and b8["text"] != " " and b9["text"] != " "):
        b1.config(bg='#0038ff')
        b4.config(bg='#0038ff')
        b7.config(bg='#0038ff')

        b2.config(bg='#ffffff')
        b5.config(bg='#ffffff')
        b8.config(bg='#ffffff')

        b3.config(bg='#fb0d01')
        b6.config(bg='#fb0d01')
        b9.config(bg='#fb0d01')
        canPlay = False

def player(b):
    global click
    global canPlay
    #Player 1

    while canPlay == True:
        if click == True:

            if b["text"] == " ":
                b["text"] = "X"
                print("case prise")
                click = False
                checkWin()
            else:
                print("choisis une autre case")
                return
        else:

            if b["text"] == " ":
                b["text"] = "O"
                print("case prise")
                click = True
                checkWin()
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
    # tkinter custom


    whoStart = random.randrange(1,3)

    if whoStart == 1:
        b1 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: player(b1))
        b1.place(x=155, y=12)

        b2 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: player(b2))
        b2.place(x=265, y=12)

        b3 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: player(b3))
        b3.place(x=375, y=12)

        # ligne 2
        b4 = tk.Button(multiApp, text=" ", width=13, height=6, bg="white", activebackground="black",
                       command=lambda: player(b4))
        b4.place(x=155, y=107)

        b5 = tk.Button(multiApp, text=" ", width=13, height=6, bg="white", activebackground="black",
                       command=lambda: player(b5))
        b5.place(x=265, y=107)

        b6 = tk.Button(multiApp, text=" ", width=13, height=6, bg="white", activebackground="black",
                       command=lambda: player(b6))
        b6.place(x=375, y=107)

        # ligne 3
        b7 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: player(b7))
        b7.place(x=155, y=215)

        b8 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: player(b8))
        b8.place(x=265, y=215)

        b9 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: player(b9))
        b9.place(x=375, y=215)

    else:
        click = False
        b1 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: player(b1))
        b1.place(x=155, y=12)

        b2 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: player(b2))
        b2.place(x=265, y=12)

        b3 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: player(b3))
        b3.place(x=375, y=12)

        # ligne 2
        b4 = tk.Button(multiApp, text=" ", width=13, height=6, bg="white", activebackground="black",
                       command=lambda: player(b4))
        b4.place(x=155, y=107)

        b5 = tk.Button(multiApp, text=" ", width=13, height=6, bg="white", activebackground="black",
                       command=lambda: player(b5))
        b5.place(x=265, y=107)

        b6 = tk.Button(multiApp, text=" ", width=13, height=6, bg="white", activebackground="black",
                       command=lambda: player(b6))
        b6.place(x=375, y=107)

        # ligne 3
        b7 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: player(b7))
        b7.place(x=155, y=215)

        b8 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: player(b8))
        b8.place(x=265, y=215)

        b9 = tk.Button(multiApp, text=" ", width=13, height=5, bg="white", activebackground="black",
                       command=lambda: player(b9))
        b9.place(x=375, y=215)

    #button
    replay = tk.Button(multiApp, text="Rejouer", command=restartGame)
    replay.place(x="20", y="300")

    img = PIL.ImageTk.PhotoImage(PIL.Image.open("blaze.png"))
    background = tk.Label(multiApp, image=img)
    background.pack(side="bottom", fill="both", expand="yes")

    multiApp.mainloop()

