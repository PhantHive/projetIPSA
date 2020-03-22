#Librairies
import tkinter as tk
import time
import PIL.Image, PIL.ImageTk
import random
import sys
import json

from tkinter import messagebox

#Tkinter app
app = tk.Tk()
app.title("MORPION")

#Login Function
def connectVerif():
    nm = collectNameLogin.get()
    ps = collectPassLogin.get()
    playerShow.get()
    userData = open('./login/login.json', 'r')
    jsonData = json.load(userData)

    for dic in jsonData:
        if nm in dic:
            if (ps == dic.get(nm)):
                print("connected")
                playerShow.set(nm)
                app.deiconify() #release invisible principal window app
                userInfo.destroy()


def confRegister():
    NAME = name.get()
    PASS = psw.get()
    CONFPASS = confpsw.get()

    # User dictionary
    userDic = {}
    if not(PASS == CONFPASS):
        tk.messagebox.showerror("Mauvais mdp", "verifiez la similitude des mdp")
    else:
        print("test")
        print(NAME, PASS)
        userDic[NAME] = PASS
        print(userDic)
        dataBase = json.load(open('./login/login.json', 'r'))
        if type(dataBase) is dict:
            dataBase = [dataBase]
        dataBase.append(userDic)

        with open('./login/login.json', 'w') as outfile:
            json.dump(dataBase, outfile)
        tk.messagebox.showinfo("success", "Compte a bien ete cree!")
        registerWindow.destroy()
        userInfo.update()



def register():
    global name
    global psw
    global confpsw
    global registerWindow

    name = tk.StringVar()
    psw = tk.StringVar()
    confpsw = tk.StringVar()

    #topLevel===
    registerWindow = tk.Toplevel()
    registerWindow.update_idletasks()  # Update "requested size" from geometry manager

    x = (registerWindow.winfo_screenwidth() - registerWindow.winfo_reqwidth()) / 2
    y = (registerWindow.winfo_screenheight() - registerWindow.winfo_reqheight()) / 2
    registerWindow.geometry("+%d+%d" % (x, y))
    #=============

    userName1 = tk.Label(registerWindow, text='Pseudo', font=("Helvtica 10"))
    entryName1 = tk.Entry(registerWindow, textvariable=name)

    userPass1 = tk.Label(registerWindow, text='MotDePasse', font=("Helvtica 10"))
    entryPass1 = tk.Entry(registerWindow, show="*", textvariable=psw)

    userConfPass = tk.Label(registerWindow, text='Confirme MotDePasse', font=("Helvtica 10"))
    entryConfPass = tk.Entry(registerWindow, show="*", textvariable=confpsw)

    confirm = tk.Button(registerWindow, font=("Helvtica 10"), command= confRegister)
    #errorLabel = tk.Label(register, font=("Helvtica 7"), fg='red')

    userName1.pack()
    entryName1.pack()
    userPass1.pack()
    entryPass1.pack()
    userConfPass.pack()
    entryConfPass.pack()
    confirm.pack()



def exit():
    userInfo.destroy()
    app.destroy()
    sys.exit()

#variable
collectNameLogin = tk.StringVar()
collectPassLogin = tk.StringVar()

#===LOGIN WINDOW====
userInfo = tk.Toplevel()
userInfo.geometry('350x300')
userInfo.title("CONNECTION A VOTRE COMPTE")
userInfo.configure(background='white')
fontPhoto = tk.PhotoImage(file='./image/logoAPOCS.png')
fontPhotoResize = fontPhoto.subsample(30, 30)
photoLabel = tk.Label(userInfo, image=fontPhotoResize, bg='white')
#===========
userInfo.update_idletasks()  # Update "requested size" from geometry manager

x = (userInfo.winfo_screenwidth() - userInfo.winfo_reqwidth()) / 2
y = (userInfo.winfo_screenheight() - userInfo.winfo_reqheight()) / 2
userInfo.geometry("+%d+%d" % (x, y))

