#Librairies
import tkinter as tk
from tkinter import messagebox


#Tkinter app
app = tk.Tk()
app.title("MORPION")

#gameWindow

#Canvas


#Fonctions
def gameOpen():
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    global win
    global game

    game = tk.Toplevel()
    # customs window
    game.geometry("650x650")


    canvas = tk.Canvas(game, width=700, height=700, relief="raised")
    canvas.pack()


    # Vertical lines
    canvas.create_line(260, 300, 500, -100000, width=10, fill="black")  # vertical line 1
    canvas.create_line(370, 300, 500, -100000, width=10, fill="black")  # vertical line 2

    # Horizontal lines
    canvas.create_line(150, 102, 475, 102, width=10, fill="black")  # horizontal line 1
    canvas.create_line(150, 212, 475, 212, width=10, fill="black")  # horizontal line 2

    # Contour
    # Vertical lines
    canvas.create_line(150, 300, 255, -100000, width=10, fill="black")  # left
    canvas.create_line(480, 300, 255, -100000, width=10, fill="black")  # right
    # Horizontal lines
    canvas.create_line(150, 7, 480, 7, width=10, fill="black")  # top
    canvas.create_line(146, 305, 485, 305, width=10, fill="black")  # bottom

    #labels players
    label_player1 = tk.Label(game, text="Joueur 1: X")
    label_player1.place(x=0, y=200)

    label_player1 = tk.Label(game, text="Joueur 2: O")
    label_player1.place(x=500, y=200)

    # button

    # ligne 1
    b1 = tk.Button(game,text= " ", width=13, height=5, bg="#7bb1ef", command=lambda: startGame(b1))
    b1.place(x=155, y=12)

    b2 = tk.Button(game,text= " ", width=13, height=5,command=lambda: startGame(b2))
    b2.place(x=265, y=12)

    b3 = tk.Button(game,text= " ", width=13, height=5, bg="#7bb1ef", command=lambda: startGame(b3))
    b3.place(x=375, y=12)

    # ligne 2
    b4 = tk.Button(game,text= " ", width=13, height=6, command=lambda: startGame(b4))
    b4.place(x=155, y=107)

    b5 = tk.Button(game,text= " ", width=13, height=6, bg="#7bb1ef", command=lambda: startGame(b5))
    b5.place(x=265, y=107)

    b6 = tk.Button(game,text= " ", width=13, height=6, command=lambda: startGame(b6))
    b6.place(x=375, y=107)

    # ligne 3
    b7 = tk.Button(game, text= " ", width=13, height=5, bg="#7bb1ef", command=lambda: startGame(b7))
    b7.place(x=155, y=215)

    b8 = tk.Button(game,text= " ", width=13, height=5, command=lambda: startGame(b8))
    b8.place(x=265, y=215)

    b9 = tk.Button(game,text= " ", width=13, height=5, bg="#7bb1ef", command=lambda: startGame(b9))
    b9.place(x=375, y=215)

    #Label Winner

    win = tk.Label(game, text=" ")
    win.place(x=240, y=500)

def CloseBoard():
    game.destroy()

#global settings
y = "" #sign attribution
player1 = []
player2 = []
click = True

