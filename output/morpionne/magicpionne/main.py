# librairies
import tkinter as tk
import random
import time
import pygame.mixer, pygame.mixer_music



class superPower:

    # 25points
    def removeCase(self):
        return

    # 20points
    def moveCase(self):
        return

    # 15points
    def blockCase(self):
        return

    # 10points
    def rotateGame(self):
        return


# GUI WITH TK
def createBoard(name):
    global magicB
    global winner
    global winnerVar
    global pseudo

    pseudo = name

    magicB = tk.Tk()
    magicB.title("MAGIC PIONNE")
    magicB.geometry("820x750")

    pygame.mixer.init()
    pygame.mixer.music.load('./sound/magicpionne.ogg')  # Bienvenue sur Magic Pionne
    pygame.mixer.music.play()

    canvas = tk.Canvas(magicB, width=820, height=750, relief="raised", background='black')
    canvas.pack(expand='yes', fill='both')


    winnerVar = tk.Label(magicB, text="?", font='Times 15', bg='black', fg='white')
    winnerVar.place(x=200, y=650)

    createBoard1()
    createBoard2()
    createBoard3()
    createBoard4()
    createBoard5()
    createBoard6()
    createBoard7()
    createBoard8()
    createBoard9()

    magicB.protocol("WM_DELETE_WINDOW", closeMagicPionne)

    x = (magicB.winfo_screenwidth() - magicB.winfo_reqwidth()) / 3.5
    y = (magicB.winfo_screenheight() - magicB.winfo_reqheight()) / 3.5
    magicB.geometry("+%d+%d" % (x, y))

    winnerLabel = tk.Label(magicB, text="GAGNANT: ", font='Times 12', bg='black', fg='orange')
    winnerLabel.place(x=100, y=650)

    restartBtn = tk.Button(magicB, text="RECOMMENCER", font='Times 14', bg='black', fg='white', command=restart)
    restartBtn.place(x=350, y=650)

    infoLb = tk.Label(magicB, text="Ce mode de jeu ne comptabilise pas les victoires pour le Leaderboard, le bot choisis aleatoirement dans ce mode de jeu.", bg='black', fg='yellow')
    infoLb.place(x=100, y=700)

    regles = tk.Button(magicB, text="Regles, explication à l'oral!", font='Times 12', bg='black', fg='pink', command=rules)
    regles.place(x=550, y=650)

    magicB.resizable(False, False)
    magicB.iconbitmap('./image/iconeAPP.ico')
    magicB.mainloop()

def restart():
    global play1
    global play2
    global play3
    global play4
    global play5
    global play6
    global play7
    global play8
    global play9
    global morpion1
    global morpion2
    global morpion3
    global morpion4
    global morpion5
    global morpion6
    global morpion7
    global morpion8
    global morpion9
    global morpionFinish
    global morpionFinish1
    global morpionFinish2
    global morpionFinish3
    global morpionFinish4
    global morpionFinish5
    global morpionFinish6
    global morpionFinish7
    global morpionFinish8
    global morpionFinish9
    global wUserL1
    global wUserL2
    global wUserL3
    global wUserC1
    global wUserC2
    global wUserC3
    global wUserD1
    global wUserD2
    global wBotL1
    global wBotL2
    global wBotL3
    global wBotC1
    global wBotC2
    global wBotC3
    global wBotD1
    global wBotD2
    global check1
    global check2
    global check3
    global check4
    global check5
    global check6
    global check7
    global check8
    global check9
    global click
    global winnerVar
    # check finished morpion
    morpionFinish = []
    morpionFinish2 = []
    morpionFinish3 = []
    morpionFinish4 = []
    morpionFinish5 = []
    morpionFinish6 = []
    morpionFinish7 = []
    morpionFinish8 = []
    morpionFinish9 = []
    # ==================
    wUserL1 = []
    wUserL2 = []
    wUserL3 = []
    wUserC1 = []
    wUserC2 = []
    wUserC3 = []
    wUserD1 = []
    wUserD2 = []
    # ==================
    wBotL1 = []
    wBotL2 = []
    wBotL3 = []
    wBotC1 = []
    wBotC2 = []
    wBotC3 = []
    wBotD1 = []
    wBotD2 = []
    # checked
    check1 = False
    check2 = False
    check3 = False
    check4 = False
    check5 = False
    check6 = False
    check7 = False
    check8 = False
    check9 = False
    winnerVar["text"] = "?"
    click = True

    for a in morpion1:
        a['state'] = 'normal'
        a['text'] = ' '
        a.config(bg='pink')
    for a in morpion2:
        a['state'] = 'normal'
        a['text'] = ' '
        a.config(bg='pink')
    for a in morpion3:
        a['state'] = 'normal'
        a['text'] = ' '
        a.config(bg='pink')
    for a in morpion4:
        a['state'] = 'normal'
        a['text'] = ' '
        a.config(bg='pink')
    for a in morpion5:
        a['state'] = 'normal'
        a['text'] = ' '
        a.config(bg='pink')
    for a in morpion6:
        a['state'] = 'normal'
        a['text'] = ' '
        a.config(bg='pink')
    for a in morpion7:
        a['state'] = 'normal'
        a['text'] = ' '
        a.config(bg='pink')
    for a in morpion8:
        a['state'] = 'normal'
        a['text'] = ' '
        a.config(bg='pink')
    for a in morpion9:
        a['state'] = 'normal'
        a['text'] = ' '
        a.config(bg='pink')

def closeMagicPionne():
    magicB.destroy()

def rules():
    pygame.mixer.init()
    pygame.mixer.music.load('./sound/reglemagicpionne.ogg')  # Bienvenue sur Magic Pionne
    pygame.mixer.music.play()
# ======================

# Creating all our morpionne board (tic tac toe)
def createBoard1():
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9

    b1 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                   command=lambda: startMagicPionne(b1))
    b1.place(x=150, y=30)

    b2 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                   command=lambda: startMagicPionne(b2))
    b2.place(x=200, y=30)

    b3 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                   command=lambda: startMagicPionne(b3))
    b3.place(x=250, y=30)

    # ligne 2
    b4 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                   command=lambda: startMagicPionne(b4))
    b4.place(x=150, y=80)

    b5 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                   command=lambda: startMagicPionne(b5))
    b5.place(x=200, y=80)

    b6 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                   command=lambda: startMagicPionne(b6))
    b6.place(x=250, y=80)

    # ligne 3
    b7 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                   command=lambda: startMagicPionne(b7))
    b7.place(x=150, y=130)

    b8 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                   command=lambda: startMagicPionne(b8))
    b8.place(x=200, y=130)

    b9 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                   command=lambda: startMagicPionne(b9))
    b9.place(x=250, y=130)


def createBoard2():
    global b12
    global b22
    global b32
    global b42
    global b52
    global b62
    global b72
    global b82
    global b92

    b12 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b12))
    b12.place(x=350, y=30)

    b22 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b22))
    b22.place(x=400, y=30)

    b32 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b32))
    b32.place(x=450, y=30)

    # ligne 2
    b42 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b42))
    b42.place(x=350, y=80)

    b52 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b52))
    b52.place(x=400, y=80)

    b62 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b62))
    b62.place(x=450, y=80)

    # ligne 3
    b72 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b72))
    b72.place(x=350, y=130)

    b82 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b82))
    b82.place(x=400, y=130)

    b92 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b92))
    b92.place(x=450, y=130)


def createBoard3():
    global b13
    global b23
    global b33
    global b43
    global b53
    global b63
    global b73
    global b83
    global b93

    b13 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b13))
    b13.place(x=550, y=30)

    b23 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b23))
    b23.place(x=600, y=30)

    b33 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b33))
    b33.place(x=650, y=30)

    # ligne 2
    b43 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b43))
    b43.place(x=550, y=80)

    b53 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b53))
    b53.place(x=600, y=80)

    b63 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b63))
    b63.place(x=650, y=80)

    # ligne 3
    b73 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b73))
    b73.place(x=550, y=130)

    b83 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b83))
    b83.place(x=600, y=130)

    b93 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b93))
    b93.place(x=650, y=130)


def createBoard4():
    global b14
    global b24
    global b34
    global b44
    global b54
    global b64
    global b74
    global b84
    global b94

    b14 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b14))
    b14.place(x=150, y=230)

    b24 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b24))
    b24.place(x=200, y=230)

    b34 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b34))
    b34.place(x=250, y=230)

    # ligne 2
    b44 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b44))
    b44.place(x=150, y=280)

    b54 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b54))
    b54.place(x=200, y=280)

    b64 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b64))
    b64.place(x=250, y=280)

    # ligne 3
    b74 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b74))
    b74.place(x=150, y=330)

    b84 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b84))
    b84.place(x=200, y=330)

    b94 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b94))
    b94.place(x=250, y=330)


def createBoard5():
    global b15
    global b25
    global b35
    global b45
    global b55
    global b65
    global b75
    global b85
    global b95

    b15 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b15))
    b15.place(x=350, y=230)

    b25 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b25))
    b25.place(x=400, y=230)

    b35 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b35))
    b35.place(x=450, y=230)

    # ligne 2
    b45 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b45))
    b45.place(x=350, y=280)

    b55 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b55))
    b55.place(x=400, y=280)

    b65 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b65))
    b65.place(x=450, y=280)

    # ligne 3
    b75 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b75))
    b75.place(x=350, y=330)

    b85 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b85))
    b85.place(x=400, y=330)

    b95 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b95))
    b95.place(x=450, y=330)