#User Label + Entry
userName = tk.Label(userInfo, text='Pseudo', font=("Helvtica 10"), bg='white')
entryName = tk.Entry(userInfo, textvariable=collectNameLogin)
userPass = tk.Label(userInfo, text='MotDePasse', font=("Helvtica 10"), bg='white')
entryPass = tk.Entry(userInfo, show="*", textvariable=collectPassLogin)

#Cancel
buttonCancel = tk.Button(userInfo, text='ANNULER', bg='black', fg='red2', font=("Times 10 bold"), command=lambda: exit())

#registration

registration = tk.Button(userInfo, text='S\'inscrire', command=register)
loginButton = tk.Button(userInfo, text="Connect", command=connectVerif)

#pack
photoLabel.pack()
userName.pack()
entryName.pack()
userPass.pack()
entryPass.pack()
loginButton.pack()
registration.pack()
buttonCancel.pack()

#====================================================================================

#Fonctions

def gameOpen(i):
    global rd
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
    global playerStart
    global countLabel
    global countWait
    global countStart
    global countStartLabel
    global countClose
    global countCloseLabel
    global game

    playerStart = random.randrange(1, 3)
    print(playerStart)

    rd = i
    game = tk.Toplevel()
    # customs window
    game.geometry("650x650")
    game.withdraw()
    game.update_idletasks()  # Update "requested size" from geometry manager
    game.iconbitmap("./image/icon.ico/")
    # window to avoid update_idletasks() drawing the window in the wrong
    # position.
    game.withdraw()
    game.update_idletasks()  # Update "requested size" from geometry manager

    x = (app.winfo_screenwidth() - app.winfo_reqwidth()) / 3
    y = (app.winfo_screenheight() - app.winfo_reqheight()) / 3
    game.geometry("+%d+%d" % (x, y))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    game.deiconify()

    game.resizable(False, False)

    #customImage

    canvas = tk.Canvas(game, width=700, height=700, relief="raised", background='black')
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

    label_player1 = tk.Label(game, text="Joueur 1: X")
    label_player1.place(x=0, y=200)

    label_player1 = tk.Label(game, text="Joueur 2: O")
    label_player1.place(x=500, y=200)

    #labels players
    if playerStart == 1:

        # button
        # ligne 1
        b1 = tk.Button(game, text= " ", width=13, height=5, bg="#7bb1ef", command=lambda: startGame(b1))
        b1.place(x=155, y=12)

        b2 = tk.Button(game, text= " ", width=13, height=5,command=lambda: startGame(b2))
        b2.place(x=265, y=12)

        b3 = tk.Button(game, text= " ", width=13, height=5, bg="#7bb1ef", command=lambda: startGame(b3))
        b3.place(x=375, y=12)

        # ligne 2
        b4 = tk.Button(game, text= " ", width=13, height=6, command=lambda: startGame(b4))
        b4.place(x=155, y=107)

        b5 = tk.Button(game, text= " ", width=13, height=6, bg="#7bb1ef", command=lambda: startGame(b5))
        b5.place(x=265, y=107)

        b6 = tk.Button(game, text= " ", width=13, height=6, command=lambda: startGame(b6))
        b6.place(x=375, y=107)

        # ligne 3
        b7 = tk.Button(game, text= " ", width=13, height=5, bg="#7bb1ef", command=lambda: startGame(b7))
        b7.place(x=155, y=215)

        b8 = tk.Button(game,text= " ", width=13, height=5, command=lambda: startGame(b8))
        b8.place(x=265, y=215)

        b9 = tk.Button(game,text= " ", width=13, height=5, bg="#7bb1ef", command=lambda: startGame(b9))
        b9.place(x=375, y=215)


        #Label Winner

        win = tk.Label(game, bg='black', fg='#ff8d00')
        win.place(x=240, y=500)

        # countdown
        countWait = tk.Label(game, bg='black', fg='white', font=("Times 17 bold"))
        countWait.place(x=120, y=320)
        countLabel = tk.Label(game, bg='black', fg='#ff8d00', font=("Times 26 bold"))
        countLabel.place(x=320, y=360)

        countStart = tk.Label(game, bg='black', fg='white', font=("Times 17 bold"))
        countStart.place(x=260, y=320)
        countStartLabel = tk.Label(game, bg='black', fg='#ff8d00', font=("Times 26 bold"))
        countStartLabel.place(x=300, y=360)

        countClose = tk.Label(game, bg='black', fg='white', font=("Times 17 bold"))
        countClose.place(x=110, y=320)
        countCloseLabel = tk.Label(game, bg='black', fg='firebrick2', font=("Times 26 bold"))
        countCloseLabel.place(x=320, y=390)
        #WHo start?
        labelStartUser = tk.Label(game, text='TU COMMENCES!', font=("Helvetica 26 italic bold underline"), bg='black', fg='DarkOrchid3')
        labelStartUser.place(x=130, y=450)
        countdownBeforeStart()
        labelStartUser.destroy()

    else:
        playCaseFirst = random.randrange(1, 5) #choose randomly where to start playing between corner case and middle case
        print(playCaseFirst)
        # button
        # ligne 1
        b1 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGame(b1))
        b1.place(x=155, y=12)

        b2 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGame(b2))
        b2.place(x=265, y=12)

        b3 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGame(b3))
        b3.place(x=375, y=12)

        # ligne 2
        b4 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGame(b4))
        b4.place(x=155, y=107)

        b5 = tk.Button(game, text=" ", width=13, height=6, bg="#7bb1ef", command=lambda: startGame(b5))
        b5.place(x=265, y=107)


        b6 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGame(b6))
        b6.place(x=375, y=107)

        # ligne 3
        b7 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGame(b7))
        b7.place(x=155, y=215)

        b8 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGame(b8))
        b8.place(x=265, y=215)

        b9 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGame(b9))
        b9.place(x=375, y=215)

        #random choose where to start

        if playCaseFirst == 1:
            b1.config(text='O')
        elif playCaseFirst == 2:
            b3.config(text='O')
        elif playCaseFirst == 3:
            b5.config(text='O')
        elif playCaseFirst == 4:
            b7.config(text='O')
        elif playCaseFirst == 5:
            b9.config(text='O')

        # Label Winner
        win = tk.Label(game, bg='black', fg='#ff8d00')
        win.place(x=240, y=500)

        # countdown
        countWait = tk.Label(game, bg='black', fg='white', font=("Times 17 bold"))
        countWait.place(x=120, y=320)
        countLabel = tk.Label(game, bg='black', fg='#ff8d00', font=("Times 26 bold"))
        countLabel.place(x=320, y=360)

        countStart = tk.Label(game, bg='black', fg='white', font=("Times 17 bold"))
        countStart.place(x=260, y=320)
        countStartLabel = tk.Label(game, bg='black', fg='#ff8d00', font=("Times 26 bold"))
        countStartLabel.place(x=300, y=360)

        countClose = tk.Label(game, bg='black', fg='white', font=("Times 17 bold"))
        countClose.place(x=110, y=320)
        countCloseLabel = tk.Label(game, bg='black', fg='firebrick2', font=("Times 26 bold"))
        countCloseLabel.place(x=320, y=390)
        #Who start?
        labelStartUser = tk.Label(game, text='LE BOT A COMMENCE! A TOI', font=("Helvetica 26 italic bold underline"), bg='black', fg='DarkOrchid3')
        labelStartUser.place(x=90, y=450)
        countdownBeforeStart()
        labelStartUser.destroy()