def startGame(b):
    import random
    global x,y
    global player1, player2
    global click
    global diffMode
    #global game
    #global win

    i = gamesNb
    print(gamesNb)

    if gamesNb == 0:
        print("end")
    else:
        playerStart = 1
        if playerStart == 1:
            #b1
            if b == b1:
                if b1["text"] == " " and click == True:
                    y = 'X'
                    b1.config(text=y)
                    click = False
                    #bot's strategy
                    if b7["text"] == 'X' and b4["text"] == " ":
                        y = 'O'
                        b4.config(text=y)
                        click = True
                    elif b2["text"] == 'X' and b3["text"] == " ":
                        y = 'O'
                        b3.config(text=y)
                        click = True
                    elif b3["text"] == 'X' and b2["text"] == " ":
                        y = 'O'
                        b2.config(text=y)
                        click = True
                    elif b4["text"] == 'X' and b7["text"] == " ":
                        y = 'O'
                        b7.config(text=y)
                        click = True
                    elif b5["text"] == 'X' and b9["text"] == " ":
                        y = 'O'
                        b9.config(text=y)
                        click = True
                    elif b9["text"] == 'X' and b5["text"] == " ":
                        y = 'O'
                        b5.config(text=y)
                        click = True
                    else:
                        y = 'O'
                        if b5["text"] == " ":
                            b5.config(text=y)
                            click = True
                        elif b9["text"] == " ":
                            b9.config(text=y)
                            click = True
                        elif b2["text"] == " ":
                            b2.config(text=y)
                            click = True
                        elif b3["text"] == " ":
                            b3.config(text=y)
                            click = True
                        elif b4["text"] == " ":
                            b4.config(text=y)
                            click = True
                        elif b7["text"] == " ":
                            b7.config(text=y)
                            click = True
                        elif b6["text"] == " ":
                            b6.config(text=y)
                            click = True
                        elif b8["text"] == " ":
                            b8.config(text=y)
                            click = True

            elif b == b2:
                #b2
                if b2["text"] == " " and click == True:
                    y = 'X'
                    b2.config(text=y)
                    click = False

                    #botStrat
                    if b1["text"] == 'X' and b3["text"] == " ":
                        y = 'O'
                        b3.config(text=y)
                        click = True
                    elif b3["text"] == 'X' and b1["text"] == " ":
                        y = 'O'
                        b1.config(text=y)
                        click = True
                    elif b5["text"] == 'X' and b8["text"] == " ":
                        y = 'O'
                        b8.config(text=y)
                        click = True
                    elif b8["text"] == 'X' and b5["text"] == " ":
                        y = 'O'
                        b5.config(text=y)
                        click = True
                    else:
                        y = 'O'
                        if b5["text"] == " ":
                            b5.config(text=y)
                            click = True
                        elif b1["text"] == " ":
                            b1.config(text=y)
                            click = True
                        elif b3["text"] == " ":
                            b3.config(text=y)
                            click = True
                        elif b5["text"] == " ":
                            b5.config(text=y)
                            click = True
                        elif b8["text"] == " ":
                            b8.config(text=y)
                            click = True
                        elif b4["text"] == " ":
                            b4.config(text=y)
                            click = True
                        elif b6["text"] == " ":
                            b6.config(text=y)
                            click = True
                        elif b7["text"] == " ":
                            b7.config(text=y)
                            click = True
                        elif b9["text"] == " ":
                            b9.config(text=y)
                            click = True

            elif b == b3:
                #b3
                if b3["text"] == " " and click == True:
                    y = 'X'
                    b3.config(text=y)
                    click = False

                    #botStrat
                    if b1["text"] == 'X' and b2["text"] == " ":
                        y = 'O'
                        b2.config(text=y)
                        click = True
                    elif b2["text"] == 'X' and b1["text"] == " ":
                        y = 'O'
                        b1.config(text=y)
                        click = True
                    elif b5["text"] == 'X' and b7["text"] == " ":
                        y = 'O'
                        b7.config(text=y)
                        click = True
                    elif b6["text"] == 'X' and b9["text"] == " ":
                        y = 'O'
                        b9.config(text=y)
                        click = True
                    elif b7["text"] == 'X' and b5["text"] == " ":
                        y = 'O'
                        b5.config(text=y)
                        click = True
                    elif b9["text"] == 'X' and b6["text"] == " ":
                        y = 'O'
                        b6.config(text=y)
                        click = True
                    else:
                        y = 'O'
                        if b5["text"] == " ":
                            b5.config(text=y)
                            click = True
                        elif b7["text"] == " ":
                            b7.config(text=y)
                            click = True
                        elif b9["text"] == " ":
                            b9.config(text=y)
                            click = True
                        elif b1["text"] == " ":
                            b1.config(text=y)
                            click = True
                        elif b6["text"] == " ":
                            b6.config(text=y)
                            click = True
                        elif b5["text"] == " ":
                            b5.config(text=y)
                            click = True
                        elif b2["text"] == " ":
                            b2.config(text=y)
                            click = True
                        elif b4["text"] == " ":
                            b4.config(text=y)
                            click = True
                        elif b8["text"] == " ":
                            b8.config(text=y)
                            click = True

            elif b == b4:
                #b4
                if b4["text"] == " " and click == True:
                    y = 'X'
                    b4.config(text=y)
                    click = False

                    #botStrat
                    if b1["text"] == 'X' and b7["text"] == " ":
                        y = 'O'
                        b7.config(text=y)
                        click = True
                    elif b5["text"] == 'X' and b6["text"] == " ":
                        y = 'O'
                        b6.config(text=y)
                        click = True
                    elif b6["text"] == 'X' and b5["text"] == " ":
                        y = 'O'
                        b5.config(text=y)
                        click = True
                    elif b7["text"] == 'X' and b1["text"] == " ":
                        y = 'O'
                        b1.config(text=y)
                        click = True

                    else:
                        y = 'O'
                        if b5["text"] == " ":
                            b5.config(text=y)
                            click = True
                        elif b1["text"] == " ":
                            b1.config(text=y)
                            click = True
                        elif b3["text"] == " ":
                            b3.config(text=y)
                            click = True
                        elif b7["text"] == " ":
                            b7.config(text=y)
                            click = True
                        elif b9["text"] == " ":
                            b9.config(text=y)
                            click = True
                        elif b6["text"] == " ":
                            b6.config(text=y)
                            click = True
                        elif b2["text"] == " ":
                            b2.config(text=y)
                            click = True
                        elif b8["text"] == " ":
                            b8.config(text=y)
                            click = True

            elif b == b5:
                #b5
                if b5["text"] == " " and click == True:
                    y = 'X'
                    b5.config(text=y)
                    click = False

                    #botStrat
                    if b1["text"] == 'X' and b9["text"] == " ":
                        y = 'O'
                        b9.config(text=y)
                        click = True
                    elif b3["text"] == 'X' and b7["text"] == " ":
                        y = 'O'
                        b7.config(text=y)
                        click = True
                    elif b2["text"] == 'X' and b8["text"] == " ":
                        y = 'O'
                        b8.config(text=y)
                        click = True
                    elif b4["text"] == 'X' and b6["text"] == " ":
                        y = 'O'
                        b6.config(text=y)
                        click = True
                    elif b6["text"] == 'X' and b4["text"] == " ":
                        y = 'O'
                        b4.config(text=y)
                        click = True
                    elif b7["text"] == 'X' and b3["text"] == " ":
                        y = 'O'
                        b3.config(text=y)
                        click = True
                    elif b8["text"] == 'X' and b2["text"] == " ":
                        y = 'O'
                        b2.config(text=y)
                        click = True
                    elif b9["text"] == 'X' and b1["text"] == " ":
                        y = 'O'
                        b1.config(text=y)
                        click = True
                    else:
                        y = 'O'
                        if b1["text"] == " ":
                            b1.config(text=y)
                            click = True
                        elif b2["text"] == " ":
                            b2.config(text=y)
                            click = True
                        elif b3["text"] == " ":
                            b3.config(text=y)
                            click = True
                        elif b4["text"] == " ":
                            b4.config(text=y)
                            click = True
                        elif b6["text"] == " ":
                            b6.config(text=y)
                            click = True
                        elif  b7["text"] == " ":
                            b7.config(text=y)
                            click = True
                        elif  b8["text"] == " ":
                            b8.config(text=y)
                            click = True
                        elif  b9["text"] == " ":
                            b9.config(text=y)
                            click = True

            elif b == b6:
                #b6
                if b6["text"] == " " and click == True:
                    y = 'X'
                    b6.config(text=y)
                    click = False

                    #botStrat
                    if b3["text"] == 'X' and b9["text"] == " ":
                        y = 'O'
                        b9.config(text=y)
                        click = True
                    elif b4["text"] == 'X' and b5["text"] == " ":
                        y = 'O'
                        b5.config(text=y)
                        click = True
                    elif b5["text"] == 'X' and b4["text"] == " ":
                        y = 'O'
                        b4.config(text=y)
                        click = True
                    elif b9["text"] == 'X' and b3["text"] == " ":
                        y = 'O'
                        b3.config(text=y)
                        click = True
                    else:
                        y = 'O'
                        if b5["text"] == " ":
                            b5.config(text=y)
                            click = True
                        elif b3["text"] == " ":
                            b3.config(text=y)
                            click = True
                        elif b7["text"] == " ":
                            b7.config(text=y)
                            click = True
                        elif b9["text"] == " ":
                            b9.config(text=y)
                            click = True
                        elif b4["text"] == " ":
                            b4.config(text=y)
                            click = True
                        elif b1["text"] == " ":
                            b1.config(text=y)
                            click = True
                        elif b2["text"] == " ":
                            b2.config(text=y)
                            click = True
                        elif b8["text"] == " ":
                            b8.config(text=y)
                            click = True

            elif b == b7:
                #b7
                if b7["text"] == " " and click == True:
                    y = 'X'
                    b7.config(text=y)
                    click = False

                    #botStrat
                    if b1["text"] == 'X' and b4["text"] == " ":
                        y = 'O'
                        b4.config(text=y)
                        click = True
                    elif b3["text"] == 'X' and b5["text"] == " ":
                        y = 'O'
                        b5.config(text=y)
                        click = True
                    elif b4["text"] == 'X' and b1["text"] == " ":
                        y = 'O'
                        b1.config(text=y)
                        click = True
                    elif b5["text"] == 'X' and b3["text"] == " ":
                        y = 'O'
                        b3.config(text=y)
                        click = True
                    elif b8["text"] == 'X' and b9["text"] == " ":
                        y = 'O'
                        b9.config(text=y)
                        click = True
                    elif b9["text"] == 'X' and b8["text"] == " ":
                        y = 'O'
                        b8.config(text=y)
                        click = True
                    else:
                        y = 'O'
                        if b5["text"] == " ":
                            b5.config(text=y)
                            click = True
                        elif  b1["text"] == " ":
                            b1.config(text=y)
                            click = True
                        elif b3["text"] == " ":
                            b3.config(text=y)
                            click = True
                        elif b9["text"] == " ":
                            b9.config(text=y)
                            click = True
                        elif b4["text"] == " ":
                            b4.config(text=y)
                            click = True
                        elif b8["text"] == " ":
                            b8.config(text=y)
                            click = True
                        elif b2["text"] == " ":
                            b2.config(text=y)
                            click = True
                        elif b6["text"] == " ":
                            b6.config(text=y)
                            click = True

            elif b == b8:
                #b8
                if b8["text"] == " " and click == True:
                    y = 'X'
                    b8.config(text=y)
                    click = False

                    #botStrat
                    if b2["text"] == 'X' and b5["text"] == " ":
                        y = 'O'
                        b5.config(text=y)
                        click = True
                    elif b5["text"] == 'X' and b2["text"] == " ":
                        y = 'O'
                        b2.config(text=y)
                        click = True
                    elif b7["text"] == 'X' and b9["text"] == " ":
                        y = 'O'
                        b9.config(text=y)
                        click = True
                    elif b9["text"] == 'X' and b7["text"] == " ":
                        y = 'O'
                        b7.config(text=y)
                        click = True
                    else:
                        y = 'O'
                        if b5["text"] == " ":
                            b5.config(text=y)
                            click = True
                        elif b7["text"] == " ":
                            b7.config(text=y)
                            click = True
                        elif b9["text"] == " ":
                            b9.config(text=y)
                            click = True
                        elif b1["text"] == " ":
                            b1.config(text=y)
                            click = True
                        elif b3["text"] == " ":
                            b3.config(text=y)
                            click = True
                        elif b2["text"] == " ":
                            b2.config(text=y)
                            click = True
                        elif b4["text"] == " ":
                            b4.config(text=y)
                            click = True
                        elif b6["text"] == " ":
                            b6.config(text=y)
                            click = True

            elif b == b9:
                #b9
                if b9["text"] == " " and click == True:
                    y = 'X'
                    b9.config(text=y)
                    click = False

                    #botStrat
                    if b1["text"] == 'X' and b5["text"] == " ":
                        y = 'O'
                        b5.config(text=y)
                        click = True
                    elif b3["text"] == 'X' and b6["text"] == " ":
                        y = 'O'
                        b6.config(text=y)
                        click = True
                    elif b5["text"] == 'X' and b1["text"] == " ":
                        y = 'O'
                        b1.config(text=y)
                        click = True
                    elif b7["text"] == 'X' and b8["text"] == " ":
                        y = 'O'
                        b8.config(text=y)
                        click = True
                    elif b8["text"] == 'X' and b7["text"] == " ":
                        y = 'O'
                        b7.config(text=y)
                        click = True
                    elif b6["text"] == 'X' and b3["text"] == " ":
                        y = 'O'
                        b6.config(text=y)
                        click = True
                    else:
                        y = 'O'
                        if b5["text"] == " ":
                            b5.config(text=y)
                            click = True
                        elif b1["text"] == " ":
                            b1.config(text=y)
                            click = True
                        elif b3["text"] == " ":
                            b3.config(text=y)
                            click = True
                        elif b6["text"] == " ":
                            b6.config(text=y)
                            click = True
                        elif b7["text"] == " ":
                            b7.config(text=y)
                            click = True
                        elif b8["text"] == " ":
                            b8.config(text=y)
                            click = True
                        elif b2["text"] == " ":
                            b2.config(text=y)
                            click = True
                        elif b4["text"] == " ":
                            b4.config(text=y)
                            click = True

            #winner check

            if (b1["text"] == 'X' and b2["text"] == 'X' and b3["text"] == 'X' or
                b1["text"] == 'X' and b5["text"] == 'X' and b9["text"] == 'X' or
                b1["text"] == 'X' and b4["text"] == 'X' and b7["text"] == 'X' or
                b3["text"] == 'X' and b5["text"] == 'X' and b7["text"] == 'X' or
                b3["text"] == 'X' and b6["text"] == 'X' and b9["text"] == 'X' or
                b7["text"] == 'X' and b8["text"] == 'X' and b9["text"] == 'X' or
                b4["text"] == 'X' and b5["text"] == 'X' and b6["text"] == 'X'):
                    win.config(text="GG, Tu m'impressionnes!")

            #Vertical Verif
            if b1["text"] == 'O' and b4["text"] == 'O' and b7["text"] == 'O':
                    b1.config(bg='red')
                    b4.config(bg='red')
                    b7.config(bg='red')
                    win.set(text="Dommage, Bot a gagne!")

            if b2["text"] == 'O' and b5["text"] == 'O' and b8["text"] == 'O':
                    b2.config(bg='red')
                    b5.config(bg='red')
                    b8.config(bg='red')
                    win.config(text="Dommage, Bot a gagne!")

            if b3["text"] == 'O' and b6["text"] == 'O' and b9["text"] == 'O':
                    b3.config(bg='red')
                    b6.config(bg='red')
                    b9.config(bg='red')
                    win.config(text="Dommage, Bot a gagne!")


            #Diagonal Verif
            if b1["text"] == 'O' and b5["text"] == 'O' and b9["text"] == 'O':
                    b1.config(bg='red')
                    b5.config(bg='red')
                    b9.config(bg='red')
                    win.config(text="Dommage Bot a gagne!")

            if b3["text"] == 'O' and b5["text"] == 'O' and b7["text"] == 'O':
                    b3.config(bg='red')
                    b5.config(bg='red')
                    b7.config(bg='red')
                    win.config(text="Dommage Bot a gagne!")



            #Horizontal verif
            if b1["text"] == 'O' and b2["text"] == 'O' and b3["text"] == 'O':
                b1.config(bg='red')
                b2.config(bg='red')
                b3.config(bg='red')
                win.config(text="Dommage, Bot a gagne!")

            if b4["text"] == 'O' and b5["text"] == 'O' and b6["text"] == 'O':
                    b4.config(bg='red')
                    b5.config(bg='red')
                    b6.config(bg='red')
                    win.config(text="Dommage, Bot a gagne!")

            if b7["text"] == 'O' and b8["text"] == 'O' and b9["text"] == 'O':
                    b7.config(bg='red')
                    b8.config(bg='red')
                    b9.config(bg='red')
                    win.config(text="Dommage, Bot a gagne!")

            #draw
            if (b1["text"] != " " and b2["text"] != " " and b3["text"] != " " and
                b4["text"] != " " and b5["text"] != " " and b6["text"] != " " and
                b7["text"] != " " and b8["text"] != " " and b9["text"] != " "):
                    win.config(text="egalite! Match fini en egalite")
                    i -= 1
                    CloseBoard()
                    click = True
                    gameOpen()





def initialisation():
    global gamesNb
    gamesNb = nb.get()
    diffMode = df.get()

    lDf = ["facile", "moyen", "difficile", "extreme"]
    if diffMode in lDf:
        if (gamesNb > 5):
            nb.set("No life! joue -!")
        elif (gamesNb > 0):
            gameOpen()
        else:
            nb.set("WHUT")
    else:
        df.set("error")


#EntryVariable
nb = tk.IntVar()
df = tk.StringVar()

#number of match
nbMatch = tk.Entry(app, textvariable=nb)
nb.set("1-5")
nbMatch.place(x=250, y=350)

#Difficulty status


difficulty = tk.Entry(app, textvariable=df)
df.set("facile-moyen-difficile-extreme")
difficulty.place(x=250, y=380)


#Labels


#resultatGame = tk.Label(app, text="SCORE: ")

#Bottom
matchValidate = tk.Button(app, text="Valider", command=initialisation)
matchValidate.place(x=380, y=347)


#tkinter customs
app.geometry("650x650")
app.iconbitmap("./image/icon.ico/")


#Tkinter loop
app.mainloop()