def createBoard6():
    global b16
    global b26
    global b36
    global b46
    global b56
    global b66
    global b76
    global b86
    global b96

    b16 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b16))
    b16.place(x=550, y=230)

    b26 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b26))
    b26.place(x=600, y=230)

    b36 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b36))
    b36.place(x=650, y=230)

    # ligne 2
    b46 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b46))
    b46.place(x=550, y=280)

    b56 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b56))
    b56.place(x=600, y=280)

    b66 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b66))
    b66.place(x=650, y=280)

    # ligne 3
    b76 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b76))
    b76.place(x=550, y=330)

    b86 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b86))
    b86.place(x=600, y=330)

    b96 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b96))
    b96.place(x=650, y=330)


def createBoard7():
    global b17
    global b27
    global b37
    global b47
    global b57
    global b67
    global b77
    global b87
    global b97

    b17 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b17))
    b17.place(x=150, y=430)

    b27 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b27))
    b27.place(x=200, y=430)

    b37 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b37))
    b37.place(x=250, y=430)

    # ligne 2
    b47 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b47))
    b47.place(x=150, y=480)

    b57 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b57))
    b57.place(x=200, y=480)

    b67 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b67))
    b67.place(x=250, y=480)

    # ligne 3
    b77 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b77))
    b77.place(x=150, y=530)

    b87 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b87))
    b87.place(x=200, y=530)

    b97 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b97))
    b97.place(x=250, y=530)


def createBoard8():
    global b18
    global b28
    global b38
    global b48
    global b58
    global b68
    global b78
    global b88
    global b98

    b18 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b18))
    b18.place(x=350, y=430)

    b28 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b28))
    b28.place(x=400, y=430)

    b38 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b38))
    b38.place(x=450, y=430)

    # ligne 2
    b48 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b48))
    b48.place(x=350, y=480)

    b58 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b58))
    b58.place(x=400, y=480)

    b68 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b68))
    b68.place(x=450, y=480)

    # ligne 3
    b78 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b78))
    b78.place(x=350, y=530)

    b88 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b88))
    b88.place(x=400, y=530)

    b98 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b98))
    b98.place(x=450, y=530)


def createBoard9():
    global b19
    global b29
    global b39
    global b49
    global b59
    global b69
    global b79
    global b89
    global b99

    b19 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b19))
    b19.place(x=550, y=430)

    b29 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b29))
    b29.place(x=600, y=430)

    b39 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b39))
    b39.place(x=650, y=430)

    # ligne 2
    b49 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b49))
    b49.place(x=550, y=480)

    b59 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b59))
    b59.place(x=600, y=480)

    b69 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b69))
    b69.place(x=650, y=480)

    # ligne 3
    b79 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b79))
    b79.place(x=550, y=530)

    b89 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b89))
    b89.place(x=600, y=530)

    b99 = tk.Button(magicB, text=" ", width=5, height=2, bg="pink", activebackground="white", disabledforeground="cyan",
                    command=lambda: startMagicPionne(b99))
    b99.place(x=650, y=530)


# ======================

click = True  # cool BOOL to check if YOU CAN CLICK!
# check finished morpion
morpionFinish = []
morpionFinish2 = []
morpionFinish3 = []
morpionFinish4 = []
morpionFinish5 = []
morpionFinish6 = []
morpionFinish7 = []
morpionFinish8 = []
morpionFinish9 = []
# ==================
wUserL1 = []
wUserL2 = []
wUserL3 = []
wUserC1 = []
wUserC2 = []
wUserC3 = []
wUserD1 = []
wUserD2 = []
# ==================
wBotL1 = []
wBotL2 = []
wBotL3 = []
wBotC1 = []
wBotC2 = []
wBotC3 = []
wBotD1 = []
wBotD2 = []
# checked
check1 = False
check2 = False
check3 = False
check4 = False
check5 = False
check6 = False
check7 = False
check8 = False
check9 = False


def countdown(b):
    global click
    for k in range(1, 0, -1):
        click = False
        magicB.update()
        time.sleep(1)
        b.config(bg='grey')

def countdownBeforeBotPlay():
    for k in range(1, 0, -1):
        magicB.update()
        time.sleep(1)
# check win============

def WinMorpion1():
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    global play1
    global play2
    global play3
    global play4
    global play5
    global play6
    global play7
    global play8
    global play9
    global morpion1
    global morpion2
    global morpion3
    global morpion4
    global morpion5
    global morpion6
    global morpion7
    global morpion8
    global morpion9
    global morpionFinish
    global morpionFinish1
    global morpionFinish2
    global morpionFinish3
    global morpionFinish4
    global morpionFinish5
    global morpionFinish6
    global morpionFinish7
    global morpionFinish8
    global morpionFinish9
    global wUserL1
    global wUserL2
    global wUserL3
    global wUserC1
    global wUserC2
    global wUserC3
    global wUserD1
    global wUserD2
    global wBotL1
    global wBotL2
    global wBotL3
    global wBotC1
    global wBotC2
    global wBotC3
    global wBotD1
    global wBotD2
    global check1
    global check2
    global check3
    global check4
    global check5
    global check6
    global check7
    global check8
    global check9

    # ligne
    l1 = [b1, b2, b3]
    l2 = [b4, b5, b6]
    l3 = [b7, b8, b9]
    # column
    c1 = [b1, b4, b7]
    c2 = [b2, b5, b8]
    c3 = [b3, b6, b9]
    # diagonal
    d1 = [b1, b5, b9]
    d2 = [b3, b5, b7]

    # user
    if all([a['text'] == 'X' for a in l1]) and check1 == False:
        check1 = True
        for a in l1:
            a.config(bg='green')
            for e in morpion1:
                morpionFinish.append(e)
        wUserL1.append("win")
        wUserC1.append("win")
        wUserD1.append("win")

        return True

    elif all([a['text'] == 'X' for a in l2]) and check1 == False:
        check1 = True
        for a in l2:
            a.config(bg='green')
            for e in morpion1:
                morpionFinish.append(e)
        wUserL1.append("win")
        wUserC1.append("win")
        wUserD1.append("win")

        return True

    elif all([a['text'] == 'X' for a in l3]) and check1 == False:
        check1 = True
        for a in l3:
            a.config(bg='green')
            for e in morpion1:
                morpionFinish.append(e)
        wUserL1.append("win")
        wUserC1.append("win")
        wUserD1.append("win")

        return True

    elif all([a['text'] == 'X' for a in c1]) and check1 == False:
        check1 = True
        for a in c1:
            a.config(bg='green')
            for e in morpion1:
                morpionFinish.append(e)
        wUserL1.append("win")
        wUserC1.append("win")
        wUserD1.append("win")

        return True

    elif all([a['text'] == 'X' for a in c2]) and check1 == False:
        check1 = True
        for a in c2:
            a.config(bg='green')
            for e in morpion1:
                morpionFinish.append(e)
        wUserL1.append("win")
        wUserC1.append("win")
        wUserD1.append("win")

        return True

    elif all([a['text'] == 'X' for a in c3]) and check1 == False:
        check1 = True
        for a in c3:
            a.config(bg='green')
            for e in morpion1:
                morpionFinish.append(e)
        wUserL1.append("win")
        wUserC1.append("win")
        wUserD1.append("win")

        return True

    elif all([a['text'] == 'X' for a in d1]) and check1 == False:
        check1 = True
        for a in d1:
            a.config(bg='green')
            for e in morpion1:
                morpionFinish.append(e)
        wUserL1.append("win")
        wUserC1.append("win")
        wUserD1.append("win")

        return True

    if all([a['text'] == 'X' for a in d2]) and check1 == False:
        check1 = True
        for a in d2:
            a.config(bg='green')
            for e in morpion1:
                morpionFinish.append(e)
        wUserL1.append("win")
        wUserC1.append("win")
        wUserD1.append("win")

        return True

    # bot
    elif all([a['text'] == 'O' for a in l1]) and check1 == False:
        check1 = True
        for a in l1:
            a.config(bg='red')
            for e in morpion1:
                morpionFinish.append(e)
        wBotL1.append("win")
        wBotC1.append("win")
        wBotD1.append("win")

        return True

    elif all([a['text'] == 'O' for a in l2]) and check1 == False:
        check1 = True
        for a in l2:
            a.config(bg='red')
            for e in morpion1:
                morpionFinish.append(e)
        wBotL1.append("win")
        wBotC1.append("win")
        wBotD1.append("win")

        return True

    elif all([a['text'] == 'O' for a in l3]) and check1 == False:
        check1 = True
        for a in l3:
            a.config(bg='red')
            for e in morpion1:
                morpionFinish.append(e)
        wBotL1.append("win")
        wBotC1.append("win")
        wBotD1.append("win")

        return True

    elif all([a['text'] == 'O' for a in c1]) and check1 == False:
        check1 = True
        for a in c1:
            a.config(bg='red')
            for e in morpion1:
                morpionFinish.append(e)
        wBotL1.append("win")
        wBotC1.append("win")
        wBotD1.append("win")

        return True

    elif all([a['text'] == 'O' for a in c2]) and check1 == False:
        check1 = True
        for a in c2:
            a.config(bg='red')
            for e in morpion1:
                morpionFinish.append(e)
        wBotL1.append("win")
        wBotC1.append("win")
        wBotD1.append("win")

        return True

    elif all([a['text'] == 'O' for a in c3]) and check1 == False:
        check1 = True
        for a in c3:
            a.config(bg='red')
            for e in morpion1:
                morpionFinish.append(e)
        wBotL1.append("win")
        wBotC1.append("win")
        wBotD1.append("win")

        return True

    elif all([a['text'] == 'O' for a in d1]) and check1 == False:
        check1 = True
        for a in d1:
            a.config(bg='red')
            for e in morpion1:
                morpionFinish.append(e)
        wBotL1.append("win")
        wBotC1.append("win")
        wBotD1.append("win")

        return True

    elif all([a['text'] == 'O' for a in d2]) and check1 == False:
        check1 = True
        for a in d2:
            a.config(bg='red')
            for e in morpion1:
                morpionFinish.append(e)
        wBotL1.append("win")
        wBotC1.append("win")
        wBotD1.append("win")

        return True

    #draw
    elif all([a['text'] != ' ' for a in morpion1]) and check1 == False:
        check1 = True
        return True

    else:
        return False