def CloseBoard():
    game.destroy()

def countdown():
    global click
    for k in range(10, 0, -1):
        click = False
        countLabel["text"] = k
        countWait["text"] = "Compte-a-rebours avant prochain round"
        app.update()
        time.sleep(1)

def countdownBeforeStart():
    global click
    for k in range(5, -1, -1):
        click = False
        countStartLabel["text"] = k
        countStart["text"] = "A toi dans: "
        app.update()
        time.sleep(1)
    click = True
    countStartLabel.destroy()
    countStart["text"] = "A TOI!"

def countdownBeforeClose():
    global click
    for k in range(5, -1, -1):
        click = False
        countCloseLabel["text"] = k
        countClose["text"] = "Compte-a-rebours avant fermeture \n tes donnees ont ete save inchallah"
        app.update()
        time.sleep(1)

#def score(winBot,winUser):


#global settings
y = "" #sign attribution
player = []
playerBot = []
click = True
winBot = 0
winUser = 0

def startGame(b):
    global x,y
    global player, playerBot
    global click

    global winBot
    global winUser
    #global game
    #global win



    #score.append(winUser)
    #score.append(winBot)



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
#====================================================
                #USER
    # Vertical Verif
    if b1["text"] == 'X' and b4["text"] == 'X' and b7["text"] == 'X':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        win.config(text="GG, Tu m'impressionnes!")
        click = False
        winUser += 1
        countStart.destroy()
        #====
        upRd = rd - 1
        if upRd == 0:
            print("end")
            countdownBeforeClose()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
        else:
            # countdown
            countdown()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
            gameOpen(upRd)

    if b2["text"] == 'X' and b5["text"] == 'X' and b8["text"] == 'X':
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        win.config(text="GG, Tu m'impressionnes!")
        click = False
        winUser += 1
        countStart.destroy()
        # ====
        upRd = rd - 1
        if upRd == 0:
            print("end")
            countdownBeforeClose()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
        else:
            # countdown
            countdown()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
            gameOpen(upRd)

    if b3["text"] == 'X' and b6["text"] == 'X' and b9["text"] == 'X':
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        win.config(text="GG, Tu m'impressionnes!")
        click = False
        winUser += 1
        countStart.destroy()
        # ====
        upRd = rd - 1
        if upRd == 0:
            print("end")
            countdownBeforeClose()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
        else:
            # countdown
            countdown()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
            gameOpen(upRd)

    # Diagonal Verif
    if b1["text"] == 'X' and b5["text"] == 'X' and b9["text"] == 'X':
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        win.config(text="GG, Tu m'impressionnes!")
        click = False
        winUser += 1
        countStart.destroy()
        # ====
        upRd = rd - 1
        if upRd == 0:
            print("end")
            countdownBeforeClose()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
        else:
            # countdown
            countdown()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
            gameOpen(upRd)

    if b3["text"] == 'X' and b5["text"] == 'X' and b7["text"] == 'X':
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green')
        win.config(text="GG, Tu m'impressionnes!")
        click = False
        winUser += 1
        countStart.destroy()
        # ====
        upRd = rd - 1
        if upRd == 0:
            print("end")
            countdownBeforeClose()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
        else:
            # countdown
            countdown()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
            gameOpen(upRd)

    # Horizontal verif
    if b1["text"] == 'X' and b2["text"] == 'X' and b3["text"] == 'X':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        win.config(text="GG, Tu m'impressionnes!")
        click = False
        winUser += 1
        countStart.destroy()
        # ====
        upRd = rd - 1
        if upRd == 0:
            print("end")
            countdownBeforeClose()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
        else:
            # countdown
            countdown()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
            gameOpen(upRd)

    if b4["text"] == 'X' and b5["text"] == 'X' and b6["text"] == 'X':
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        win.config(text="GG, Tu m'impressionnes!")
        click = False
        winUser += 1
        countStart.destroy()
        # ====
        upRd = rd - 1
        if upRd == 0:
            print("end")
            countdownBeforeClose()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
        else:
            # countdown
            countdown()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
            gameOpen(upRd)

    if b7["text"] == 'X' and b8["text"] == 'X' and b9["text"] == 'X':
        b7.config(bg='green')
        b8.config(bg='green')
        b9.config(bg='green')
        win.config(text="GG, Tu m'impressionnes!")
        click = False
        winUser += 1
        countStart.destroy()
        # ====
        upRd = rd - 1
        if upRd == 0:
            print("end")
            countdownBeforeClose()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
        else:
            # countdown
            countdown()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
            gameOpen(upRd)