def WinMorpion2():
    global b12
    global b22
    global b32
    global b42
    global b52
    global b62
    global b72
    global b82
    global b92
    global play1
    global play2
    global play3
    global play4
    global play5
    global play6
    global play7
    global play8
    global play9
    global morpion1
    global morpion2
    global morpion3
    global morpion4
    global morpion5
    global morpion6
    global morpion7
    global morpion8
    global morpion9
    global wUserL1
    global wUserL2
    global wUserL3
    global wUserC1
    global wUserC2
    global wUserC3
    global wUserD1
    global wUserD2
    global wBotL1
    global wBotL2
    global wBotL3
    global wBotC1
    global wBotC2
    global wBotC3
    global wBotD1
    global wBotD2
    global check1
    global check2
    global check3
    global check4
    global check5
    global check6
    global check7
    global check8
    global check9

    # ligne
    l1 = [b12, b22, b32]
    l2 = [b42, b52, b62]
    l3 = [b72, b82, b92]
    # column
    c1 = [b12, b42, b72]
    c2 = [b22, b52, b82]
    c3 = [b32, b62, b92]
    # diagonal
    d1 = [b12, b52, b92]
    d2 = [b32, b52, b72]

    # user
    if all([a['text'] == 'X' for a in l1]) and check2 == False:
        check2 = True
        for a in l1:
            a.config(bg='green')
            for e in morpion2:
                morpionFinish2.append(e)
        wUserL1.append("win")
        wUserC2.append("win")

        return True

    elif all([a['text'] == 'X' for a in l2]) and check2 == False:
        check2 = True
        for a in l2:
            a.config(bg='green')
            for e in morpion2:
                morpionFinish2.append(e)
        wUserL1.append("win")
        wUserC2.append("win")

        return True

    elif all([a['text'] == 'X' for a in l3]) and check2 == False:
        check2 = True
        for a in l3:
            a.config(bg='green')
            for e in morpion2:
                morpionFinish2.append(e)
        wUserL1.append("win")
        wUserC2.append("win")

        return True

    elif all([a['text'] == 'X' for a in c1]) and check2 == False:
        check2 = True
        for a in c1:
            a.config(bg='green')
            for e in morpion2:
                morpionFinish2.append(e)
        wUserL1.append("win")
        wUserC2.append("win")

        return True

    elif all([a['text'] == 'X' for a in c2]) and check2 == False:
        check2 = True
        for a in c2:
            a.config(bg='green')
            for e in morpion2:
                morpionFinish2.append(e)
        wUserL1.append("win")
        wUserC2.append("win")

        return True

    elif all([a['text'] == 'X' for a in c3]) and check2 == False:
        check2 = True
        for a in c3:
            a.config(bg='green')
            for e in morpion2:
                morpionFinish2.append(e)
        wUserL1.append("win")
        wUserC2.append("win")

        return True

    elif all([a['text'] == 'X' for a in d1]) and check2 == False:
        check2 = True
        for a in d1:
            a.config(bg='green')
            for e in morpion2:
                morpionFinish2.append(e)
        wUserL1.append("win")
        wUserC2.append("win")

        return True

    elif all([a['text'] == 'X' for a in d2]) and check2 == False:
        check2 = True
        for a in d2:
            a.config(bg='green')
            for e in morpion2:
                morpionFinish2.append(e)
        wUserL1.append("win")
        wUserC2.append("win")

        return True

    # bot
    elif all([a['text'] == 'O' for a in l1]) and check2 == False:
        check2 = True
        for a in l1:
            a.config(bg='red')
            for e in morpion2:
                morpionFinish2.append(e)
        wBotL1.append("win")
        wBotC2.append("win")

        return True

    elif all([a['text'] == 'O' for a in l2]) and check2 == False:
        check2 = True
        for a in l2:
            a.config(bg='red')
            for e in morpion2:
                morpionFinish2.append(e)
        wBotL1.append("win")
        wBotC2.append("win")

        return True

    elif all([a['text'] == 'O' for a in l3]) and check2 == False:
        check2 = True
        for a in l3:
            a.config(bg='red')
            for e in morpion2:
                morpionFinish2.append(e)
        wBotL1.append("win")
        wBotC2.append("win")

        return True

    elif all([a['text'] == 'O' for a in c1]) and check2 == False:
        check2 = True
        for a in c1:
            a.config(bg='red')
            for e in morpion2:
                morpionFinish2.append(e)
        wBotL1.append("win")
        wBotC2.append("win")

        return True

    elif all([a['text'] == 'O' for a in c2]) and check2 == False:
        check = True
        for a in c2:
            a.config(bg='red')
            for e in morpion2:
                morpionFinish2.append(e)
        wBotL1.append("win")
        wBotC2.append("win")

        return True

    elif all([a['text'] == 'O' for a in c3]) and check2 == False:
        check = True
        for a in c3:
            a.config(bg='red')
            for e in morpion2:
                morpionFinish2.append(e)
        wBotL1.append("win")
        wBotC2.append("win")

        return True

    elif all([a['text'] == 'O' for a in d1]) and check2 == False:
        check = True
        for a in d1:
            a.config(bg='red')
            for e in morpion2:
                morpionFinish2.append(e)
        wBotL1.append("win")
        wBotC2.append("win")

        return True

    elif all([a['text'] == 'O' for a in d2]) and check2 == False:
        check = True
        for a in d2:
            a.config(bg='red')
            for e in morpion2:
                morpionFinish2.append(e)
        wBotL1.append("win")
        wBotC2.append("win")

        return True

    #draw
    elif all([a['text'] != ' ' for a in morpion2]) and check2 == False:
        check2 = True
        return True

    else:
        return False

def WinMorpion3():
    global b13
    global b23
    global b33
    global b43
    global b53
    global b63
    global b73
    global b83
    global b93
    global play1
    global play2
    global play3
    global play4
    global play5
    global play6
    global play7
    global play8
    global play9
    global morpion1
    global morpion2
    global morpion3
    global morpion4
    global morpion5
    global morpion6
    global morpion7
    global morpion8
    global morpion9
    global wUserL1
    global wUserL2
    global wUserL3
    global wUserC1
    global wUserC2
    global wUserC3
    global wUserD1
    global wUserD2
    global wBotL1
    global wBotL2
    global wBotL3
    global wBotC1
    global wBotC2
    global wBotC3
    global wBotD1
    global wBotD2
    global check1
    global check2
    global check3
    global check4
    global check5
    global check6
    global check7
    global check8
    global check9

    # ligne
    l1 = [b13, b23, b33]
    l2 = [b43, b53, b63]
    l3 = [b73, b83, b93]
    # column
    c1 = [b13, b43, b73]
    c2 = [b23, b53, b83]
    c3 = [b33, b63, b93]
    # diagonal
    d1 = [b13, b53, b93]
    d2 = [b33, b53, b73]

    # user
    if all([a['text'] == 'X' for a in l1]) and check3 == False:
        check3 = True
        for a in l1:
            a.config(bg='green')
            for e in morpion3:
                morpionFinish3.append(e)
        wUserL1.append("win")
        wUserC3.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in l2]) and check3 == False:
        check3 = True
        for a in l2:
            a.config(bg='green')
            for e in morpion3:
                morpionFinish3.append(e)
        wUserL1.append("win")
        wUserC3.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in l3]) and check3 == False:
        check3 = True
        for a in l3:
            a.config(bg='green')
            for e in morpion3:
                morpionFinish3.append(e)
        wUserL1.append("win")
        wUserC3.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in c1]) and check3 == False:
        check3 = True
        for a in c1:
            a.config(bg='green')
            for e in morpion3:
                morpionFinish3.append(e)
        wUserL1.append("win")
        wUserC3.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in c2]) and check3 == False:
        check3 = True
        for a in c2:
            a.config(bg='green')
            for e in morpion3:
                morpionFinish3.append(e)
        wUserL1.append("win")
        wUserC3.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in c3]) and check3 == False:
        check3 = True
        for a in c3:
            a.config(bg='green')
            for e in morpion3:
                morpionFinish3.append(e)
        wUserL1.append("win")
        wUserC3.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in d1]) and check3 == False:
        check3 = True
        for a in d1:
            a.config(bg='green')
            for e in morpion3:
                morpionFinish3.append(e)
        wUserL1.append("win")
        wUserC3.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in d2]) and check3 == False:
        check3 = True
        for a in d2:
            a.config(bg='green')
            for e in morpion3:
                morpionFinish3.append(e)
        wUserL1.append("win")
        wUserC3.append("win")
        wUserD2.append("win")

        return True

    # bot
    elif all([a['text'] == 'O' for a in l1]) and check3 == False:
        check3 = True
        for a in l1:
            a.config(bg='red')
            for e in morpion3:
                morpionFinish3.append(e)
        wBotL1.append("win")
        wBotC3.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in l2]) and check3 == False:
        check3 = True
        for a in l2:
            a.config(bg='red')
            for e in morpion3:
                morpionFinish3.append(e)
        wBotL1.append("win")
        wBotC3.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in l3]) and check3 == False:
        check3 = True
        for a in l3:
            a.config(bg='red')
            for e in morpion3:
                morpionFinish3.append(e)
        wBotL1.append("win")
        wBotC3.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in c1]) and check3 == False:
        check3 = True
        for a in c1:
            a.config(bg='red')
            for e in morpion3:
                morpionFinish3.append(e)
        wBotL1.append("win")
        wBotC3.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in c2]) and check3 == False:
        check3 = True
        for a in c2:
            a.config(bg='red')
            for e in morpion3:
                morpionFinish3.append(e)
        wBotL1.append("win")
        wBotC3.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in c3]) and check3 == False:
        check3 = True
        for a in c3:
            a.config(bg='red')
            for e in morpion3:
                morpionFinish3.append(e)
        wBotL1.append("win")
        wBotC3.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in d1]) and check3 == False:
        check3 = True
        for a in d1:
            a.config(bg='red')
            for e in morpion3:
                morpionFinish3.append(e)
        wBotL1.append("win")
        wBotC3.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in d2]) and check3 == False:
        check3 = True
        for a in d2:
            a.config(bg='red')
            for e in morpion3:
                morpionFinish3.append(e)
        wBotL1.append("win")
        wBotC3.append("win")
        wBotD2.append("win")

        return True

        # draw

    elif all([a['text'] != ' ' for a in morpion3]) and check3 == False:
        check3 = True
        return True

    else:
        return False