#====================================================
            #BOT
    #Vertical Verif
    if b1["text"] == 'O' and b4["text"] == 'O' and b7["text"] == 'O':
            b1.config(bg='red')
            b4.config(bg='red')
            b7.config(bg='red')
            win.config(text="Dommage, Bot a gagne!")
            click = False
            winBot += 1
            countStart.destroy()
            # ====
            upRd = rd - 1
            if upRd == 0:
                print("end")
                countdownBeforeClose()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
            else:
                # countdown
                countdown()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
                gameOpen(upRd)

    if b2["text"] == 'O' and b5["text"] == 'O' and b8["text"] == 'O':
            b2.config(bg='red')
            b5.config(bg='red')
            b8.config(bg='red')
            win.config(text="Dommage, Bot a gagne!")
            click = False
            winBot += 1
            countStart.destroy()
            # ====
            upRd = rd - 1
            if upRd == 0:
                print("end")
                countdownBeforeClose()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
            else:
                # countdown
                countdown()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
                gameOpen(upRd)

    if b3["text"] == 'O' and b6["text"] == 'O' and b9["text"] == 'O':
            b3.config(bg='red')
            b6.config(bg='red')
            b9.config(bg='red')
            win.config(text="Dommage, Bot a gagne!")
            click = False
            winBot += 1
            countStart.destroy()
            # ====
            upRd = rd - 1
            if upRd == 0:
                print("end")
                countdownBeforeClose()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
            else:
                # countdown
                countdown()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
                gameOpen(upRd)

    #Diagonal Verif
    if b1["text"] == 'O' and b5["text"] == 'O' and b9["text"] == 'O':
            b1.config(bg='red')
            b5.config(bg='red')
            b9.config(bg='red')
            win.config(text="Dommage Bot a gagne!")
            click = False
            winBot += 1
            countStart.destroy()
            # ====
            upRd = rd - 1
            if upRd == 0:
                print("end")
                countdownBeforeClose()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
            else:
                # countdown
                countdown()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
                gameOpen(upRd)

    if b3["text"] == 'O' and b5["text"] == 'O' and b7["text"] == 'O':
            b3.config(bg='red')
            b5.config(bg='red')
            b7.config(bg='red')
            win.config(text="Dommage Bot a gagne!")
            click = False
            winBot += 1
            countStart.destroy()
            # ====
            upRd = rd - 1
            if upRd == 0:
                print("end")
                countdownBeforeClose()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
            else:
                # countdown
                countdown()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
                gameOpen(upRd)

    #Horizontal verif
    if b1["text"] == 'O' and b2["text"] == 'O' and b3["text"] == 'O':
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        win.config(text="Dommage, Bot a gagne!")
        click = False
        winBot += 1
        countStart.destroy()
        # ====
        upRd = rd - 1
        if upRd == 0:
            print("end")
            countdownBeforeClose()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
        else:
            # countdown
            countdown()
            CloseBoard()
            print("point Bot:", winBot, "point User:", winUser)
            gameOpen(upRd)

    if b4["text"] == 'O' and b5["text"] == 'O' and b6["text"] == 'O':
            b4.config(bg='red')
            b5.config(bg='red')
            b6.config(bg='red')
            win.config(text="Dommage, Bot a gagne!")
            click = False
            winBot += 1
            countStart.destroy()
            # ====
            upRd = rd - 1
            if upRd == 0:
                print("end")
                countdownBeforeClose()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
            else:
                # countdown
                countdown()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
                gameOpen(upRd)

    if b7["text"] == 'O' and b8["text"] == 'O' and b9["text"] == 'O':
            b7.config(bg='red')
            b8.config(bg='red')
            b9.config(bg='red')
            win.config(text="Dommage, Bot a gagne!")
            click = False
            winBot += 1
            countStart.destroy()
            # ====
            upRd = rd - 1
            if upRd == 0:
                print("end")
                countdownBeforeClose()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
            else:
                # countdown
                countdown()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
                gameOpen(upRd)

    #draw
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
            win.config(text="egalite! Match fini en egalite")
            click = False
            countStart.destroy()
            # ====
            upRd = rd - 1
            if upRd == 0:
                countdownBeforeClose()
                print("end")
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
            else:
                # countdown
                countdown()
                CloseBoard()
                print("point Bot:", winBot, "point User:", winUser)
                gameOpen(upRd)