def WinMorpion4():
    global b14
    global b24
    global b34
    global b44
    global b54
    global b64
    global b74
    global b84
    global b94
    global play1
    global play2
    global play3
    global play4
    global play5
    global play6
    global play7
    global play8
    global play9
    global morpion1
    global morpion2
    global morpion3
    global morpion4
    global morpion5
    global morpion6
    global morpion7
    global morpion8
    global morpion9
    global wUserL1
    global wUserL2
    global wUserL3
    global wUserC1
    global wUserC2
    global wUserC3
    global wUserD1
    global wUserD2
    global wBotL1
    global wBotL2
    global wBotL3
    global wBotC1
    global wBotC2
    global wBotC3
    global wBotD1
    global wBotD2
    global check1
    global check2
    global check3
    global check4
    global check5
    global check6
    global check7
    global check8
    global check9

    # ligne
    l1 = [b14, b24, b34]
    l2 = [b44, b54, b64]
    l3 = [b74, b84, b94]
    # column
    c1 = [b14, b44, b74]
    c2 = [b24, b54, b84]
    c3 = [b34, b64, b94]
    # diagonal
    d1 = [b14, b54, b94]
    d2 = [b34, b54, b74]

    # user
    if all([a['text'] == 'X' for a in l1]) and check4 == False:
        check4 = True
        for a in l1:
            a.config(bg='green')
            for e in morpion4:
                morpionFinish4.append(e)
        wUserL2.append("win")
        wUserC1.append("win")

        return True

    elif all([a['text'] == 'X' for a in l2]) and check4 == False:
        check4 = True
        for a in l2:
            a.config(bg='green')
            for e in morpion4:
                morpionFinish4.append(e)
        wUserL2.append("win")
        wUserC1.append("win")

        return True

    elif all([a['text'] == 'X' for a in l3]) and check4 == False:
        check4 = True
        for a in l3:
            a.config(bg='green')
            for e in morpion4:
                morpionFinish4.append(e)
        wUserL2.append("win")
        wUserC1.append("win")

        return True

    elif all([a['text'] == 'X' for a in c1]) and check4 == False:
        check4 = True
        for a in c1:
            a.config(bg='green')
            for e in morpion4:
                morpionFinish4.append(e)
        wUserL2.append("win")
        wUserC1.append("win")

        return True

    elif all([a['text'] == 'X' for a in c2]) and check4 == False:
        check4 = True
        for a in c2:
            a.config(bg='green')
            for e in morpion4:
                morpionFinish4.append(e)
        wUserL2.append("win")
        wUserC1.append("win")

        return True

    elif all([a['text'] == 'X' for a in c3]) and check4 == False:
        check4 = True
        for a in c3:
            a.config(bg='green')
            for e in morpion4:
                morpionFinish4.append(e)
        wUserL2.append("win")
        wUserC1.append("win")

        return True

    elif all([a['text'] == 'X' for a in d1]) and check4 == False:
        check4 = True
        for a in d1:
            a.config(bg='green')
            for e in morpion4:
                morpionFinish4.append(e)
        wUserL2.append("win")
        wUserC1.append("win")
        return True

    elif all([a['text'] == 'X' for a in d2]) and check4 == False:
        check4 = True
        for a in d2:
            a.config(bg='green')
            for e in morpion4:
                morpionFinish4.append(e)
        wUserL2.append("win")
        wUserC1.append("win")
        return True

    # bot
    elif all([a['text'] == 'O' for a in l1]) and check4 == False:
        check4 = True
        for a in l1:
            a.config(bg='red')
            for e in morpion4:
                morpionFinish4.append(e)
        wBotL2.append("win")
        wBotC1.append("win")
        return True

    elif all([a['text'] == 'O' for a in l2]) and check4 == False:
        check4 = True
        for a in l2:
            a.config(bg='red')
            for e in morpion4:
                morpionFinish4.append(e)
        wBotL2.append("win")
        wBotC1.append("win")

        return True

    elif all([a['text'] == 'O' for a in l3]) and check4 == False:
        check4 = True
        for a in l3:
            a.config(bg='red')
            for e in morpion4:
                morpionFinish4.append(e)
        wBotL2.append("win")
        wBotC1.append("win")

        return True

    elif all([a['text'] == 'O' for a in c1]) and check4 == False:
        check4 = True
        for a in c1:
            a.config(bg='red')
            for e in morpion4:
                morpionFinish4.append(e)
        wBotL2.append("win")
        wBotC1.append("win")

        return True

    elif all([a['text'] == 'O' for a in c2]) and check4 == False:
        check4 = True
        for a in c2:
            a.config(bg='red')
            for e in morpion4:
                morpionFinish4.append(e)
        wBotL2.append("win")
        wBotC1.append("win")
        return True

    elif all([a['text'] == 'O' for a in c3]) and check4 == False:
        check4 = True
        for a in c3:
            a.config(bg='red')
            for e in morpion4:
                morpionFinish4.append(e)
        wBotL2.append("win")
        wBotC1.append("win")

        return True

    elif all([a['text'] == 'O' for a in d1]) and check4 == False:
        check4 = True
        for a in d1:
            a.config(bg='red')
            for e in morpion4:
                morpionFinish4.append(e)
        wBotL2.append("win")
        wBotC1.append("win")

        return True

    elif all([a['text'] == 'O' for a in d2]) and check4 == False:
        check4 = True
        for a in d2:
            a.config(bg='red')
            for e in morpion4:
                morpionFinish4.append(e)
        wBotL2.append("win")
        wBotC1.append("win")
        return True

    # draw
    elif all([a['text'] != ' ' for a in morpion4]) and check4 == False:
        check4 = True
        return True

    else:
        return False

def WinMorpion5():
    global b15
    global b25
    global b35
    global b45
    global b55
    global b65
    global b75
    global b85
    global b95
    global play1
    global play2
    global play3
    global play4
    global play5
    global play6
    global play7
    global play8
    global play9
    global morpion1
    global morpion2
    global morpion3
    global morpion4
    global morpion5
    global morpion6
    global morpion7
    global morpion8
    global morpion9
    global wUserL1
    global wUserL2
    global wUserL3
    global wUserC1
    global wUserC2
    global wUserC3
    global wUserD1
    global wUserD2
    global wBotL1
    global wBotL2
    global wBotL3
    global wBotC1
    global wBotC2
    global wBotC3
    global wBotD1
    global wBotD2
    global check1
    global check2
    global check3
    global check4
    global check5
    global check6
    global check7
    global check8
    global check9

    # ligne
    l1 = [b15, b25, b35]
    l2 = [b45, b55, b65]
    l3 = [b75, b85, b95]
    # column
    c1 = [b15, b45, b75]
    c2 = [b25, b55, b85]
    c3 = [b35, b65, b95]
    # diagonal
    d1 = [b15, b55, b95]
    d2 = [b35, b55, b75]

    # user
    if all([a['text'] == 'X' for a in l1]) and check5 == False:
        check5 = True
        for a in l1:
            a.config(bg='green')
            for e in morpion5:
                morpionFinish5.append(e)
        wUserL2.append("win")
        wUserC2.append("win")
        wUserD1.append("win")
        wUserD2.append("win")
        return True

    elif all([a['text'] == 'X' for a in l2]) and check5 == False:
        check5 = True
        for a in l2:
            a.config(bg='green')
            for e in morpion5:
                morpionFinish5.append(e)
        wUserL2.append("win")
        wUserC2.append("win")
        wUserD1.append("win")
        wUserD2.append("win")
        return True

    elif all([a['text'] == 'X' for a in l3]) and check5 == False:
        check5 = True
        for a in l3:
            a.config(bg='green')
            for e in morpion5:
                morpionFinish5.append(e)
        wUserL2.append("win")
        wUserC2.append("win")
        wUserD1.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in c1]) and check5 == False:
        check5 = True
        for a in c1:
            a.config(bg='green')
            for e in morpion5:
                morpionFinish5.append(e)
        wUserL2.append("win")
        wUserC2.append("win")
        wUserD1.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in c2]) and check5 == False:
        check5 = True
        for a in c2:
            a.config(bg='green')
            for e in morpion5:
                morpionFinish5.append(e)
        wUserL2.append("win")
        wUserC2.append("win")
        wUserD1.append("win")
        wUserD2.append("win")
        return True

    elif all([a['text'] == 'X' for a in c3]) and check5 == False:
        check5 = True
        for a in c3:
            a.config(bg='green')
            for e in morpion5:
                morpionFinish5.append(e)
        wUserL2.append("win")
        wUserC2.append("win")
        wUserD1.append("win")
        wUserD2.append("win")
        return True

    elif all([a['text'] == 'X' for a in d1]) and check5 == False:
        check5 = True
        for a in d1:
            a.config(bg='green')
            for e in morpion5:
                morpionFinish5.append(e)
        wUserL2.append("win")
        wUserC2.append("win")
        wUserD1.append("win")
        wUserD2.append("win")
        return True

    elif all([a['text'] == 'X' for a in d2]) and check5 == False:
        check5 = True
        for a in d2:
            a.config(bg='green')
            for e in morpion5:
                morpionFinish5.append(e)
        wUserL2.append("win")
        wUserC2.append("win")
        wUserD1.append("win")
        wUserD2.append("win")

        return True

    # bot
    elif all([a['text'] == 'O' for a in l1]) and check5 == False:
        check5 = True
        for a in l1:
            a.config(bg='red')
            for e in morpion5:
                morpionFinish5.append(e)
        wBotL2.append("win")
        wBotC2.append("win")
        wBotD1.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in l2]) and check5 == False:
        check5 = True
        for a in l2:
            a.config(bg='red')
            for e in morpion5:
                morpionFinish5.append(e)
        wBotL2.append("win")
        wBotC2.append("win")
        wBotD1.append("win")
        wBotD2.append("win")
        return True

    elif all([a['text'] == 'O' for a in l3]) and check5 == False:
        check5 = True
        for a in l3:
            a.config(bg='red')
            for e in morpion5:
                morpionFinish5.append(e)
        wBotL2.append("win")
        wBotC2.append("win")
        wBotD1.append("win")
        wBotD2.append("win")
        return True

    elif all([a['text'] == 'O' for a in c1]) and check5 == False:
        check5 = True
        for a in c1:
            a.config(bg='red')
            for e in morpion5:
                morpionFinish5.append(e)
        wBotL2.append("win")
        wBotC2.append("win")
        wBotD1.append("win")
        wBotD2.append("win")
        return True

    elif all([a['text'] == 'O' for a in c2]) and check5 == False:
        check5 = True
        for a in c2:
            a.config(bg='red')
            for e in morpion5:
                morpionFinish5.append(e)
        wBotL2.append("win")
        wBotC2.append("win")
        wBotD1.append("win")
        wBotD2.append("win")
        return True

    elif all([a['text'] == 'O' for a in c3]) and check5 == False:
        check5 = True
        for a in c3:
            a.config(bg='red')
            for e in morpion5:
                morpionFinish5.append(e)
        wBotL2.append("win")
        wBotC2.append("win")
        wBotD1.append("win")
        wBotD2.append("win")
        return True

    elif all([a['text'] == 'O' for a in d1]) and check5 == False:
        check5 = True
        for a in d1:
            a.config(bg='red')
            for e in morpion5:
                morpionFinish5.append(e)
        wBotL2.append("win")
        wBotC2.append("win")
        wBotD1.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in d2]) and check5 == False:
        check5 = True
        for a in d2:
            a.config(bg='red')
            for e in morpion5:
                morpionFinish5.append(e)
        wBotL2.append("win")
        wBotC2.append("win")
        wBotD1.append("win")
        wBotD2.append("win")

        return True

        # draw

    elif all([a['text'] != ' ' for a in morpion5]) and check5 == False:
        check5 = True
        return True

    else:
        return False

def WinMorpion6():
    global b16
    global b26
    global b36
    global b46
    global b56
    global b66
    global b76
    global b86
    global b96
    global play1
    global play2
    global play3
    global play4
    global play5
    global play6
    global play7
    global play8
    global play9
    global morpion1
    global morpion2
    global morpion3
    global morpion4
    global morpion5
    global morpion6
    global morpion7
    global morpion8
    global morpion9
    global wUserL1
    global wUserL2
    global wUserL3
    global wUserC1
    global wUserC2
    global wUserC3
    global wUserD1
    global wUserD2
    global wBotL1
    global wBotL2
    global wBotL3
    global wBotC1
    global wBotC2
    global wBotC3
    global wBotD1
    global wBotD2
    global check1
    global check2
    global check3
    global check4
    global check5
    global check6
    global check7
    global check8
    global check9

    # ligne
    l1 = [b16, b26, b36]
    l2 = [b46, b56, b66]
    l3 = [b76, b86, b96]
    # column
    c1 = [b16, b46, b76]
    c2 = [b26, b56, b86]
    c3 = [b36, b66, b96]
    # diagonal
    d1 = [b16, b56, b96]
    d2 = [b36, b56, b76]

    # user
    if all([a['text'] == 'X' for a in l1]) and check6 == False:
        check6 = True
        for a in l1:
            a.config(bg='green')
            for e in morpion6:
                morpionFinish6.append(e)
        wUserL2.append("win")
        wUserC3.append("win")

        return True

    elif all([a['text'] == 'X' for a in l2]) and check6 == False:
        check6 = True
        for a in l2:
            a.config(bg='green')
            for e in morpion6:
                morpionFinish6.append(e)
        wUserL2.append("win")
        wUserC3.append("win")

        return True

    elif all([a['text'] == 'X' for a in l3]) and check6 == False:
        check6 = True
        for a in l3:
            a.config(bg='green')
            for e in morpion6:
                morpionFinish6.append(e)
        wUserL2.append("win")
        wUserC3.append("win")

        return True

    elif all([a['text'] == 'X' for a in c1]) and check6 == False:
        check6 = True
        for a in c1:
            a.config(bg='green')
            for e in morpion6:
                morpionFinish6.append(e)
        wUserL2.append("win")
        wUserC3.append("win")
        return True

    elif all([a['text'] == 'X' for a in c2]) and check6 == False:
        check6 = True
        for a in c2:
            a.config(bg='green')
            for e in morpion6:
                morpionFinish6.append(e)
        wUserL2.append("win")
        wUserC3.append("win")
        return True

    elif all([a['text'] == 'X' for a in c3]) and check6 == False:
        check6 = True
        for a in c3:
            a.config(bg='green')
            for e in morpion6:
                morpionFinish6.append(e)
        wUserL2.append("win")
        wUserC3.append("win")
        return True

    elif all([a['text'] == 'X' for a in d1]) and check6 == False:
        check6 = True
        for a in d1:
            a.config(bg='green')
            for e in morpion6:
                morpionFinish6.append(e)
        wUserL2.append("win")
        wUserC3.append("win")
        return True

    elif all([a['text'] == 'X' for a in d2]) and check6 == False:
        check6 = True
        for a in d2:
            a.config(bg='green')
            for e in morpion6:
                morpionFinish6.append(e)
        wUserL2.append("win")
        wUserC3.append("win")
        return True

    # bot
    elif all([a['text'] == 'O' for a in l1]) and check6 == False:
        check6 = True
        for a in l1:
            a.config(bg='red')
            for e in morpion6:
                morpionFinish6.append(e)
        wBotL2.append("win")
        wBotC3.append("win")
        return True

    elif all([a['text'] == 'O' for a in l2]) and check6 == False:
        check6 = True
        for a in l2:
            a.config(bg='red')
            for e in morpion6:
                morpionFinish6.append(e)
        wBotL2.append("win")
        wBotC3.append("win")
        return True

    elif all([a['text'] == 'O' for a in l3]) and check6 == False:
        check6 = True
        for a in l3:
            a.config(bg='red')
            for e in morpion6:
                morpionFinish6.append(e)
        wBotL2.append("win")
        wBotC3.append("win")
        return True

    elif all([a['text'] == 'O' for a in c1]) and check6 == False:
        check6 = True
        for a in c1:
            a.config(bg='red')
            for e in morpion6:
                morpionFinish6.append(e)
        wBotL2.append("win")
        wBotC3.append("win")
        return True

    elif all([a['text'] == 'O' for a in c2]) and check6 == False:
        check6 = True
        for a in c2:
            a.config(bg='red')
            for e in morpion6:
                morpionFinish6.append(e)
        wBotL2.append("win")
        wBotC3.append("win")
        return True

    elif all([a['text'] == 'O' for a in c3]) and check6 == False:
        check6 = True
        for a in c3:
            a.config(bg='red')
            for e in morpion6:
                morpionFinish6.append(e)
        wBotL2.append("win")
        wBotC3.append("win")
        return True

    elif all([a['text'] == 'O' for a in d1]) and check6 == False:
        check6 = True
        for a in d1:
            a.config(bg='red')
            for e in morpion6:
                morpionFinish6.append(e)
        wBotL2.append("win")
        wBotC3.append("win")

        return True

    elif all([a['text'] == 'O' for a in d2]) and check6 == False:
        check6 = True
        for a in d2:
            a.config(bg='red')
            for e in morpion6:
                morpionFinish6.append(e)
        wBotL2.append("win")
        wBotC3.append("win")

        return True

        # draw

    elif all([a['text'] != ' ' for a in morpion6]) and check6 == False:
        check6 = True
        return True

    else:
        return False