def initialisation():
    global gamesNb
    global diffMode
    gamesNb = nb.get()
    diffMode = df.get()

    lDf = ["facile", "moyen", "difficile", "extreme"]
    if diffMode in lDf:
        if (gamesNb > 5):
            nb.set("No life! joue -!")
        elif (gamesNb > 0):
            gameOpen(gamesNb)
        else:
            nb.set("WHUT")
    else:
        df.set("error")


#tkinter custom
app.withdraw()
app.update_idletasks()  # Update "requested size" from geometry manager
app.iconbitmap("./image/icon.ico/")
app.geometry("650x390")

# window to avoid update_idletasks() drawing the window in the wrong
# position.
app.withdraw()
app.update_idletasks()  # Update "requested size" from geometry manager

x = (app.winfo_screenwidth() - app.winfo_reqwidth()) / 3
y = (app.winfo_screenheight() - app.winfo_reqheight()) / 3
app.geometry("+%d+%d" % (x, y))

# This seems to draw the window frame immediately, so only call deiconify()
# after setting correct window position

app.resizable(False, False)

#cursor
app.configure(cursor='heart')

#title
canvastext = tk.Canvas(app, width=650, height=40, bg="black")
canvastext.pack()
canvastext.create_text(320, 20,fill="#ff8d00",font="Helvetica 26 italic bold",
                        text="MORPIONNE")