def WinMorpion7():
    global b17
    global b27
    global b37
    global b47
    global b57
    global b67
    global b77
    global b87
    global b97
    global play1
    global play2
    global play3
    global play4
    global play5
    global play6
    global play7
    global play8
    global play9
    global morpion1
    global morpion2
    global morpion3
    global morpion4
    global morpion5
    global morpion6
    global morpion7
    global morpion8
    global morpion9
    global wUserL1
    global wUserL2
    global wUserL3
    global wUserC1
    global wUserC2
    global wUserC3
    global wUserD1
    global wUserD2
    global wBotL1
    global wBotL2
    global wBotL3
    global wBotC1
    global wBotC2
    global wBotC3
    global wBotD1
    global wBotD2
    global check1
    global check2
    global check3
    global check4
    global check5
    global check6
    global check7
    global check8
    global check9

    # ligne
    l1 = [b17, b27, b37]
    l2 = [b47, b57, b67]
    l3 = [b77, b87, b97]
    # column
    c1 = [b17, b47, b77]
    c2 = [b27, b57, b87]
    c3 = [b37, b67, b97]

    # diagonal
    d1 = [b17, b57, b97]
    d2 = [b37, b57, b77]

    # user
    if all([a['text'] == 'X' for a in l1]) and check7 == False:
        check7 = True
        for a in l1:
            a.config(bg='green')
            for e in morpion7:
                morpionFinish7.append(e)
        wUserL3.append("win")
        wUserC1.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in l2]) and check7 == False:
        check7 = True
        for a in l2:
            a.config(bg='green')
            for e in morpion7:
                morpionFinish7.append(e)
        wUserL3.append("win")
        wUserC1.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in l3]) and check7 == False:
        check7 = True
        for a in l3:
            a.config(bg='green')
            for e in morpion7:
                morpionFinish7.append(e)
        wUserL3.append("win")
        wUserC1.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in c1]) and check7 == False:
        check7 = True
        for a in c1:
            a.config(bg='green')
            for e in morpion7:
                morpionFinish7.append(e)
        wUserL3.append("win")
        wUserC1.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in c2]) and check7 == False:
        check7 = True
        for a in c2:
            a.config(bg='green')
            for e in morpion7:
                morpionFinish7.append(e)
        wUserL3.append("win")
        wUserC1.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in c3]) and check7 == False:
        check7 = True
        for a in c3:
            a.config(bg='green')
            for e in morpion7:
                morpionFinish7.append(e)
        wUserL3.append("win")
        wUserC1.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in d1]) and check7 == False:
        check7 = True
        for a in d1:
            a.config(bg='green')
            for e in morpion7:
                morpionFinish7.append(e)
        wUserL3.append("win")
        wUserC1.append("win")
        wUserD2.append("win")

        return True

    elif all([a['text'] == 'X' for a in d2]) and check7 == False:
        check7 = True
        for a in d2:
            a.config(bg='green')
            for e in morpion7:
                morpionFinish7.append(e)
        wUserL3.append("win")
        wUserC1.append("win")
        wUserD2.append("win")

        return True

    # bot
    elif all([a['text'] == 'O' for a in l1]) and check7 == False:
        check7 = True
        for a in l1:
            a.config(bg='red')
            for e in morpion7:
                morpionFinish7.append(e)
        wBotL3.append("win")
        wBotC1.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in l2]) and check7 == False:
        check7 = True
        for a in l2:
            a.config(bg='red')
            for e in morpion7:
                morpionFinish7.append(e)
        wBotL3.append("win")
        wBotC1.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in l3]) and check7 == False:
        check7 = True
        for a in l3:
            a.config(bg='red')
            for e in morpion7:
                morpionFinish7.append(e)
        wBotL3.append("win")
        wBotC1.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in c1]) and check7 == False:
        check7 = True
        for a in c1:
            a.config(bg='red')
            for e in morpion7:
                morpionFinish7.append(e)
        wBotL3.append("win")
        wBotC1.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in c2]) and check7 == False:
        check7 = True
        for a in c2:
            a.config(bg='red')
            for e in morpion7:
                morpionFinish7.append(e)
        wBotL3.append("win")
        wBotC1.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in c3]) and check7 == False:
        check7 = True
        for a in c3:
            a.config(bg='red')
            for e in morpion7:
                morpionFinish7.append(e)
        wBotL3.append("win")
        wBotC1.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in d1]) and check7 == False:
        check7 = True
        for a in d1:
            a.config(bg='red')
            for e in morpion7:
                morpionFinish7.append(e)
        wBotL3.append("win")
        wBotC1.append("win")
        wBotD2.append("win")

        return True

    elif all([a['text'] == 'O' for a in d2]) and check7 == False:
        check7 = True
        for a in d2:
            a.config(bg='red')
            for e in morpion7:
                morpionFinish7.append(e)
        wBotL3.append("win")
        wBotC1.append("win")
        wBotD2.append("win")

        return True

        # draw

    elif all([a['text'] != ' ' for a in morpion7]) and check7 == False:
        check7 = True
        return True

    else:
        return False

def WinMorpion8():
    global b18
    global b28
    global b38
    global b48
    global b58
    global b68
    global b78
    global b88
    global b98
    global play1
    global play2
    global play3
    global play4
    global play5
    global play6
    global play7
    global play8
    global play9
    global morpion1
    global morpion2
    global morpion3
    global morpion4
    global morpion5
    global morpion6
    global morpion7
    global morpion8
    global morpion9
    global wUserL1
    global wUserL2
    global wUserL3
    global wUserC1
    global wUserC2
    global wUserC3
    global wUserD1
    global wUserD2
    global wBotL1
    global wBotL2
    global wBotL3
    global wBotC1
    global wBotC2
    global wBotC3
    global wBotD1
    global wBotD2
    global check1
    global check2
    global check3
    global check4
    global check5
    global check6
    global check7
    global check8
    global check9

    # ligne
    l1 = [b18, b28, b38]
    l2 = [b48, b58, b68]
    l3 = [b78, b88, b98]
    # column
    c1 = [b18, b48, b78]
    c2 = [b28, b58, b88]
    c3 = [b38, b68, b98]

    # diagonal
    d1 = [b18, b58, b98]
    d2 = [b38, b58, b78]

    # user
    if all([a['text'] == 'X' for a in l1]) and check8 == False:
        check8 = True
        for a in l1:
            a.config(bg='green')
            for e in morpion8:
                morpionFinish8.append(e)
        wUserL3.append("win")
        wUserC2.append("win")

        return True

    elif all([a['text'] == 'X' for a in l2]) and check8 == False:
        check8 = True
        for a in l2:
            a.config(bg='green')
            for e in morpion8:
                morpionFinish8.append(e)
        wUserL3.append("win")
        wUserC2.append("win")

        return True

    elif all([a['text'] == 'X' for a in l3]) and check8 == False:
        check8 = True
        for a in l3:
            a.config(bg='green')
            for e in morpion8:
                morpionFinish8.append(e)
        wUserL3.append("win")
        wUserC2.append("win")

        return True

    elif all([a['text'] == 'X' for a in c1]) and check8 == False:
        check8 = True
        for a in c1:
            a.config(bg='green')
            for e in morpion8:
                morpionFinish8.append(e)
        wUserL3.append("win")
        wUserC2.append("win")

        return True

    elif all([a['text'] == 'X' for a in c2]) and check8 == False:
        check8 = True
        for a in c2:
            a.config(bg='green')
            for e in morpion8:
                morpionFinish8.append(e)
        wUserL3.append("win")
        wUserC2.append("win")

        return True

    elif all([a['text'] == 'X' for a in c3]) and check8 == False:
        check8 = True
        for a in c3:
            a.config(bg='green')
            for e in morpion8:
                morpionFinish8.append(e)
        wUserL3.append("win")
        wUserC2.append("win")

        return True

    elif all([a['text'] == 'X' for a in d1]) and check8 == False:
        check8 = True
        for a in d1:
            a.config(bg='green')
            for e in morpion8:
                morpionFinish8.append(e)
        wUserL3.append("win")
        wUserC2.append("win")

        return True

    elif all([a['text'] == 'X' for a in d2]) and check8 == False:
        check8 = True
        for a in d2:
            a.config(bg='green')
            for e in morpion8:
                morpionFinish8.append(e)
        wUserL3.append("win")
        wUserC2.append("win")

        return True

    # bot
    elif all([a['text'] == 'O' for a in l1]) and check8 == False:
        check8 = True
        for a in l1:
            a.config(bg='red')
            for e in morpion8:
                morpionFinish8.append(e)
        wBotL3.append("win")
        wBotC2.append("win")

        return True

    elif all([a['text'] == 'O' for a in l2]) and check8 == False:
        check8 = True
        for a in l2:
            a.config(bg='red')
            for e in morpion8:
                morpionFinish8.append(e)
        wBotL3.append("win")
        wBotC2.append("win")

        return True

    elif all([a['text'] == 'O' for a in l3]) and check8 == False:
        check8 = True
        for a in l3:
            a.config(bg='red')
            for e in morpion8:
                morpionFinish8.append(e)
        wBotL3.append("win")
        wBotC2.append("win")

        return True

    elif all([a['text'] == 'O' for a in c1]) and check8 == False:
        check8 = True
        for a in c1:
            a.config(bg='red')
            for e in morpion8:
                morpionFinish8.append(e)
        wBotL3.append("win")
        wBotC2.append("win")

        return True

    elif all([a['text'] == 'O' for a in c2]) and check8 == False:
        check8 = True
        for a in c2:
            a.config(bg='red')
            for e in morpion8:
                morpionFinish8.append(e)
        wBotL3.append("win")
        wBotC2.append("win")

        return True

    elif all([a['text'] == 'O' for a in c3]) and check8 == False:
        check8 = True
        for a in c3:
            a.config(bg='red')
            for e in morpion8:
                morpionFinish8.append(e)
        wBotL3.append("win")
        wBotC2.append("win")

        return True

    elif all([a['text'] == 'O' for a in d1]) and check8 == False:
        check8 = True
        for a in d1:
            a.config(bg='red')
            for e in morpion8:
                morpionFinish8.append(e)
        wBotL3.append("win")
        wBotC2.append("win")

        return True

    elif all([a['text'] == 'O' for a in d2]) and check8 == False:
        check8 = True
        for a in d2:
            a.config(bg='red')
            for e in morpion8:
                morpionFinish8.append(e)
        wBotL3.append("win")
        wBotC2.append("win")

        return True

    # draw
    elif all([a['text'] != ' ' for a in morpion8]) and check8 == False:
        check8 = True
        return True

    else:
        return False

def WinMorpion9():
    global b19
    global b29
    global b39
    global b49
    global b59
    global b69
    global b79
    global b89
    global b99
    global play1
    global play2
    global play3
    global play4
    global play5
    global play6
    global play7
    global play8
    global play9
    global morpion1
    global morpion2
    global morpion3
    global morpion4
    global morpion5
    global morpion6
    global morpion7
    global morpion8
    global morpion9
    global wUserL1
    global wUserL2
    global wUserL3
    global wUserC1
    global wUserC2
    global wUserC3
    global wUserD1
    global wUserD2
    global wBotL1
    global wBotL2
    global wBotL3
    global wBotC1
    global wBotC2
    global wBotC3
    global wBotD1
    global wBotD2
    global check1
    global check2
    global check3
    global check4
    global check5
    global check6
    global check7
    global check8
    global check9

    # ligne
    l1 = [b19, b29, b39]
    l2 = [b49, b59, b69]
    l3 = [b79, b89, b99]
    # column
    c1 = [b19, b49, b79]
    c2 = [b29, b59, b89]
    c3 = [b39, b69, b99]

    # diagonal
    d1 = [b19, b59, b99]
    d2 = [b39, b59, b79]

    # user
    if all([a['text'] == 'X' for a in l1]) and check9 == False:
        check9 = True
        for a in l1:
            a.config(bg='green')
            for e in morpion9:
                morpionFinish9.append(e)
        wUserL3.append("win")
        wUserC3.append("win")
        wUserD1.append("win")

        return True

    elif all([a['text'] == 'X' for a in l2]) and check9 == False:
        check9 = True
        for a in l2:
            a.config(bg='green')
            for e in morpion9:
                morpionFinish9.append(e)
        wUserL3.append("win")
        wUserC3.append("win")
        wUserD1.append("win")

        return True

    elif all([a['text'] == 'X' for a in l3]) and check9 == False:
        check9 = True
        for a in l3:
            a.config(bg='green')
            for e in morpion9:
                morpionFinish9.append(e)
        wUserL3.append("win")
        wUserC3.append("win")
        wUserD1.append("win")

        return True

    elif all([a['text'] == 'X' for a in c1]) and check9 == False:
        check9 = True
        for a in c1:
            a.config(bg='green')
            for e in morpion9:
                morpionFinish9.append(e)
        wUserL3.append("win")
        wUserC3.append("win")
        wUserD1.append("win")

        return True

    elif all([a['text'] == 'X' for a in c2]) and check9 == False:
        check9 = True
        for a in c2:
            a.config(bg='green')
            for e in morpion9:
                morpionFinish9.append(e)
        wUserL3.append("win")
        wUserC3.append("win")
        wUserD1.append("win")

        return True

    elif all([a['text'] == 'X' for a in c3]) and check9 == False:
        check9 = True
        for a in c3:
            a.config(bg='green')
            for e in morpion9:
                morpionFinish9.append(e)
        wUserL3.append("win")
        wUserC3.append("win")
        wUserD1.append("win")

        return True

    elif all([a['text'] == 'X' for a in d1]) and check9 == False:
        check9 = True
        for a in d1:
            a.config(bg='green')
            for e in morpion9:
                morpionFinish9.append(e)
        wUserL3.append("win")
        wUserC3.append("win")
        wUserD1.append("win")

        return True

    elif all([a['text'] == 'X' for a in d2]) and check9 == False:
        check9 = True
        for a in d2:
            a.config(bg='green')
            for e in morpion9:
                morpionFinish9.append(e)
        wUserL3.append("win")
        wUserC3.append("win")
        wUserD1.append("win")

        return True

    # bot
    elif all([a['text'] == 'O' for a in l1]) and check9 == False:
        check9 = True
        for a in l1:
            a.config(bg='red')
            for e in morpion9:
                morpionFinish9.append(e)
        wBotL3.append("win")
        wBotC3.append("win")
        wBotD1.append("win")

        return True

    elif all([a['text'] == 'O' for a in l2]) and check9 == False:
        check9 = True
        for a in l2:
            a.config(bg='red')
            for e in morpion9:
                morpionFinish9.append(e)
        wBotL3.append("win")
        wBotC3.append("win")
        wBotD1.append("win")

        return True

    elif all([a['text'] == 'O' for a in l3]) and check9 == False:
        check9 = True
        for a in l3:
            a.config(bg='red')
            for e in morpion9:
                morpionFinish9.append(e)
        wBotL3.append("win")
        wBotC3.append("win")
        wBotD1.append("win")

        return True

    elif all([a['text'] == 'O' for a in c1]) and check9 == False:
        check9 = True
        for a in c1:
            a.config(bg='red')
            for e in morpion9:
                morpionFinish9.append(e)
        wBotL3.append("win")
        wBotC3.append("win")
        wBotD1.append("win")

        return True

    elif all([a['text'] == 'O' for a in c2]) and check9 == False:
        check9 = True
        for a in c2:
            a.config(bg='red')
            for e in morpion9:
                morpionFinish9.append(e)
        wBotL3.append("win")
        wBotC3.append("win")
        wBotD1.append("win")

        return True

    elif all([a['text'] == 'O' for a in c3]) and check9 == False:
        check9 = True
        for a in c3:
            a.config(bg='red')
            for e in morpion9:
                morpionFinish9.append(e)
        wBotL3.append("win")
        wBotC3.append("win")
        wBotD1.append("win")

        return True

    elif all([a['text'] == 'O' for a in d1]) and check9 == False:
        check9 = True
        for a in d1:
            a.config(bg='red')
            for e in morpion9:
                morpionFinish9.append(e)
        wBotL3.append("win")
        wBotC3.append("win")
        wBotD1.append("win")

        return True

    elif all([a['text'] == 'O' for a in d2]) and check9 == False:
        check9 = True
        for a in d2:
            a.config(bg='red')
            for e in morpion9:
                morpionFinish9.append(e)
        wBotL3.append("win")
        wBotC3.append("win")
        wBotD1.append("win")

        return True

    # draw
    elif all([a['text'] != ' ' for a in morpion9]) and check9 == False:
        check9 = True
        return True

    else:
        return False

def winnerIs():
    global click
    global morpion1
    global morpion2
    global morpion3
    global morpion4
    global morpion5
    global morpion6
    global morpion7
    global morpion8
    global morpion9
    global winnerVar

    if (len(wUserL1) == 3 or len(wUserL2) == 3 or len(wUserL3) == 3
            or len(wUserC1) == 3 or len(wUserC2) == 3 or len(wUserC3) == 3
            or len(wUserD1) == 3 or len(wUserD2) == 3):
        print("ta gagner")
        winnerVar["text"] = pseudo
        pygame.mixer.init()
        pygame.mixer.music.load('./sound/voice/1round/victoire1-0.ogg')
        pygame.mixer.music.play()
        for a in morpion1:
            a['state'] = 'disabled'
            a.config(bg='green')
        for a in morpion2:
            a['state'] = 'disabled'
            a.config(bg='green')
        for a in morpion3:
            a['state'] = 'disabled'
            a.config(bg='green')
        for a in morpion4:
            a['state'] = 'disabled'
            a.config(bg='green')
        for a in morpion5:
            a['state'] = 'disabled'
            a.config(bg='green')
        for a in morpion6:
            a['state'] = 'disabled'
            a.config(bg='green')
        for a in morpion7:
            a['state'] = 'disabled'
            a.config(bg='green')
        for a in morpion8:
            a['state'] = 'disabled'
            a.config(bg='green')
        for a in morpion9:
            a['state'] = 'disabled'
            a.config(bg='green')
        click = False

        return True

    elif (len(wBotL1) == 3 or len(wBotL2) == 3 or len(wBotL3) == 3
            or len(wBotC1) == 3 or len(wBotC2) == 3 or len(wBotC3) == 3
            or len(wBotD1) == 3 or len(wBotD2) == 3):
        print("ta perdu")
        winnerVar["text"] = "BOT!"
        pygame.mixer.init()
        pygame.mixer.music.load('./sound/voice/1round/defaite1-0.ogg')
        pygame.mixer.music.play()
        for a in morpion1:
            a['state'] = 'disabled'
            a.config(bg='red')
        for a in morpion2:
            a['state'] = 'disabled'
            a.config(bg='red')
        for a in morpion3:
            a['state'] = 'disabled'
            a.config(bg='red')
        for a in morpion4:
            a['state'] = 'disabled'
            a.config(bg='red')
        for a in morpion5:
            a['state'] = 'disabled'
            a.config(bg='red')
        for a in morpion6:
            a['state'] = 'disabled'
            a.config(bg='red')
        for a in morpion7:
            a['state'] = 'disabled'
            a.config(bg='red')
        for a in morpion8:
            a['state'] = 'disabled'
            a.config(bg='red')
        for a in morpion9:
            a['state'] = 'disabled'
            a.config(bg='red')
        click = False
        return True

    else:
        return False