#=========

#image

img = PIL.ImageTk.PhotoImage(PIL.Image.open("./image/background.jpg"))
background = tk.Label(app, image=img)
background.pack(side="bottom", fill="both", expand="yes")




#EntryVariable
nb = tk.IntVar()
df = tk.StringVar()
playerShow = tk.StringVar()
#Labels==============================================================
#TITRE


#number of match
nbMatchLabel = tk.Label(app, text="Nombre de Round:", font="Helvetica 11 italic bold", bg='black', fg="#ff8d00")
nbMatchLabel.place(x=160, y=120)


nbMatch = tk.Entry(app, textvariable=nb, font="Helvetica 11 italic bold")
nb.set("1-5")
nbMatch.place(x=320, y=120)

#Difficulty status
nbDiffLabel = tk.Label(app, text="Niveau de difficulter:", font="Helvetica 11 italic bold", bg='black', fg="#ff8d00")
nbDiffLabel.place(x=160, y=150)
difficulty = tk.Entry(app, textvariable=df, font="Helvetica 11 italic bold")
df.set("facile-moyen-difficile-extreme")
difficulty.place(x=325, y=150)

#player
plLabel = tk.Label(app, text="Bienvenue: ", font="Helvetica 11 italic bold")
playerLabelShow = tk.Label(app, textvariable=playerShow, bg="pink", font="Helvetica 11 italic bold")
playerShow.set("Joueur: ???")
playerLabelShow.place(x= 102, y=300)
plLabel.place(x=10, y=300)
#Bottom
matchValidate = tk.Button(app, text="JOUER", font="Helvetica 11 italic bold", command=initialisation, bg='#ff8d00', fg="black")
matchValidate.place(x=270, y=190)
#=====================================================================




#Tkinter loop
app.mainloop()