# =====================

# ========BOT PLAY
def botPlay(morp):
    global click
    global morpion1
    global morpion2
    global morpion3
    global morpion4
    global morpion5
    global morpion6
    global morpion7
    global morpion8
    global morpion9

    global play1
    global play2
    global play3
    global play4
    global play5
    global play6
    global play7
    global play8
    global play9



    if not(winnerIs()):


        t = random.choice(morp)

        if t['text'] == ' ' and (t not in morpionFinish) and (t not in morpionFinish2) \
                and (t not in morpionFinish3) and (t not in morpionFinish4) and (t not in morpionFinish5) \
                and (t not in morpionFinish6) and (t not in morpionFinish7) and (t not in morpionFinish8) \
                and (t not in morpionFinish9):

            t['text'] = 'O'
            t.config(bg='cyan')
            winnerIs()
            countdown(t)
            WinMorpion1()
            WinMorpion2()
            WinMorpion3()
            WinMorpion4()
            WinMorpion5()
            WinMorpion6()
            WinMorpion7()
            WinMorpion8()
            WinMorpion9()

            if t in play1 and not(morpionFinish):
                print("t1")
                for b in morpion1:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play2 and not(morpionFinish2):
                print("t2")
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play3 and not(morpionFinish3):
                print("t3")
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play4 and not(morpionFinish4):
                print("t4")
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play5 and not(morpionFinish5):
                print("t5")
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play6 and not(morpionFinish6):
                print("t6")
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play7 and not(morpionFinish7):
                print("t7")
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play8 and not(morpionFinish8):
                print("t8")
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play9 and not(morpionFinish9):
                print("t9")
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                click = True
            # if one of list is not empty we enable everything except the morpionne corresponding to the list and morpion already won
            elif t in play1 and morpionFinish:
                print("tt1")
                if not(check1):
                   for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play2 and morpionFinish2:
                print("tt2")
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play3 and morpionFinish3:
                print("tt3")
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play4 and morpionFinish4:
                print("tt4")
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play5 and morpionFinish5:
                print("tt5")
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play6 and morpionFinish6:
                print("tt6")
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play7 and morpionFinish7:
                print("tt7")
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play8 and morpionFinish8:
                print("tt8")
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                if not (check8):
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                click = True
            elif t in play9 and morpionFinish9:
                print("tt9")
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
        else:
            try:
                botPlay(morp)

            except:
                botPlayExcept()


def botPlayExcept():
    global click
    global morpion1
    global morpion2
    global morpion3
    global morpion4
    global morpion5
    global morpion6
    global morpion7
    global morpion8
    global morpion9

    global play1
    global play2
    global play3
    global play4
    global play5
    global play6
    global play7
    global play8
    global play9

    t1 = random.choice(morpion1)
    t2 = random.choice(morpion2)
    t3 = random.choice(morpion3)
    t4 = random.choice(morpion4)
    t5 = random.choice(morpion5)
    t6 = random.choice(morpion6)
    t7 = random.choice(morpion7)
    t8 = random.choice(morpion8)
    t9 = random.choice(morpion9)

    listRand = []
    listRand.append(t1)
    listRand.append(t2)
    listRand.append(t3)
    listRand.append(t4)
    listRand.append(t5)
    listRand.append(t6)
    listRand.append(t7)
    listRand.append(t8)
    listRand.append(t9)


    if not(winnerIs()):

        t = random.choice(listRand)

        if t['text'] == ' ' and (t not in morpionFinish) and (t not in morpionFinish2) \
                and (t not in morpionFinish3) and (t not in morpionFinish4) and (t not in morpionFinish5) \
                and (t not in morpionFinish6) and (t not in morpionFinish7) and (t not in morpionFinish8) \
                and (t not in morpionFinish9):

            t['text'] = 'O'
            t.config(bg='cyan')
            winnerIs()
            WinMorpion1()
            WinMorpion2()
            WinMorpion3()
            WinMorpion4()
            WinMorpion5()
            WinMorpion6()
            WinMorpion7()
            WinMorpion8()
            WinMorpion9()


            if t in play1 and (not morpionFinish):
                for b in morpion1:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play2 and (not morpionFinish2):
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play3 and (not morpionFinish3):
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play4 and (not morpionFinish4):
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play5 and (not morpionFinish5):
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play6 and (not morpionFinish6):
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play7 and (not morpionFinish7):
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play8 and (not morpionFinish8):
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                for b in morpion9:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                click = True
            elif t in play9 and (not morpionFinish9):
                for b in morpion1:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion2:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion3:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion4:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion5:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion6:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion7:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion8:
                    b['state'] = 'disabled'
                    b.config(bg='grey')
                for b in morpion9:
                    b['state'] = 'normal'
                    b.config(bg='pink')
                click = True
            # if one of list is not empty we enable everything except the morpionne corresponding to the list
            elif t in play1 and morpionFinish:
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play2 and morpionFinish2:
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play3 and morpionFinish3:
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play4 and morpionFinish4:
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play5 and morpionFinish5:
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play6 and morpionFinish6:
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play7 and morpionFinish7:
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play8 and morpionFinish8:
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
            elif t in play9 and morpionFinish9:
                if not (check1):
                    for b in morpion1:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion1:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check2):
                    for b in morpion2:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion2:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check3):
                    for b in morpion3:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion3:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check4):
                    for b in morpion4:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion4:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check5):
                    for b in morpion5:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion5:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check6):
                    for b in morpion6:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion6:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check7):
                    for b in morpion7:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion7:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check8):
                    for b in morpion8:
                        b['state'] = 'normal'
                        b.config(bg='pink')
                else:
                    for b in morpion8:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                if not (check9):
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')
                else:
                    for b in morpion9:
                        b['state'] = 'disabled'
                        b.config(bg='grey')

                click = True
        else:
            botPlayExcept()


# ========USER PLAY
def startMagicPionne(b):
    global click
    global morpion1
    global morpion2
    global morpion3
    global morpion4
    global morpion5
    global morpion6
    global morpion7
    global morpion8
    global morpion9

    global play1
    global play2
    global play3
    global play4
    global play5
    global play6
    global play7
    global play8
    global play9

    # whereToPlay
    play1 = [b1, b12, b13, b14, b15, b16, b17, b18, b19]
    play2 = [b2, b22, b23, b24, b25, b26, b27, b28, b29]
    play3 = [b3, b32, b33, b34, b35, b36, b37, b38, b39]
    play4 = [b4, b42, b43, b44, b45, b46, b47, b48, b49]
    play5 = [b5, b52, b53, b54, b55, b56, b57, b58, b59]
    play6 = [b6, b62, b63, b64, b65, b66, b67, b68, b69]
    play7 = [b7, b72, b73, b74, b75, b76, b77, b78, b79]
    play8 = [b8, b82, b83, b84, b85, b86, b87, b88, b89]
    play9 = [b9, b92, b93, b94, b95, b96, b97, b98, b99]

    # morpionButtons
    morpion1 = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    morpion2 = [b12, b22, b32, b42, b52, b62, b72, b82, b92]
    morpion3 = [b13, b23, b33, b43, b53, b63, b73, b83, b93]
    morpion4 = [b14, b24, b34, b44, b54, b64, b74, b84, b94]
    morpion5 = [b15, b25, b35, b45, b55, b65, b75, b85, b95]
    morpion6 = [b16, b26, b36, b46, b56, b66, b76, b86, b96]
    morpion7 = [b17, b27, b37, b47, b57, b67, b77, b87, b97]
    morpion8 = [b18, b28, b38, b48, b58, b68, b78, b88, b98]
    morpion9 = [b19, b29, b39, b49, b59, b69, b79, b89, b99]

    if b in play1 and (not morpionFinish):
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not(winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlay(morpion1)
    elif b in play2 and (not morpionFinish2):
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not(winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlay(morpion2)
    elif b in play3 and (not morpionFinish3):
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not(winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlay(morpion3)
    elif b in play4 and (not morpionFinish4):
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not(winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlay(morpion4)
    elif b in play5 and (not morpionFinish5):
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not(winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlay(morpion5)
    elif b in play6 and (not morpionFinish6):
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not(winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlay(morpion6)
    elif b in play7 and (not morpionFinish7):
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not(winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlay(morpion7)
    elif b in play8 and (not morpionFinish8):
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not(winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlay(morpion8)
    elif b in play9 and (not morpionFinish9):
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not (winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlay(morpion9)
    # if morpion is closeD:
    elif b in play1 and morpionFinish:
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not(winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlayExcept()
    elif b in play2 and morpionFinish2:
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not(winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlayExcept()
    elif b in play3 and morpionFinish3:
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not (winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlayExcept()
    elif b in play4 and morpionFinish4:
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not (winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlayExcept()
    elif b in play5 and morpionFinish5:
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not (winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlayExcept()
    elif b in play6 and morpionFinish6:
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not(winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlayExcept()
    elif b in play7 and morpionFinish7:
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not (winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlayExcept()
    elif b in play8 and morpionFinish8:
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not(winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlayExcept()
    elif b in play9 and morpionFinish9:
        if b["text"] == " " and click == True:
            b["text"] = 'X'
            click = False
            if not (winnerIs()):
                WinMorpion1()
                WinMorpion2()
                WinMorpion3()
                WinMorpion4()
                WinMorpion5()
                WinMorpion6()
                WinMorpion7()
                WinMorpion8()
                WinMorpion9()
                botPlayExcept()
