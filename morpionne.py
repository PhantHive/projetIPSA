#Librairies
import pymongo
from pymongo import MongoClient
import tkinter as tk
import time
import PIL.Image, PIL.ImageTk, PIL.ImageDraw
import random
import sys
import json
import pygame.mixer, pygame.mixer_music
from tkinter import messagebox

#db===================
cluster = MongoClient("mongodb+srv://phanthive:morpionne@cluster0-pll8o.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["morpionne"]
collection = db["connection"]
collectionScore = db["leaderboard"]
#online classification
collectionScore.find({}, {"scoreLB": 1}).limit(100)

#=====================

#Tkinter app

app = tk.Tk()
app.title("MORPION")

def updateLB():
    # ===
    global numberThree, numberTwo, numberOne
    file = './jsonScore/score.json'
    outputLB = json.load(open(file, 'r'))

    # collector
    try:
        virtuoseVic = outputLB[nm]["virtuoso"]["Victoire"]
        virtuosoScore.set(virtuoseVic)
    except KeyError:
        virtuosoScore.set(0)

    try:
        cauchemarVic = outputLB[nm]["cauchemar"]["Victoire"]
        cauchemarScore.set(cauchemarVic)
    except KeyError:
        cauchemarScore.set(0)

    try:
        extremVic = outputLB[nm]["extreme"]["Victoire"]
        extremeScore.set(extremVic)
    except KeyError:
        extremeScore.set(0)

    try:
        difficileVic = outputLB[nm]["difficile"]["Victoire"]
        difficileScore.set(difficileVic)
    except KeyError:
        difficileScore.set(0)

    try:
        moyenVic = outputLB[nm]["moyen"]["Victoire"]
        moyenScore.set(moyenVic)
    except KeyError:
        moyenScore.set(0)

    try:
        facileVic = outputLB[nm]["facile"]["Victoire"]
        facileScore.set(facileVic)
    except KeyError:
        facileScore.set(0)

    lb = []
    collectDATA = collectionScore.find({})
    for dic in collectDATA:
        a = str(dic["scoreLB"])
        b = dic["pseudo"]
        ab = a + " by " + b
        lb.append(ab)


    lb.sort(key = lambda x: int(x.split(" by ")[0]))
    lb.reverse()

    try:
        numberOne = lb[0]
        numberTwo = lb[1]
        numberThree = lb[2]
    except IndexError:
        try:
            numberOne = lb[0]
            numberTwo = lb[1]
        except IndexError:
            try:
                numberOne = lb[0]
            except IndexError:
                return

    try:
        onlineTOP1.set(numberOne)
    except NameError:
        onlineTOP1.set("personne classé!")

    try:
        onlineTOP2.set(numberTwo)
    except NameError:
        onlineTOP2.set("personne en position2")

    try:
        onlineTOP3.set(numberThree)
    except NameError:
        onlineTOP3.set("personne en position3")



    print(lb[0])


#trop de probleme a regler sur fonction voiceScore!!!!!
def voiceScore():
    global frames
    global pseudo

    pygame.mixer.init()
    L = ['./sound/voice/clash/clash.ogg', './sound/voice/clash/clash2.ogg', './sound/voice/clash/clash3.ogg', './sound/voice/clash/clash4.ogg', './sound/voice/clash/clash5.ogg']
    filename = random.choice(L)

    if gamesNb == 5:
        # egalite
        if (winBot == winUser) and (winUser == 0):
            pygame.mixer.music.load('./sound/voice/5round/egalite 0-0.ogg')  # 0-0
            pygame.mixer.music.play()
        elif (winBot == winUser) and (winUser == 1):
            pygame.mixer.music.load('./sound/voice/2round/egalite 1-1.ogg')  # 1-1
            pygame.mixer.music.play()
        elif (winBot == winUser) and (winUser == 2):
            pygame.mixer.music.load('./sound/voice/4round/egalite2-2.ogg')  # 2-2
            pygame.mixer.music.play()
            # defaite
        elif winBot == 5:
            pygame.mixer.music.load('./sound/voice/5round/defaite5-0.ogg')
            pygame.mixer.music.play()
        elif (winBot == 4) and (winUser == 1):
            pygame.mixer.music.load('./sound/voice/5round/defaite4-1.ogg')
            pygame.mixer.music.play()
        elif (winBot == 3 and winUser == 2):
            pygame.mixer.music.load('./sound/voice/5round/defaite3-2.ogg')
            pygame.mixer.music.play()
            # victoire
        elif winUser == 5:
            pygame.mixer.music.load('./sound/voice/5round/victoire5-0.ogg')
            pygame.mixer.music.play()
        elif (winUser == 4) and (winBot == 1):
            pygame.mixer.music.load('./sound/voice/5round/victoire4-1.ogg')
            pygame.mixer.music.play()
        elif (winUser == 3) and (winBot == 2):
            pygame.mixer.music.load('./sound/voice/5round/victoire3-2.ogg')
            pygame.mixer.music.play()
            # precedent
            # victoire
        elif winUser == 4:
            pygame.mixer.music.load('./sound/voice/4round/victoire4-0.ogg')
            pygame.mixer.music.play()
        elif (winUser == 3) and (winBot == 1):
            pygame.mixer.music.load('./sound/voice/4round/victoire3-1.ogg')
            pygame.mixer.music.play()
            # defaite
        elif winBot == 4:
            pygame.mixer.music.load('./sound/voice/4round/defaite4-0.ogg')
            pygame.mixer.music.play()
        elif (winBot == 3) and (winUser == 1):
            pygame.mixer.music.load('./sound/voice/4round/defaite3-1.ogg')
            pygame.mixer.music.play()
            # victoire
        elif winUser == 3:
            pygame.mixer.music.load('./sound/voice/3round/victoire3-0.ogg')  # 3-0
            pygame.mixer.music.play()
        elif winUser == 2 and winBot == 1:
            pygame.mixer.music.load('./sound/voice/3round/victoire2-1.ogg')  # 2-1
            pygame.mixer.music.play()
            # defaite
        elif winBot == 3:
            pygame.mixer.music.load('./sound/voice/3round/defaite3-0.ogg')  # 0-3
            pygame.mixer.music.play()
        elif winBot == 2 and winUser == 1:
            pygame.mixer.music.load('./sound/voice/3round/defaite2-1.ogg')  # 1-2
            pygame.mixer.music.play()
        elif winUser == 2:
            pygame.mixer.music.load('./sound/voice/2round/victoire2-0.ogg')  # 2-0
            pygame.mixer.music.play()
            # defaite
        elif winBot == 2:
            pygame.mixer.music.load('./sound/voice/2round/defaite2-0.ogg')  # 0-2
            pygame.mixer.music.play()
            # victoire
        elif winUser == 1:
            pygame.mixer.music.load('./sound/voice/1round/victoire1-0.ogg')  # 1-0
            pygame.mixer.music.play()
            # defaite
        elif winBot == 1:
            pygame.mixer.music.load('sound/voice/clash/clash.ogg')
            pygame.mixer.music.play()
            pygame.mixer.music.load('./sound/voice/1round/defaite1-0.ogg')  # 0-1
            pygame.mixer.music.play()

    elif gamesNb == 4:
        # egalite
        if (winBot == winUser) and (winUser == 0):
            pygame.mixer.music.load('./sound/voice/4round/egalite 0-0.ogg')
            pygame.mixer.music.play()
        elif (winBot == winUser) and (winUser == 1):
            pygame.mixer.music.load('./sound/voice/2round/egalite 1-1.ogg')  # 1-1
            pygame.mixer.music.play()
        elif (winBot == winUser) and (winUser == 2):
            pygame.mixer.music.load('./sound/voice/4round/egalite2-2.ogg')
            pygame.mixer.music.play()
            # victoire
        elif winUser == 4:
            pygame.mixer.music.load('./sound/voice/4round/victoire4-0.ogg')
            pygame.mixer.music.play()
        elif (winUser == 3) and (winBot == 1):
            pygame.mixer.music.load('./sound/voice/4round/victoire3-1.ogg')
            pygame.mixer.music.play()
            # defaite
        elif winBot == 4:
            pygame.mixer.music.load('./sound/voice/4round/defaite4-0.ogg')
            pygame.mixer.music.play()
        elif (winBot == 3) and (winUser == 1):
            pygame.mixer.music.load('./sound/voice/4round/defaite3-1.ogg')
            pygame.mixer.music.play()
            # precedent
            # victoire
        elif winUser == 3:
            pygame.mixer.music.load('./sound/voice/3round/victoire3-0.ogg')  # 3-0
            pygame.mixer.music.play()
        elif winUser == 2 and winBot == 1:
            pygame.mixer.music.load('./sound/voice/3round/victoire2-1.ogg')  # 2-1
            pygame.mixer.music.play()
            # defaite
        elif winBot == 3:
            pygame.mixer.music.load('./sound/voice/3round/defaite3-0.ogg')  # 0-3
            pygame.mixer.music.play()
        elif winBot == 2 and winUser == 1:
            pygame.mixer.music.load('./sound/voice/3round/defaite2-1.ogg')  # 1-2
            pygame.mixer.music.play()
        elif winUser == 2:
            pygame.mixer.music.load('./sound/voice/2round/victoire2-0.ogg')  # 2-0
            pygame.mixer.music.play()
            # defaite
        elif winBot == 2:
            pygame.mixer.music.load('./sound/voice/2round/defaite2-0.ogg')  # 0-2
            pygame.mixer.music.play()
            # victoire
        elif winUser == 1:
            pygame.mixer.music.load('./sound/voice/1round/victoire1-0.ogg')  # 1-0
            pygame.mixer.music.play()
            # defaite
        elif winBot == 1:
            pygame.mixer.music.load('./sound/voice/1round/defaite1-0.ogg')  # 0-1
            pygame.mixer.music.play()

    elif gamesNb == 3:
        # egalite
        if (winBot == winUser) and (winUser == 0):
            pygame.mixer.music.load('./sound/voice/3round/egalite 0-0.ogg')  # 0-0
            pygame.mixer.music.play()
        elif (winBot == winUser) and (winUser == 1):
            pygame.mixer.music.load('./sound/voice/2round/egalite 1-1.ogg')  # 1-1
            pygame.mixer.music.play()
            # victoire
        elif winUser == 3:
            pygame.mixer.music.load('./sound/voice/3round/victoire3-0.ogg')  # 3-0
            pygame.mixer.music.play()
        elif winUser == 2 and winBot == 1:
            pygame.mixer.music.load('./sound/voice/3round/victoire2-1.ogg')  # 2-1
            pygame.mixer.music.play()
            # defaite
        elif winBot == 3:
            pygame.mixer.music.load('./sound/voice/3round/defaite3-0.ogg')  # 0-3
            pygame.mixer.music.play()
        elif winBot == 2 and winUser == 1:
            pygame.mixer.music.load('./sound/voice/3round/defaite2-1.ogg')  # 1-2
            pygame.mixer.music.play()
            # precedent
        elif winUser == 2:
            pygame.mixer.music.load('./sound/voice/2round/victoire2-0.ogg')  # 2-0
            pygame.mixer.music.play()
            # defaite
        elif winBot == 2:
            pygame.mixer.music.load('./sound/voice/2round/defaite2-0.ogg')  # 0-2
            pygame.mixer.music.play()
            # victoire
        elif winUser == 1:
            pygame.mixer.music.load('./sound/voice/1round/victoire1-0.ogg')  # 1-0
            pygame.mixer.music.play()
            # defaite
        elif winBot == 1:
            pygame.mixer.music.load('./sound/voice/1round/defaite1-0.ogg')  # 0-1
            pygame.mixer.music.play()

    elif gamesNb == 2:
        # egalite
        if (winBot == winUser) and (winUser == 0):
            pygame.mixer.music.load('./sound/voice/2round/egalite 0-0.ogg')  # 0-0
            pygame.mixer.music.play()
        elif (winBot == winUser) and (winUser == 1):
            pygame.mixer.music.load('./sound/voice/2round/egalite 1-1.ogg')  # 1-1
            pygame.mixer.music.play()
            # victoire
        elif winUser == 2:
            pygame.mixer.music.load('./sound/voice/2round/victoire2-0.ogg')  # 2-0
            pygame.mixer.music.play()
            # defaite
        elif winBot == 2:
            pygame.mixer.music.load('./sound/voice/2round/defaite2-0.ogg')  # 0-2
            pygame.mixer.music.play()
            # Precedent
        elif winUser == 1:
            pygame.mixer.music.load('./sound/voice/1round/victoire1-0.ogg')  # 1-0
            pygame.mixer.music.play()
            # defaite
        elif winBot == 1:
            pygame.mixer.music.load('./sound/voice/1round/defaite1-0.ogg')  # 0-1
            pygame.mixer.music.play()

    elif gamesNb == 1:
        # egalite
        if (winBot == winUser) and (winUser == 0):
            pygame.mixer.music.load('./sound/voice/1round/egalite 0-0.ogg')
            pygame.mixer.music.play()
            # victoire
        elif winUser == 1:
            pygame.mixer.music.load('./sound/voice/1round/victoire1-0.ogg')
            pygame.mixer.music.play()
            # defaite
        elif winBot == 1:
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()


    dataScore = {}
    dataScore["Victoire"] = winUser
    dataScore["Defaite"] = winBot
    dataScore["Egalite"] = draw

    dataDiffMode = {}
    dataDiffMode[diffMode] = dataScore


    print(dataDiffMode)


    pseudo = collectNameLogin.get()
    print(pseudo)
    type(pseudo)
    print(winUser)
    print(winBot)

    lbArray = {}
    lbArray[diffMode] = winUser

    with open('./jsonScore/score.json', 'r+') as upFile:
        dataUp = json.load(upFile)
        if (pseudo in dataUp):
            if diffMode in dataUp[pseudo]:

                dataUp[pseudo][diffMode]["Victoire"] += winUser
                dataUp[pseudo][diffMode]["Defaite"] += winBot
                dataUp[pseudo][diffMode]["Egalite"] += draw
                print("update")
                try:
                    upFile.seek(0)
                    upFile.write(json.dumps(dataUp, indent=4))
                    upFile.truncate()
                except:
                    print("probleme survenu")

            else:

                dataUp[pseudo][diffMode] = dataScore
                print("update 2")
                try:
                    upFile.seek(0)
                    upFile.write(json.dumps(dataUp, indent=4))
                    upFile.truncate()
                except:
                    print("probleme survenu")

        else:

            dataUp[pseudo] = dataDiffMode
            print(dataUp)
            try:
                upFile.seek(0)
                upFile.write(json.dumps(dataUp, indent=4))
                upFile.truncate()
            except:
                print("probleme survenu 2")  #TROP


    verifyScore = collectionScore.count_documents({pseudo: {"$exists": True}})

    if (verifyScore != 0):
        print("cet utilisateur a deja un score")
        for doc in collectionScore.find({pseudo: {"$exists": True}}):
            oldScore = doc[pseudo]["score"]
            print("ancien score" + str(oldScore))
            newScore = oldScore + winUser
            print("newscore" + str(newScore))
            collectionScore.update_one({pseudo: {"name": pseudo, "score": oldScore}}, {"$set": {pseudo: {"name": pseudo, "score": newScore}, "scoreLB": newScore, "pseudo": pseudo}})
            print("score bien mise a jour")
    else:
        collectionScore.insert_one({pseudo: { "name": pseudo, "score": winUser}, "scoreLB": winUser, "pseudo": pseudo})

    updateLB()

#=====================FONCTION LOGIN-REGISTER
def closeRegistration():
    if messagebox.askokcancel("FERMER", "Si tu fermes la page de Login sans te connecter tu ne pourras pas acceder au jeu. Etes-vous sur d'abandonner?"):
        userInfo.destroy()
        app.destroy()

def connectVerif():
    global nm
    nm = collectNameLogin.get()
    ps = collectPassLogin.get()
    playerShow.get()
    #userData = open('./login/login.json', 'r')
    #jsonData = json.load(userData)

    resultsDB = collection.count_documents({"name": nm, "pass": ps})

    if (resultsDB != 0):
        print("connected")
        playerShow.set(nm)
        app.deiconify()  # release invisible principal window app
        pygame.mixer.init()
        pygame.mixer.music.load('./sound/voice/welcome.ogg')
        pygame.mixer.music.play()
        userInfo.destroy()
    else:
        tk.messagebox.showwarning("Wrong Password", "MAUVAIS MOT DE PASSE! OU Mauvais nom d'utilisateur")
    '''
    for dic in jsonData:
        if nm in dic:
            if (ps == dic.get(nm)):
                print("connected")
                playerShow.set(nm)
                updateLB()
                app.deiconify() #release invisible principal window app
                pygame.mixer.init()
                pygame.mixer.music.load('./sound/voice/welcome.ogg')
                pygame.mixer.music.play()
                userInfo.destroy()
            else:
                tk.messagebox.showwarning("Wrong Password", "MAUVAIS MOT DE PASSE!")
    '''

def confRegister():
    global NAME
    NAME = name.get()
    PASS = psw.get()
    CONFPASS = confpsw.get()

    # User dictionary
    #userDic = {}

    try:
        dbase = collection.find({})
        for doc in dbase:
            if (doc["name"] == NAME):
                print("pas possible")
                tk.messagebox.showinfo("impossible", "Nom d'utilisateur deja pris!")
                return
        print("mince")
        return 1/0
    except ZeroDivisionError:
        collection.insert_one({"name": NAME, "pass": PASS})
        tk.messagebox.showinfo("success", "Compte a bien ete cree!")
        registerWindow.destroy()
        return



        '''
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
        '''


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

    confirm = tk.Button(registerWindow, text="S'enregistrer", font=("Helvtica 10"), command= confRegister)
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
#======================


#Fonctions
#==================WIN VERIF + ATTACK

def checkWin():
    global click
    global winBot
    global winUser
    global draw
    # ===================================================
    # mixerinit
    pygame.mixer.init()
    # USER
    # Vertical Verif
    if b1["text"] == 'X' and b4["text"] == 'X' and b7["text"] == 'X':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        win.config(text="GG, Tu m'impressionnes!")
        click = False
        winUser += 1
        countStart.destroy()
        # ====
        upRd = rd - 1

        if upRd == 0:
            voiceScore()
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
            voiceScore()
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
            voiceScore()
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
            voiceScore()
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
            voiceScore()
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
            voiceScore()
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
            voiceScore()
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
            voiceScore()
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

    # ====================================================
    # BOT
    # Vertical Verif
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

            voiceScore()
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
            voiceScore()
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
            voiceScore()
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
            voiceScore()
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
            voiceScore()
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
            voiceScore()
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
            voiceScore()
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
            voiceScore()
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
        win.config(text="egalite! Match fini en egalite")
        click = False
        draw += 1
        countStart.destroy()
        # ====
        upRd = rd - 1
        if upRd == 0:
            voiceScore()
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

def attack():
    global click

    #line 1
    if (b1["text"] == 'O') and (b2["text"] == 'O') and (b3["text"] == ' '):
        b3.config(text='O')
        click = True
        return click
    elif (b1["text"] == 'O') and (b3["text"] == 'O') and (b2["text"] == ' '):
        b2.config(text='O')
        click = True
        return click
    elif (b2["text"] == 'O') and (b3["text"] == 'O') and (b1["text"] == ' '):
        b1.config(text='O')
        click = True
        return click
    #line 2
    elif (b5["text"] == 'O') and (b6["text"] == 'O') and (b4["text"] == ' '):
        b4.config(text='O')
        click = True
        return click
    elif (b4["text"] == 'O') and (b6["text"] == 'O') and (b5["text"] == ' '):
        b5.config(text='O')
        click = True
        return click
    elif (b4["text"] == 'O') and (b5["text"] == 'O') and (b6["text"] == ' '):
        b6.config(text='O')
        click = True
        return click
    #line 3
    elif (b8["text"] == 'O') and (b9["text"] == 'O') and (b7["text"] == ' '):
        b7.config(text='O')
        click = True
        return click
    elif (b7["text"] == 'O') and (b9["text"] == 'O') and (b8["text"] == ' '):
        b8.config(text='O')
        click = True
        return click
    elif (b7["text"] == 'O') and (b8["text"] == 'O') and (b9["text"] == ' '):
        b9.config(text='O')
        click = True
        return click
    #column 1
    elif (b4["text"] == 'O') and (b7["text"] == 'O') and (b1["text"] == ' '):
        b1.config(text='O')
        click = True
        return click
    elif (b1["text"] == 'O') and (b7["text"] == 'O') and (b4["text"] == ' '):
        b4.config(text='O')
        click = True
        return click
    elif (b1["text"] == 'O') and (b4["text"] == 'O') and (b7["text"] == ' '):
        b7.config(text='O')
        click = True
        return click
    # column 2
    elif (b5["text"] == 'O') and (b8["text"] == 'O') and (b2["text"] == ' '):
        b2.config(text='O')
        click = True
        return click
    elif (b2["text"] == 'O') and (b8["text"] == 'O') and (b5["text"] == ' '):
        b5.config(text='O')
        click = True
        return click
    elif (b2["text"] == 'O') and (b5["text"] == 'O') and (b8["text"] == ' '):
        b8.config(text='O')
        click = True
        return click
    # column 3
    elif (b6["text"] == 'O') and (b9["text"] == 'O') and (b3["text"] == ' '):
        b3.config(text='O')
        click = True
        return click
    elif (b3["text"] == 'O') and (b9["text"] == 'O') and (b6["text"] == ' '):
        b6.config(text='O')
        click = True
        return click
    elif (b3["text"] == 'O') and (b6["text"] == 'O') and (b9["text"] == ' '):
        b9.config(text='O')
        click = True
        return click
    #diagonal 1
    elif (b5["text"] == 'O') and (b9["text"] == 'O') and (b1["text"] == ' '):
        b1.config(text='O')
        click = True
        return click
    elif (b1["text"] == 'O') and (b9["text"] == 'O') and (b5["text"] == ' '):
        b5.config(text='O')
        click = True
        return click
    elif (b1["text"] == 'O') and (b5["text"] == 'O') and (b9["text"] == ' '):
        b9.config(text='O')
        click = True
        return click
    # diagonal 2
    elif (b5["text"] == 'O') and (b7["text"] == 'O') and (b3["text"] == ' '):
        b3.config(text='O')
        click = True
        return click
    elif (b3["text"] == 'O') and (b7["text"] == 'O') and (b5["text"] == ' '):
        b5.config(text='O')
        click = True
        return click
    elif (b3["text"] == 'O') and (b5["text"] == 'O') and (b7["text"] == ' '):
        b7.config(text='O')
        click = True
        return click

    else:
        return 1/0
#==================

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
    global gif
    global win
    global click
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

    rd = i  # number of round previously chosen

    game = tk.Toplevel()
    # customs window
    game.geometry("650x650")
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

    # labels players

    label_player1 = tk.Label(game, text="Joueur 1: X")
    label_player1.place(x=0, y=200)

    label_player1 = tk.Label(game, text="Joueur 2: O")
    label_player1.place(x=500, y=200)

    gif = tk.Canvas(game)
    gif.place(x=750, y=600)

    pygame.mixer.init()

    if playerStart == 1:
        #voice start====
        pygame.mixer.music.load('./sound/voice/matchstart.ogg')
        pygame.mixer.music.play()
        #===
        if diffMode == "virtuoso":

            pygame.mixer.music.load("./sound/voice/virtuoseMode.ogg")
            pygame.mixer.music.play()
            playCaseFirst = random.randrange(1,5)  # choose randomly where to start playing between corner case and middle case
            print(playCaseFirst)
            # button
            # ligne 1
            b1 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameVirtuoso(b1))
            b1.place(x=155, y=12)

            b2 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameVirtuoso(b2))
            b2.place(x=265, y=12)

            b3 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameVirtuoso(b3))
            b3.place(x=375, y=12)

            # ligne 2
            b4 = tk.Button(game, text=" ", width=13, height=6, bg="black", activebackground="black", command=lambda: startGameVirtuoso(b4))
            b4.place(x=155, y=107)

            b5 = tk.Button(game, text=" ", width=13, height=6, bg="black", activebackground="black", command=lambda: startGameVirtuoso(b5))
            b5.place(x=265, y=107)

            b6 = tk.Button(game, text=" ", width=13, height=6, bg="black", activebackground="black", command=lambda: startGameVirtuoso(b6))
            b6.place(x=375, y=107)

            # ligne 3
            b7 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameVirtuoso(b7))
            b7.place(x=155, y=215)

            b8 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameVirtuoso(b8))
            b8.place(x=265, y=215)

            b9 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameVirtuoso(b9))
            b9.place(x=375, y=215)

        elif diffMode == "cauchemar":
            pygame.mixer.music.load("./sound/voice/cauchemarMode.ogg")
            pygame.mixer.music.play()

            # button
            # ligne 1
            b1 = tk.Button(game, text= " ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameCauchemar(b1))
            b1.place(x=155, y=12)

            b2 = tk.Button(game, text= " ", bg="black", width=13, height=5, activebackground="black", command=lambda: startGameCauchemar(b2))
            b2.place(x=265, y=12)

            b3 = tk.Button(game, text= " ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameCauchemar(b3))
            b3.place(x=375, y=12)

            # ligne 2
            b4 = tk.Button(game, text= " ", bg="black", width=13, height=6, activebackground="black", command=lambda: startGameCauchemar(b4))
            b4.place(x=155, y=107)

            b5 = tk.Button(game, text= " ", width=13, height=6, bg="black", activebackground="black",command=lambda: startGameCauchemar(b5))
            b5.place(x=265, y=107)

            b6 = tk.Button(game, text= " ", width=13, height=6, bg="black", activebackground="black", command=lambda: startGameCauchemar(b6))
            b6.place(x=375, y=107)

            # ligne 3
            b7 = tk.Button(game, text= " ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameCauchemar(b7))
            b7.place(x=155, y=215)

            b8 = tk.Button(game,text= " ", bg="black", width=13, height=5, activebackground="black", command=lambda: startGameCauchemar(b8))
            b8.place(x=265, y=215)

            b9 = tk.Button(game,text= " ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameCauchemar(b9))
            b9.place(x=375, y=215)

        elif diffMode == "extreme":

            # voice start====
            pygame.mixer.music.load('./sound/voice/extremeMode.ogg')
            pygame.mixer.music.play()
            # ===
            playCaseFirst = random.randrange(1,
                                             5)  # choose randomly where to start playing between corner case and middle case
            print(playCaseFirst)
            # button
            # ligne 1
            b1 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameExtreme(b1))
            b1.place(x=155, y=12)

            b2 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameExtreme(b2))
            b2.place(x=265, y=12)

            b3 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameExtreme(b3))
            b3.place(x=375, y=12)

            # ligne 2
            b4 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameExtreme(b4))
            b4.place(x=155, y=107)

            b5 = tk.Button(game, text=" ", width=13, height=6, bg="#7bb1ef", command=lambda: startGameExtreme(b5))
            b5.place(x=265, y=107)

            b6 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameExtreme(b6))
            b6.place(x=375, y=107)

            # ligne 3
            b7 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameExtreme(b7))
            b7.place(x=155, y=215)

            b8 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameExtreme(b8))
            b8.place(x=265, y=215)

            b9 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameExtreme(b9))
            b9.place(x=375, y=215)

        elif diffMode == "difficile":
            playCaseFirst = random.randrange(1,
                                             5)  # choose randomly where to start playing between corner case and middle case
            print(playCaseFirst)
            # button
            # ligne 1
            b1 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameDifficile(b1))
            b1.place(x=155, y=12)

            b2 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameDifficile(b2))
            b2.place(x=265, y=12)

            b3 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameDifficile(b3))
            b3.place(x=375, y=12)

            # ligne 2
            b4 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameDifficile(b4))
            b4.place(x=155, y=107)

            b5 = tk.Button(game, text=" ", width=13, height=6, bg="#7bb1ef", command=lambda: startGameDifficile(b5))
            b5.place(x=265, y=107)

            b6 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameDifficile(b6))
            b6.place(x=375, y=107)

            # ligne 3
            b7 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameDifficile(b7))
            b7.place(x=155, y=215)

            b8 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameDifficile(b8))
            b8.place(x=265, y=215)

            b9 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameDifficile(b9))
            b9.place(x=375, y=215)

        elif diffMode == "moyen":
            playCaseFirst = random.randrange(1,
                                             5)  # choose randomly where to start playing between corner case and middle case
            print(playCaseFirst)
            # button
            # ligne 1
            b1 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameMoyen(b1))
            b1.place(x=155, y=12)

            b2 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameMoyen(b2))
            b2.place(x=265, y=12)

            b3 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameMoyen(b3))
            b3.place(x=375, y=12)

            # ligne 2
            b4 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameMoyen(b4))
            b4.place(x=155, y=107)

            b5 = tk.Button(game, text=" ", width=13, height=6, bg="#7bb1ef", command=lambda: startGameMoyen(b5))
            b5.place(x=265, y=107)

            b6 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameMoyen(b6))
            b6.place(x=375, y=107)

            # ligne 3
            b7 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameMoyen(b7))
            b7.place(x=155, y=215)

            b8 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameMoyen(b8))
            b8.place(x=265, y=215)

            b9 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameMoyen(b9))
            b9.place(x=375, y=215)

        elif diffMode == "facile":
            playCaseFirst = random.randrange(1,
                                             5)  # choose randomly where to start playing between corner case and middle case
            print(playCaseFirst)
            # button
            # ligne 1
            b1 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameFacile(b1))
            b1.place(x=155, y=12)

            b2 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameFacile(b2))
            b2.place(x=265, y=12)

            b3 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameFacile(b3))
            b3.place(x=375, y=12)

            # ligne 2
            b4 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameFacile(b4))
            b4.place(x=155, y=107)

            b5 = tk.Button(game, text=" ", width=13, height=6, bg="#7bb1ef", command=lambda: startGameFacile(b5))
            b5.place(x=265, y=107)

            b6 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameFacile(b6))
            b6.place(x=375, y=107)

            # ligne 3
            b7 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameFacile(b7))
            b7.place(x=155, y=215)

            b8 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameFacile(b8))
            b8.place(x=265, y=215)

            b9 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameFacile(b9))
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
        # voice start====
        pygame.mixer.music.load('./sound/voice/matchstart.ogg')
        pygame.mixer.music.play()
        # ===

        if diffMode == "virtuoso":
            pygame.mixer.music.load("./sound/voice/virtuoseMode.ogg")
            pygame.mixer.music.play()
            playCaseFirst = random.randrange(1,5)  # choose randomly where to start playing between corner case and middle case
            print(playCaseFirst)
            # button
            # ligne 1
            b1 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black",
                           command=lambda: startGameVirtuoso(b1))
            b1.place(x=155, y=12)

            b2 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black",
                           command=lambda: startGameVirtuoso(b2))
            b2.place(x=265, y=12)

            b3 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black",
                           command=lambda: startGameVirtuoso(b3))
            b3.place(x=375, y=12)

            # ligne 2
            b4 = tk.Button(game, text=" ", width=13, height=6, bg="black", activebackground="black",
                           command=lambda: startGameVirtuoso(b4))
            b4.place(x=155, y=107)

            b5 = tk.Button(game, text=" ", width=13, height=6, bg="black", activebackground="black",
                           command=lambda: startGameVirtuoso(b5))
            b5.place(x=265, y=107)

            b6 = tk.Button(game, text=" ", width=13, height=6, bg="black", activebackground="black",
                           command=lambda: startGameVirtuoso(b6))
            b6.place(x=375, y=107)

            # ligne 3
            b7 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black",
                           command=lambda: startGameVirtuoso(b7))
            b7.place(x=155, y=215)

            b8 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black",
                           command=lambda: startGameVirtuoso(b8))
            b8.place(x=265, y=215)

            b9 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black",
                           command=lambda: startGameVirtuoso(b9))
            b9.place(x=375, y=215)

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

            countdownRotation()

        elif diffMode == "cauchemar":
            pygame.mixer.music.load("./sound/voice/cauchemarMode.ogg")
            pygame.mixer.music.play()
            playCaseFirst = random.randrange(1, 5) #choose randomly where to start playing between corner case and middle case
            print(playCaseFirst)
            # button
            # ligne 1
            b1 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameCauchemar(b1))
            b1.place(x=155, y=12)

            b2 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameCauchemar(b2))
            b2.place(x=265, y=12)

            b3 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameCauchemar(b3))
            b3.place(x=375, y=12)

            # ligne 2
            b4 = tk.Button(game, text=" ", width=13, height=6, bg="black", activebackground="black", command=lambda: startGameCauchemar(b4))
            b4.place(x=155, y=107)

            b5 = tk.Button(game, text=" ", width=13, height=6, bg="black", activebackground="black", command=lambda: startGameCauchemar(b5))
            b5.place(x=265, y=107)


            b6 = tk.Button(game, text=" ", width=13, height=6, bg="black", activebackground="black", command=lambda: startGameCauchemar(b6))
            b6.place(x=375, y=107)

            # ligne 3
            b7 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameCauchemar(b7))
            b7.place(x=155, y=215)

            b8 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameCauchemar(b8))
            b8.place(x=265, y=215)

            b9 = tk.Button(game, text=" ", width=13, height=5, bg="black", activebackground="black", command=lambda: startGameCauchemar(b9))
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

        elif diffMode == "extreme":
            # voice start====
            pygame.mixer.music.load('./sound/voice/extremeMode.ogg')
            pygame.mixer.music.play()
            # ===
            playCaseFirst = random.randrange(1,5)  # choose randomly where to start playing between corner case and middle case
            print(playCaseFirst)
            # button
            # ligne 1
            b1 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameExtreme(b1))
            b1.place(x=155, y=12)

            b2 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameExtreme(b2))
            b2.place(x=265, y=12)

            b3 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameExtreme(b3))
            b3.place(x=375, y=12)

            # ligne 2
            b4 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameExtreme(b4))
            b4.place(x=155, y=107)

            b5 = tk.Button(game, text=" ", width=13, height=6, bg="#7bb1ef", command=lambda: startGameExtreme(b5))
            b5.place(x=265, y=107)

            b6 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameExtreme(b6))
            b6.place(x=375, y=107)

            # ligne 3
            b7 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameExtreme(b7))
            b7.place(x=155, y=215)

            b8 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameExtreme(b8))
            b8.place(x=265, y=215)

            b9 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameExtreme(b9))
            b9.place(x=375, y=215)

            # random choose where to start

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

        elif diffMode == "difficile":

            playCaseFirst = random.randrange(1,
                                             5)  # choose randomly where to start playing between corner case and middle case
            print(playCaseFirst)
            # button
            # ligne 1
            b1 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameDifficile(b1))
            b1.place(x=155, y=12)

            b2 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameDifficile(b2))
            b2.place(x=265, y=12)

            b3 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameDifficile(b3))
            b3.place(x=375, y=12)

            # ligne 2
            b4 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameDifficile(b4))
            b4.place(x=155, y=107)

            b5 = tk.Button(game, text=" ", width=13, height=6, bg="#7bb1ef", command=lambda: startGameDifficile(b5))
            b5.place(x=265, y=107)

            b6 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameDifficile(b6))
            b6.place(x=375, y=107)

            # ligne 3
            b7 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameDifficile(b7))
            b7.place(x=155, y=215)

            b8 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameDifficile(b8))
            b8.place(x=265, y=215)

            b9 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameDifficile(b9))
            b9.place(x=375, y=215)

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

        elif diffMode == "moyen":
            playCaseFirst = random.randrange(1,
                                             5)  # choose randomly where to start playing between corner case and middle case
            print(playCaseFirst)
            # button
            # ligne 1
            b1 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameMoyen(b1))
            b1.place(x=155, y=12)

            b2 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameMoyen(b2))
            b2.place(x=265, y=12)

            b3 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameMoyen(b3))
            b3.place(x=375, y=12)

            # ligne 2
            b4 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameMoyen(b4))
            b4.place(x=155, y=107)

            b5 = tk.Button(game, text=" ", width=13, height=6, bg="#7bb1ef", command=lambda: startGameMoyen(b5))
            b5.place(x=265, y=107)

            b6 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameMoyen(b6))
            b6.place(x=375, y=107)

            # ligne 3
            b7 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameMoyen(b7))
            b7.place(x=155, y=215)

            b8 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameMoyen(b8))
            b8.place(x=265, y=215)

            b9 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameMoyen(b9))
            b9.place(x=375, y=215)

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

        elif diffMode == "facile":
            playCaseFirst = random.randrange(1,
                                             5)  # choose randomly where to start playing between corner case and middle case
            print(playCaseFirst)
            # button
            # ligne 1
            b1 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameFacile(b1))
            b1.place(x=155, y=12)

            b2 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameFacile(b2))
            b2.place(x=265, y=12)

            b3 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameFacile(b3))
            b3.place(x=375, y=12)

            # ligne 2
            b4 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameFacile(b4))
            b4.place(x=155, y=107)

            b5 = tk.Button(game, text=" ", width=13, height=6, bg="#7bb1ef", command=lambda: startGameFacile(b5))
            b5.place(x=265, y=107)

            b6 = tk.Button(game, text=" ", width=13, height=6, command=lambda: startGameFacile(b6))
            b6.place(x=375, y=107)

            # ligne 3
            b7 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameFacile(b7))
            b7.place(x=155, y=215)

            b8 = tk.Button(game, text=" ", width=13, height=5, command=lambda: startGameFacile(b8))
            b8.place(x=265, y=215)

            b9 = tk.Button(game, text=" ", width=13, height=5, bg="#7bb1ef", command=lambda: startGameFacile(b9))
            b9.place(x=375, y=215)

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
    for k in range(3, -1, -1):
        click = False
        countStartLabel["text"] = k
        countStart["text"] = "A toi dans: "
        app.update()
        time.sleep(1)
    click = True
    countStartLabel.destroy()
    countStart.destroy()

def countdownBeforeTurn():
    global click
    for k in range(1, -1, -1):
        click = False
        app.update()
        time.sleep(0.07)
    click = True

def fortissimo():
    global click
    for k in range(1, -1, -1):
        click = False
        app.update()
        time.sleep(0.009)
    click = True

def pianissimo():
    global click
    for k in range(1, -1, -1):
        click = False
        app.update()
        time.sleep(0.007)
    click = True

def countdownRotation():

    labelRot = tk.Label(game, text='', font=("Helvetica 15 italic bold underline"), bg='black', fg='yellow')
    labelRot.place(x=250, y=350)
    for k in range(3, -1, -1):
        labelRot["text"] = k
        labelRot["text"] = "ROTATION DU JEU"
        app.update()
        time.sleep(0.09)
    labelRot.destroy()

def mozart():
    # ===========================
    b1.config(bg="white")
    countdownBeforeTurn()
    b1.config(bg="black")
    b3.config(bg="white")
    countdownBeforeTurn()
    b3.config(bg="black")
    b5.config(bg="white")
    countdownBeforeTurn()
    b5.config(bg="black")
    b2.config(bg="white")
    countdownBeforeTurn()
    b2.config(bg="black")
    b4.config(bg="white")
    countdownBeforeTurn()
    b4.config(bg="black")
    b9.config(bg="white")
    countdownBeforeTurn()
    b9.config(bg="black")
    b8.config(bg="white")
    countdownBeforeTurn()
    b8.config(bg="black")
    b7.config(bg="white")
    countdownBeforeTurn()
    b7.config(bg="black")
    b6.config(bg="white")
    countdownBeforeTurn()
    b6.config(bg="black")

    oldb1 = b1["text"]
    oldb2 = b2["text"]
    oldb3 = b3["text"]
    oldb4 = b4["text"]
    oldb5 = b5["text"]
    oldb6 = b6["text"]
    oldb7 = b7["text"]
    oldb8 = b8["text"]
    oldb9 = b9["text"]

    b1.config(bg="red", fg="red")
    countdownRotation()
    b4.config(bg="red", fg="red")
    countdownRotation()
    b7.config(bg="red", fg="red")
    countdownRotation()
    b8.config(bg="red", fg="red")
    countdownRotation()
    b9.config(bg="red", fg="red")
    countdownRotation()
    b6.config(bg="red", fg="red")
    countdownRotation()
    b3.config(bg="red", fg="red")
    countdownRotation()
    b2.config(bg="red", fg="red")
    countdownRotation()

    b1.config(bg="black", fg="black")
    b2.config(bg="black", fg="black")
    b3.config(bg="black", fg="black")
    b4.config(bg="black", fg="black")
    b5.config(bg="black", fg="black")
    b6.config(bg="black", fg="black")
    b7.config(bg="black", fg="black")
    b8.config(bg="black", fg="black")
    b9.config(bg="black", fg="black")

    b1["text"] = oldb3
    b2["text"] = oldb6
    b3["text"] = oldb9
    b4["text"] = oldb2
    b5["text"] = oldb5
    b6["text"] = oldb8
    b7["text"] = oldb1
    b8["text"] = oldb4
    b9["text"] = oldb7

    b1.config(bg="yellow")
    fortissimo()
    b1.config(bg="black")
    b2.config(bg="yellow")
    fortissimo()
    b2.config(bg="black")
    b3.config(bg="yellow")
    fortissimo()
    b3.config(bg="black")
    b4.config(bg="yellow")
    fortissimo()
    b4.config(bg="black")
    b5.config(bg="yellow")
    fortissimo()
    b5.config(bg="black")
    b6.config(bg="yellow")
    fortissimo()
    b6.config(bg="black")
    b7.config(bg="yellow")
    fortissimo()
    b7.config(bg="black")
    b8.config(bg="yellow")
    fortissimo()
    b8.config(bg="black")
    b9.config(bg="yellow")
    fortissimo()
    b9.config(bg="yellow")

    pianissimo()
    b9.config(bg="pink")
    pianissimo()
    b9.config(bg="black")
    b8.config(bg="pink")
    pianissimo()
    b8.config(bg="black")
    b7.config(bg="pink")
    pianissimo()
    b7.config(bg="black")
    b6.config(bg="pink")
    pianissimo()
    b6.config(bg="black")
    b5.config(bg="pink")
    pianissimo()
    b5.config(bg="black")
    b4.config(bg="pink")
    pianissimo()
    b4.config(bg="black")
    b3.config(bg="pink")
    pianissimo()
    b3.config(bg="black")
    b2.config(bg="pink")
    pianissimo()
    b2.config(bg="black")
    b1.config(bg="pink")
    pianissimo()
    b1.config(bg="black")

    fortissimo()
    b1.config(bg="yellow")
    fortissimo()
    b1.config(bg="black")
    b2.config(bg="yellow")
    fortissimo()
    b2.config(bg="black")
    b3.config(bg="yellow")
    fortissimo()
    b3.config(bg="black")
    b4.config(bg="yellow")
    fortissimo()
    b4.config(bg="black")
    b5.config(bg="yellow")
    fortissimo()
    b5.config(bg="black")
    b6.config(bg="yellow")
    fortissimo()
    b6.config(bg="black")
    b7.config(bg="yellow")
    fortissimo()
    b7.config(bg="black")
    b8.config(bg="yellow")
    fortissimo()
    b8.config(bg="black")
    b9.config(bg="yellow")
    fortissimo()
    b9.config(bg="yellow")

    pianissimo()
    b9.config(bg="pink")
    pianissimo()
    b9.config(bg="black")
    b8.config(bg="pink")
    pianissimo()
    b8.config(bg="black")
    b7.config(bg="pink")
    pianissimo()
    b7.config(bg="black")
    b6.config(bg="pink")
    pianissimo()
    b6.config(bg="black")
    b5.config(bg="pink")
    pianissimo()
    b5.config(bg="black")
    b4.config(bg="pink")
    pianissimo()
    b4.config(bg="black")
    b3.config(bg="pink")
    pianissimo()
    b3.config(bg="black")
    b2.config(bg="pink")
    pianissimo()
    b2.config(bg="black")
    b1.config(bg="pink")
    pianissimo()
    b1.config(bg="black")

def Flash():
    # ===========================
    b1.config(bg="white")
    countdownBeforeTurn()
    b1.config(bg="black")
    b3.config(bg="white")
    countdownBeforeTurn()
    b3.config(bg="black")
    b5.config(bg="white")
    countdownBeforeTurn()
    b5.config(bg="black")
    b2.config(bg="white")
    countdownBeforeTurn()
    b2.config(bg="black")
    b4.config(bg="white")
    countdownBeforeTurn()
    b4.config(bg="black")
    b9.config(bg="white")
    countdownBeforeTurn()
    b9.config(bg="black")
    b8.config(bg="white")
    countdownBeforeTurn()
    b8.config(bg="black")
    b7.config(bg="white")
    countdownBeforeTurn()
    b7.config(bg="black")
    b6.config(bg="white")
    countdownBeforeTurn()
    b6.config(bg="black")
    # ================================

def countdownBeforeClose():
    global click

    for k in range(3, -1, -1):
        click = False
        countCloseLabel["text"] = k
        countClose["text"] = "Compte-a-rebours avant fermeture \n tes donnees ont ete save inchallah"
        app.update()
        time.sleep(1)

#global settings
y = "" #sign attribution
player = []
playerBot = []
click = True
winBot = 0
winUser = 0
draw = 0

def randomChoice():
    global i
    global click
    y = "O"
    b = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    i = random.choice(b)

    if i["text"] == " ":
        i.config(text=y)
        click = True
    else:
        randomChoice()

#=======================================GAAME DIFFICULTIES
def startGameVirtuoso(b):
    global x, y
    global player, playerBot
    global click

    #global game
    #global win

    #b1
    # winner check
    checkWin()
    if b == b1:
        if b1["text"] == " " and click == True:
            y = 'X'
            b1.config(text=y)
            click = False
            # ===========================
            mozart()
            # ================================
            try:
                attack()
                checkWin()
            except:
                # bot's strategy
                if b1["text"] == 'X' and b4["text"] == " ":
                    y = 'O'
                    b7.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b4["text"] == 'X' and b1["text"] == " ":
                    y = 'O'
                    b1.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b3["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b5["text"] == 'X' and b3["text"] == " ":
                    y = 'O'
                    b3.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b9["text"] == 'X' and b8["text"] == " ":
                    y = 'O'
                    b8.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b8["text"] == 'X' and b9["text"] == " ":
                    y = 'O'
                    b9.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True

                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b2["text"] == " ":
                        b2.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True

                    elif b3["text"] == " ":
                        b3.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True

    elif b == b2:
        # b2
        if b2["text"] == " " and click == True:
            y = 'X'
            b2.config(text=y)
            click = False
            # ===========================
            mozart()
            # ================================
            try:
                attack()
                checkWin()
            except:
                # botStrat
                if b1["text"] == 'X' and b7["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b7["text"] == 'X' and b1["text"] == " ":
                    y = 'O'
                    b1.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b5["text"] == 'X' and b6["text"] == " ":
                    y = 'O'
                    b4.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b6["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True

                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b5["text"] == " ":
                        b5.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True

                    elif b9["text"] == " ":
                        b9.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True

    elif b == b3:
        # b3
        if b3["text"] == " " and click == True:
            y = 'X'
            b3.config(text=y)
            click = False
            # ===========================
            mozart()
            # ================================
            try:
                attack()
                checkWin()
            except:
                # botStrat
                if b4["text"] == 'X' and b7["text"] == " ":
                    y = 'O'
                    b7.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b7["text"] == 'X' and b4["text"] == " ":
                    y = 'O'
                    b4.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b5["text"] == 'X' and b9["text"] == " ":
                    y = 'O'
                    b9.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b9["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b2["text"] == 'X' and b3["text"] == " ":
                    y = 'O'
                    b3.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b3["text"] == 'X' and b2["text"] == " ":
                    y = 'O'
                    b6.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True

                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b2["text"] == " ":
                        b2.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b5["text"] == " ":
                        b5.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True

    elif b == b4:
        # b4
        if b4["text"] == " " and click == True:
            y = 'X'
            b4.config(text=y)
            click = False
            # ===========================
            mozart()
            # ================================
            try:
                attack()
                checkWin()
            except:
                # botStrat
                if b7["text"] == 'X' and b9["text"] == " ":
                    y = 'O'
                    b9.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b9["text"] == 'X' and b7["text"] == " ":
                    y = 'O'
                    b7.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b5["text"] == 'X' and b3["text"] == " ":
                    y = 'O'
                    b3.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b3["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True

                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True

                    elif b2["text"] == " ":
                        b2.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True

    elif b == b5:
        # b5
        if b5["text"] == " " and click == True:
            y = 'X'
            b5.config(text=y)
            click = False
            # ===========================
            mozart()
            # ================================
            try:
                attack()
                checkWin()
            except:
                # botStrat
                if b1["text"] == 'X' and b9["text"] == " ":
                    y = 'O'
                    b9.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b3["text"] == 'X' and b7["text"] == " ":
                    y = 'O'
                    b7.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b2["text"] == 'X' and b8["text"] == " ":
                    y = 'O'
                    b8.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b4["text"] == 'X' and b6["text"] == " ":
                    y = 'O'
                    b6.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b6["text"] == 'X' and b4["text"] == " ":
                    y = 'O'
                    b4.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b7["text"] == 'X' and b3["text"] == " ":
                    y = 'O'
                    b3.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b8["text"] == 'X' and b2["text"] == " ":
                    y = 'O'
                    b2.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b9["text"] == 'X' and b1["text"] == " ":
                    y = 'O'
                    b1.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True

                else:
                    y = 'O'
                    if b1["text"] == " ":
                        b1.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b2["text"] == " ":
                        b2.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True

    elif b == b6:
        # b6
        if b6["text"] == " " and click == True:
            y = 'X'
            b6.config(text=y)
            click = False
            # ===========================
            mozart()
            # ================================
            try:
                attack()
                checkWin()
            except:
                # botStrat
                if b3["text"] == 'X' and b1["text"] == " ":
                    y = 'O'
                    b1.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b1["text"] == 'X' and b3["text"] == " ":
                    y = 'O'
                    b3.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b5["text"] == 'X' and b8["text"] == " ":
                    y = 'O'
                    b8.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b8["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True

                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b2["text"] == " ":
                        b2.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True

    elif b == b7:
        # b7
        if b7["text"] == " " and click == True:
            y = 'X'
            b7.config(text=y)
            click = False
            # ===========================
            mozart()
            # ================================
            try:
                attack()
                checkWin()
            except:
                # botStrat
                if b7["text"] == 'X' and b8["text"] == " ":
                    y = 'O'
                    b8.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b8["text"] == 'X' and b7["text"] == " ":
                    y = 'O'
                    b7.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b6["text"] == 'X' and b3["text"] == " ":
                    y = 'O'
                    b3.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b3["text"] == 'X' and b6["text"] == " ":
                    y = 'O'
                    b6.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b5["text"] == 'X' and b1["text"] == " ":
                    y = 'O'
                    b1.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b1["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True

                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b2["text"] == " ":
                        b2.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True

    elif b == b8:
        # b8
        if b8["text"] == " " and click == True:
            y = 'X'
            b8.config(text=y)
            click = False
            # ===========================
            mozart()
            # ================================
            try:
                attack()
                checkWin()
            except:
                # botStrat
                if b2["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b5["text"] == 'X' and b2["text"] == " ":
                    y = 'O'
                    b2.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b7["text"] == 'X' and b9["text"] == " ":
                    y = 'O'
                    b9.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b9["text"] == 'X' and b7["text"] == " ":
                    y = 'O'
                    b7.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True

                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b2["text"] == " ":
                        b2.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True

    elif b == b9:
        # b9
        if b9["text"] == " " and click == True:
            y = 'X'
            b9.config(text=y)
            click = False
            # ===========================
            mozart()
            # ================================
            try:
                attack()
                checkWin()
            except:
                # botStrat
                if b1["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b3["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b5["text"] == 'X' and b1["text"] == " ":
                    y = 'O'
                    b1.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b7["text"] == 'X' and b8["text"] == " ":
                    y = 'O'
                    b8.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b8["text"] == 'X' and b7["text"] == " ":
                    y = 'O'
                    b7.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True
                elif b6["text"] == 'X' and b3["text"] == " ":
                    y = 'O'
                    b6.config(text=y)
                    # ===========================
                    mozart()
                    # ================================
                    click = True

                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        # ===========================
                        mozart()
                        # ==================
                        click = True
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b2["text"] == " ":
                        b2.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        # ===========================
                        mozart()
                        # ================================
                        click = True

    checkWin()

#mode flash + defense + strategic pose (attack disabled so he focus more on not making u win
def startGameCauchemar(b):
    global x, y
    global player, playerBot
    global click
    #b1

    if b == b1:
        if b1["text"] == " " and click == True:
            y = 'X'
            b1.config(text=y)
            click = False
            checkWin()
            #bot's strategy
            if b7["text"] == 'X' and b4["text"] == " ":
                y = 'O'
                b4.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b2["text"] == 'X' and b3["text"] == " ":
                y = 'O'
                b3.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b3["text"] == 'X' and b2["text"] == " ":
                y = 'O'
                b2.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b4["text"] == 'X' and b7["text"] == " ":
                y = 'O'
                b7.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b5["text"] == 'X' and b9["text"] == " ":
                y = 'O'
                b9.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b9["text"] == 'X' and b5["text"] == " ":
                y = 'O'
                b5.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            else:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    #===========================
                    Flash()
                    #================================
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b8["text"] == " ":
                    b8.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b9["text"] == " ":
                    b9.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b7["text"] == " ":
                    b7.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()

    elif b == b2:
        #b2
        if b2["text"] == " " and click == True:
            y = 'X'
            b2.config(text=y)
            click = False
            checkWin()
            #botStrat
            if b1["text"] == 'X' and b3["text"] == " ":
                y = 'O'
                b3.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b3["text"] == 'X' and b1["text"] == " ":
                y = 'O'
                b1.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b5["text"] == 'X' and b8["text"] == " ":
                y = 'O'
                b8.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b8["text"] == 'X' and b5["text"] == " ":
                y = 'O'
                b5.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            else:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b8["text"] == " ":
                    b8.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b1["text"] == " ":
                    b1.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b5["text"] == " ":
                    b5.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b7["text"] == " ":
                    b7.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b9["text"] == " ":
                    b9.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()

    elif b == b3:
        #b3
        if b3["text"] == " " and click == True:
            y = 'X'
            b3.config(text=y)
            click = False
            checkWin()
            #botStrat
            if b1["text"] == 'X' and b2["text"] == " ":
                y = 'O'
                b2.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b2["text"] == 'X' and b1["text"] == " ":
                y = 'O'
                b1.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b5["text"] == 'X' and b7["text"] == " ":
                y = 'O'
                b7.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b6["text"] == 'X' and b9["text"] == " ":
                y = 'O'
                b9.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b7["text"] == 'X' and b5["text"] == " ":
                y = 'O'
                b5.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b9["text"] == 'X' and b6["text"] == " ":
                y = 'O'
                b6.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            else:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b8["text"] == " ":
                    b8.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b7["text"] == " ":
                    b7.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b9["text"] == " ":
                    b9.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b1["text"] == " ":
                    b1.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b5["text"] == " ":
                    b5.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()

    elif b == b4:
        #b4
        if b4["text"] == " " and click == True:
            y = 'X'
            b4.config(text=y)
            click = False
            checkWin()
            #botStrat
            if b1["text"] == 'X' and b7["text"] == " ":
                y = 'O'
                b7.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b5["text"] == 'X' and b6["text"] == " ":
                y = 'O'
                b6.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b6["text"] == 'X' and b5["text"] == " ":
                y = 'O'
                b5.config( text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b7["text"] == 'X' and b1["text"] == " ":
                y = 'O'
                b1.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            else:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b8["text"] == " ":
                    b8.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b1["text"] == " ":
                    b1.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b7["text"] == " ":
                    b7.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b9["text"] == " ":
                    b9.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()

    elif b == b5:
        #b5
        if b5["text"] == " " and click == True:
            y = 'X'
            b5.config(text=y)
            click = False
            checkWin()
            #botStrat
            if b1["text"] == 'X' and b9["text"] == " ":
                y = 'O'
                b9.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b3["text"] == 'X' and b7["text"] == " ":
                y = 'O'
                b7.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b2["text"] == 'X' and b8["text"] == " ":
                y = 'O'
                b8.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b4["text"] == 'X' and b6["text"] == " ":
                y = 'O'
                b6.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b6["text"] == 'X' and b4["text"] == " ":
                y = 'O'
                b4.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b7["text"] == 'X' and b3["text"] == " ":
                y = 'O'
                b3.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b8["text"] == 'X' and b2["text"] == " ":
                y = 'O'
                b2.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b9["text"] == 'X' and b1["text"] == " ":
                y = 'O'
                b1.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()

            else:
                y = 'O'
                if b2["text"] == " ":
                    b2.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif  b8["text"] == " ":
                    b8.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b1["text"] == " ":
                    b1.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif  b7["text"] == " ":
                    b7.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif  b9["text"] == " ":
                    b9.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()

    elif b == b6:
        #b6
        if b6["text"] == " " and click == True:
            y = 'X'
            b6.config(text=y)
            click = False
            checkWin()
            #botStrat
            if b3["text"] == 'X' and b9["text"] == " ":
                y = 'O'
                b9.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b4["text"] == 'X' and b5["text"] == " ":
                y = 'O'
                b5.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b5["text"] == 'X' and b4["text"] == " ":
                y = 'O'
                b4.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b9["text"] == 'X' and b3["text"] == " ":
                y = 'O'
                b3.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()

            else:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b8["text"] == " ":
                    b8.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b7["text"] == " ":
                    b7.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b9["text"] == " ":
                    b9.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b1["text"] == " ":
                    b1.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()

    elif b == b7:
        #b7
        if b7["text"] == " " and click == True:
            y = 'X'
            b7.config(text=y)
            click = False
            checkWin()
            #botStrat
            if b1["text"] == 'X' and b4["text"] == " ":
                y = 'O'
                b4.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b3["text"] == 'X' and b5["text"] == " ":
                y = 'O'
                b5.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b4["text"] == 'X' and b1["text"] == " ":
                y = 'O'
                b1.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b5["text"] == 'X' and b3["text"] == " ":
                y = 'O'
                b3.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b8["text"] == 'X' and b9["text"] == " ":
                y = 'O'
                b9.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b9["text"] == 'X' and b8["text"] == " ":
                y = 'O'
                b8.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()

            else:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b8["text"] == " ":
                    b8.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b1["text"] == " ":
                    b1.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b9["text"] == " ":
                    b9.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()

    elif b == b8:
        #b8
        if b8["text"] == " " and click == True:
            y = 'X'
            b8.config(text=y)
            click = False
            checkWin()
            #botStrat
            if b2["text"] == 'X' and b5["text"] == " ":
                y = 'O'
                b5.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b5["text"] == 'X' and b2["text"] == " ":
                y = 'O'
                b2.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b7["text"] == 'X' and b9["text"] == " ":
                y = 'O'
                b9.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b9["text"] == 'X' and b7["text"] == " ":
                y = 'O'
                b7.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()

            else:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b7["text"] == " ":
                    b7.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b9["text"] == " ":
                    b9.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b1["text"] == " ":
                    b1.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()

    elif b == b9:
        #b9
        if b9["text"] == " " and click == True:
            y = 'X'
            b9.config(text=y)
            click = False
            checkWin()
            #botStrat
            if b1["text"] == 'X' and b5["text"] == " ":
                y = 'O'
                b5.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b3["text"] == 'X' and b6["text"] == " ":
                y = 'O'
                b6.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b5["text"] == 'X' and b1["text"] == " ":
                y = 'O'
                b1.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b7["text"] == 'X' and b8["text"] == " ":
                y = 'O'
                b8.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b8["text"] == 'X' and b7["text"] == " ":
                y = 'O'
                b7.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()
            elif b6["text"] == 'X' and b3["text"] == " ":
                y = 'O'
                b6.config(text=y)
                # ===========================
                Flash()
                # ================================
                click = True
                checkWin()

            else:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b8["text"] == " ":
                    b8.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b1["text"] == " ":
                    b1.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    # ===========================
                    Flash()
                    # ==================
                    click = True
                    checkWin()
                elif b7["text"] == " ":
                    b7.config(text=y)
                    # ===========================
                    Flash()
                    # ================================
                    click = True
                    checkWin()

#mode defense + strategic pose + attack
def startGameExtreme(b):
    global x, y
    global player, playerBot
    global click

    global winBot
    global winUser

    #b1

    if b == b1:
        if b1["text"] == " " and click == True:
            y = 'X'
            b1.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                #bot's strategy
                if b7["text"] == 'X' and b4["text"] == " ":
                    y = 'O'
                    b4.config(text=y)
                    click = True
                    checkWin()
                elif b3["text"] == 'X' and b2["text"] == " ":
                    y = 'O'
                    b2.config(text=y)
                    click = True
                    checkWin()
                elif b9["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b2["text"] == 'X' and b3["text"] == " ":
                    y = 'O'
                    b3.config(text=y)
                    click = True
                    checkWin()
                elif b3["text"] == 'X' and b2["text"] == " ":
                    y = 'O'
                    b2.config(text=y)
                    click = True
                    checkWin()
                elif b4["text"] == 'X' and b7["text"] == " ":
                    y = 'O'
                    b7.config(text=y)
                    click = True
                    checkWin()
                elif b5["text"] == 'X' and b9["text"] == " ":
                    y = 'O'
                    b9.config(text=y)
                    click = True
                    checkWin()
                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        click = True
                        checkWin()
                    elif b2["text"] == " ":
                        b2.config(text=y)
                        click = True
                        checkWin()
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        click = True
                        checkWin()
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        click = True
                        checkWin()
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        click = True
                        checkWin()
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        click = True
                        checkWin()
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        click = True
                        checkWin()
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        click = True
                        checkWin()

    elif b == b2:
        #b2
        if b2["text"] == " " and click == True:
            y = 'X'
            b2.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                #botStrat-Defense
                if b1["text"] == 'X' and b3["text"] == " ":
                    y = 'O'
                    b3.config(text=y)
                    click = True
                    checkWin()
                elif b3["text"] == 'X' and b1["text"] == " ":
                    y = 'O'
                    b1.config(text=y)
                    click = True
                    checkWin()
                elif b5["text"] == 'X' and b8["text"] == " ":
                    y = 'O'
                    b8.config(text=y)
                    click = True
                    checkWin()
                elif b8["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    click = True
                    checkWin()
                else: #strategic position
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        click = True
                        checkWin()
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        click = True
                        checkWin()
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        click = True
                        checkWin()
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        click = True
                        checkWin()
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        click = True
                        checkWin()
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        click = True
                        checkWin()
                    elif b5["text"] == " ":
                        b5.config(text=y)
                        click = True
                        checkWin()
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        click = True
                        checkWin()
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        click = True
                        checkWin()

    elif b == b3:
        #b3
        if b3["text"] == " " and click == True:
            y = 'X'
            b3.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                #botStrat
                if b1["text"] == 'X' and b2["text"] == " ":
                    y = 'O'
                    b2.config(text=y)
                    click = True
                    checkWin()
                elif b2["text"] == 'X' and b1["text"] == " ":
                    y = 'O'
                    b1.config(text=y)
                    click = True
                    checkWin()
                elif b5["text"] == 'X' and b7["text"] == " ":
                    y = 'O'
                    b7.config(text=y)
                    click = True
                    checkWin()
                elif b6["text"] == 'X' and b9["text"] == " ":
                    y = 'O'
                    b9.config(text=y)
                    click = True
                    checkWin()
                elif b7["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b9["text"] == 'X' and b6["text"] == " ":
                    y = 'O'
                    b6.config(text=y)
                    click = True
                    checkWin()
                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        click = True
                        checkWin()
                    elif b2["text"] == " ":
                        b2.config(text=y)
                        click = True
                        checkWin()
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        click = True
                        checkWin()
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        click = True
                        checkWin()
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        click = True
                        checkWin()
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        click = True
                        checkWin()
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        click = True
                        checkWin()
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        click = True
                        checkWin()
                    elif b5["text"] == " ":
                        b5.config(text=y)
                        click = True
                        checkWin()

    elif b == b4:
        #b4
        if b4["text"] == " " and click == True:
            y = 'X'
            b4.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                #botStrat
                if b1["text"] == 'X' and b7["text"] == " ":
                    y = 'O'
                    b7.config(text=y)
                    click = True
                    checkWin()
                elif b5["text"] == 'X' and b6["text"] == " ":
                    y = 'O'
                    b6.config(text=y)
                    click = True
                    checkWin()
                elif b6["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b7["text"] == 'X' and b1["text"] == " ":
                    y = 'O'
                    b1.config(text=y)
                    click = True
                    checkWin()
                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        click = True
                        checkWin()
                    elif b2["text"] == " ":
                        b2.config(text=y)
                        click = True
                        checkWin()
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        click = True
                        checkWin()
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        click = True
                        checkWin()
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        click = True
                        checkWin()
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        click = True
                        checkWin()
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        click = True
                        checkWin()
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        click = True
                        checkWin()

    elif b == b5:
        #b5
        if b5["text"] == " " and click == True:
            y = 'X'
            b5.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                #botStrat
                if b1["text"] == 'X' and b9["text"] == " ":
                    y = 'O'
                    b9.config(text=y)
                    click = True
                    checkWin()
                elif b3["text"] == 'X' and b7["text"] == " ":
                    y = 'O'
                    b7.config(text=y)
                    click = True
                    checkWin()
                elif b2["text"] == 'X' and b8["text"] == " ":
                    y = 'O'
                    b8.config(text=y)
                    click = True
                    checkWin()
                elif b4["text"] == 'X' and b6["text"] == " ":
                    y = 'O'
                    b6.config(text=y)
                    click = True
                    checkWin()
                elif b6["text"] == 'X' and b4["text"] == " ":
                    y = 'O'
                    b4.config(text=y)
                    click = True
                    checkWin()
                elif b7["text"] == 'X' and b3["text"] == " ":
                    y = 'O'
                    b3.config(text=y)
                    click = True
                    checkWin()
                elif b8["text"] == 'X' and b2["text"] == " ":
                    y = 'O'
                    b2.config(text=y)
                    click = True
                    checkWin()
                elif b9["text"] == 'X' and b1["text"] == " ":
                    y = 'O'
                    b1.config(text=y)
                    click = True
                    checkWin()
                else:
                    y = 'O'
                    if b2["text"] == " ":
                        b2.config(text=y)
                        click = True
                        checkWin()
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        click = True
                        checkWin()
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        click = True
                        checkWin()
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        click = True
                        checkWin()
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        click = True
                        checkWin()
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        click = True
                        checkWin()
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        click = True
                        checkWin()
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        click = True
                        checkWin()

    elif b == b6:
        #b6
        if b6["text"] == " " and click == True:
            y = 'X'
            b6.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                #botStrat
                if b3["text"] == 'X' and b9["text"] == " ":
                    y = 'O'
                    b9.config(text=y)
                    click = True
                    checkWin()
                elif b4["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b5["text"] == 'X' and b4["text"] == " ":
                    y = 'O'
                    b4.config(text=y)
                    click = True
                    checkWin()
                elif b9["text"] == 'X' and b3["text"] == " ":
                    y = 'O'
                    b3.config(text=y)
                    click = True
                    checkWin()
                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        click = True
                        checkWin()
                    elif b2["text"] == " ":
                        b2.config(text=y)
                        click = True
                        checkWin()
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        click = True
                        checkWin()
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        click = True
                        checkWin()
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        click = True
                        checkWin()
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        click = True
                        checkWin()
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        click = True
                        checkWin()
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        click = True
                        checkWin()

    elif b == b7:
        #b7
        if b7["text"] == " " and click == True:
            y = 'X'
            b7.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                #botStrat
                if b1["text"] == 'X' and b4["text"] == " ":
                    y = 'O'
                    b4.config(text=y)
                    click = True
                    checkWin()
                elif b3["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b4["text"] == 'X' and b1["text"] == " ":
                    y = 'O'
                    b1.config(text=y)
                    click = True
                    checkWin()
                elif b5["text"] == 'X' and b3["text"] == " ":
                    y = 'O'
                    b3.config(text=y)
                    click = True
                    checkWin()
                elif b8["text"] == 'X' and b9["text"] == " ":
                    y = 'O'
                    b9.config(text=y)
                    click = True
                    checkWin()
                elif b9["text"] == 'X' and b8["text"] == " ":
                    y = 'O'
                    b8.config(text=y)
                    click = True
                    checkWin()
                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        click = True
                        checkWin()
                    elif b2["text"] == " ":
                        b2.config(text=y)
                        click = True
                        checkWin()
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        click = True
                        checkWin()
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        click = True
                        checkWin()
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        click = True
                        checkWin()
                    elif  b1["text"] == " ":
                        b1.config(text=y)
                        click = True
                        checkWin()
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        click = True
                        checkWin()
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        click = True
                        checkWin()

    elif b == b8:
        #b8
        if b8["text"] == " " and click == True:
            y = 'X'
            b8.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                #botStrat
                if b2["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b5["text"] == 'X' and b2["text"] == " ":
                    y = 'O'
                    b2.config(text=y)
                    click = True
                    checkWin()
                elif b7["text"] == 'X' and b9["text"] == " ":
                    y = 'O'
                    b9.config(text=y)
                    click = True
                    checkWin()
                elif b9["text"] == 'X' and b7["text"] == " ":
                    y = 'O'
                    b7.config(text=y)
                    click = True
                    checkWin()
                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        click = True
                        checkWin()
                    elif b2["text"] == " ":
                        b2.config(text=y)
                        click = True
                        checkWin()
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        click = True
                        checkWin()
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        click = True
                        checkWin()
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        click = True
                        checkWin()
                    elif b9["text"] == " ":
                        b9.config(text=y)
                        click = True
                        checkWin()
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        click = True
                        checkWin()
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        click = True
                        checkWin()

    elif b == b9:
        #b9
        if b9["text"] == " " and click == True:
            y = 'X'
            b9.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                #botStrat
                if b1["text"] == 'X' and b5["text"] == " ":
                    y = 'O'
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b3["text"] == 'X' and b6["text"] == " ":
                    y = 'O'
                    b6.config(text=y)
                    click = True
                    checkWin()
                elif b5["text"] == 'X' and b1["text"] == " ":
                    y = 'O'
                    b1.config(text=y)
                    click = True
                    checkWin()
                elif b7["text"] == 'X' and b8["text"] == " ":
                    y = 'O'
                    b8.config(text=y)
                    click = True
                    checkWin()
                elif b8["text"] == 'X' and b7["text"] == " ":
                    y = 'O'
                    b7.config(text=y)
                    click = True
                    checkWin()
                elif b6["text"] == 'X' and b3["text"] == " ":
                    y = 'O'
                    b6.config(text=y)
                    click = True
                    checkWin()
                else:
                    y = 'O'
                    if b5["text"] == " ":
                        b5.config(text=y)
                        click = True
                        checkWin()
                    elif b2["text"] == " ":
                        b2.config(text=y)
                        click = True
                        checkWin()
                    elif b8["text"] == " ":
                        b8.config(text=y)
                        click = True
                        checkWin()
                    elif b6["text"] == " ":
                        b6.config(text=y)
                        click = True
                        checkWin()
                    elif b4["text"] == " ":
                        b4.config(text=y)
                        click = True
                        checkWin()
                    elif b1["text"] == " ":
                        b1.config(text=y)
                        click = True
                        checkWin()
                    elif b3["text"] == " ":
                        b3.config(text=y)
                        click = True
                        checkWin()
                    elif b7["text"] == " ":
                        b7.config(text=y)
                        click = True
                        checkWin()

#mode attack + strategic pose
def startGameDifficile(b):
    global x, y
    global player, playerBot
    global click

    global winBot
    global winUser

    #b1

    if b == b1:
        if b1["text"] == " " and click == True:
            y = 'X'
            b1.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                #bot's strategy
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b9["text"] == " ":
                    b9.config(text=y)
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    click = True
                    checkWin()
                elif b7["text"] == " ":
                    b7.config(text=y)
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    click = True
                    checkWin()
                elif b8["text"] == " ":
                    b8.config(text=y)
                    click = True
                    checkWin()

    elif b == b2:
        #b2
        if b2["text"] == " " and click == True:
            y = 'X'
            b2.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b1["text"] == " ":
                    b1.config(text=y)
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    click = True
                    checkWin()
                elif b5["text"] == " ":
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b8["text"] == " ":
                    b8.config(text=y)
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    click = True
                    checkWin()
                elif b7["text"] == " ":
                    b7.config(text=y)
                    click = True
                    checkWin()
                elif b9["text"] == " ":
                    b9.config(text=y)
                    click = True
                    checkWin()

    elif b == b3:
        #b3
        if b3["text"] == " " and click == True:
            y = 'X'
            b3.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b7["text"] == " ":
                    b7.config(text=y)
                    click = True
                    checkWin()
                elif b9["text"] == " ":
                    b9.config(text=y)
                    click = True
                    checkWin()
                elif b1["text"] == " ":
                    b1.config(text=y)
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    click = True
                    checkWin()
                elif b5["text"] == " ":
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    click = True
                    checkWin()
                elif b8["text"] == " ":
                    b8.config(text=y)
                    click = True
                    checkWin()

    elif b == b4:
        #b4
        if b4["text"] == " " and click == True:
            y = 'X'
            b4.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b1["text"] == " ":
                    b1.config(text=y)
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    click = True
                    checkWin()
                elif b7["text"] == " ":
                    b7.config(text=y)
                    click = True
                    checkWin()
                elif b9["text"] == " ":
                    b9.config(text=y)
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    click = True
                    checkWin()
                elif b8["text"] == " ":
                    b8.config(text=y)
                    click = True
                    checkWin()

    elif b == b5:
        #b5
        if b5["text"] == " " and click == True:
            y = 'X'
            b5.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                y = 'O'
                if b1["text"] == " ":
                    b1.config(text=y)
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    click = True
                    checkWin()
                elif  b7["text"] == " ":
                    b7.config(text=y)
                    click = True
                    checkWin()
                elif  b8["text"] == " ":
                    b8.config(text=y)
                    click = True
                    checkWin()
                elif  b9["text"] == " ":
                    b9.config(text=y)
                    click = True
                    checkWin()

    elif b == b6:
        #b6
        if b6["text"] == " " and click == True:
            y = 'X'
            b6.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    click = True
                    checkWin()
                elif b7["text"] == " ":
                    b7.config(text=y)
                    click = True
                    checkWin()
                elif b9["text"] == " ":
                    b9.config(text=y)
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    click = True
                    checkWin()
                elif b1["text"] == " ":
                    b1.config(text=y)
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    click = True
                    checkWin()
                elif b8["text"] == " ":
                    b8.config(text=y)
                    click = True
                    checkWin()

    elif b == b7:
        #b7
        if b7["text"] == " " and click == True:
            y = 'X'
            b7.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif  b1["text"] == " ":
                    b1.config(text=y)
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    click = True
                    checkWin()
                elif b9["text"] == " ":
                    b9.config(text=y)
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    click = True
                    checkWin()
                elif b8["text"] == " ":
                    b8.config(text=y)
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    click = True
                    checkWin()

    elif b == b8:
        #b8
        if b8["text"] == " " and click == True:
            y = 'X'
            b8.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b7["text"] == " ":
                    b7.config(text=y)
                    click = True
                    checkWin()
                elif b9["text"] == " ":
                    b9.config(text=y)
                    click = True
                    checkWin()
                elif b1["text"] == " ":
                    b1.config(text=y)
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    click = True
                    checkWin()

    elif b == b9:
        #b9
        if b9["text"] == " " and click == True:
            y = 'X'
            b9.config(text=y)
            click = False
            checkWin()
            try:
                attack()
                checkWin()
            except:
                y = 'O'
                if b5["text"] == " ":
                    b5.config(text=y)
                    click = True
                    checkWin()
                elif b1["text"] == " ":
                    b1.config(text=y)
                    click = True
                    checkWin()
                elif b3["text"] == " ":
                    b3.config(text=y)
                    click = True
                    checkWin()
                elif b6["text"] == " ":
                    b6.config(text=y)
                    click = True
                    checkWin()
                elif b7["text"] == " ":
                    b7.config(text=y)
                    click = True
                    checkWin()
                elif b8["text"] == " ":
                    b8.config(text=y)
                    click = True
                    checkWin()
                elif b2["text"] == " ":
                    b2.config(text=y)
                    click = True
                    checkWin()
                elif b4["text"] == " ":
                    b4.config(text=y)
                    click = True
                    checkWin()

#mode strategic pose
def startGameMoyen(b):
    global x, y
    global player, playerBot
    global click

    global winBot
    global winUser
    #global game
    #global win



    #score.append(winUser)
    #score.append(winBot)

    # winner check

    #b1

    if b == b1:
        if b1["text"] == " " and click == True:
            y = 'X'
            b1.config(text=y)
            click = False
            checkWin()

            #bot's strategy
            y = 'O'
            if b5["text"] == " ":
                b5.config(text=y)
                click = True
                checkWin()
            elif b9["text"] == " ":
                b9.config(text=y)
                click = True
                checkWin()
            elif b2["text"] == " ":
                b2.config(text=y)
                click = True
                checkWin()
            elif b3["text"] == " ":
                b3.config(text=y)
                click = True
                checkWin()
            elif b4["text"] == " ":
                b4.config(text=y)
                click = True
                checkWin()
            elif b7["text"] == " ":
                b7.config(text=y)
                click = True
                checkWin()
            elif b6["text"] == " ":
                b6.config(text=y)
                click = True
                checkWin()
            elif b8["text"] == " ":
                b8.config(text=y)
                click = True
                checkWin()

    elif b == b2:
        #b2
        if b2["text"] == " " and click == True:
            y = 'X'
            b2.config(text=y)
            click = False
            checkWin()
            y = 'O'
            if b5["text"] == " ":
                b5.config(text=y)
                click = True
                checkWin()
            elif b1["text"] == " ":
                b1.config(text=y)
                click = True
                checkWin()
            elif b3["text"] == " ":
                b3.config(text=y)
                click = True
                checkWin()
            elif b5["text"] == " ":
                b5.config(text=y)
                click = True
                checkWin()
            elif b8["text"] == " ":
                b8.config(text=y)
                click = True
                checkWin()
            elif b4["text"] == " ":
                b4.config(text=y)
                click = True
                checkWin()
            elif b6["text"] == " ":
                b6.config(text=y)
                click = True
                checkWin()
            elif b7["text"] == " ":
                b7.config(text=y)
                click = True
                checkWin()
            elif b9["text"] == " ":
                b9.config(text=y)
                click = True
                checkWin()

    elif b == b3:
        #b3
        if b3["text"] == " " and click == True:
            y = 'X'
            b3.config(text=y)
            click = False
            checkWin()
            y = 'O'
            if b5["text"] == " ":
                b5.config(text=y)
                click = True
                checkWin()
            elif b7["text"] == " ":
                b7.config(text=y)
                click = True
                checkWin()
            elif b9["text"] == " ":
                b9.config(text=y)
                click = True
                checkWin()
            elif b1["text"] == " ":
                b1.config(text=y)
                click = True
                checkWin()
            elif b6["text"] == " ":
                b6.config(text=y)
                click = True
                checkWin()
            elif b5["text"] == " ":
                b5.config(text=y)
                click = True
                checkWin()
            elif b2["text"] == " ":
                b2.config(text=y)
                click = True
                checkWin()
            elif b4["text"] == " ":
                b4.config(text=y)
                click = True
                checkWin()
            elif b8["text"] == " ":
                b8.config(text=y)
                click = True
                checkWin()

    elif b == b4:
        #b4
        if b4["text"] == " " and click == True:
            y = 'X'
            b4.config(text=y)
            click = False
            checkWin()
            y = 'O'
            if b5["text"] == " ":
                b5.config(text=y)
                click = True
                checkWin()
            elif b1["text"] == " ":
                b1.config(text=y)
                click = True
                checkWin()
            elif b3["text"] == " ":
                b3.config(text=y)
                click = True
                checkWin()
            elif b7["text"] == " ":
                b7.config(text=y)
                click = True
                checkWin()
            elif b9["text"] == " ":
                b9.config(text=y)
                click = True
                checkWin()
            elif b6["text"] == " ":
                b6.config(text=y)
                click = True
                checkWin()
            elif b2["text"] == " ":
                b2.config(text=y)
                click = True
                checkWin()
            elif b8["text"] == " ":
                b8.config(text=y)
                click = True
                checkWin()

    elif b == b5:
        #b5
        if b5["text"] == " " and click == True:
            y = 'X'
            b5.config(text=y)
            click = False
            checkWin()
            y = 'O'
            if b1["text"] == " ":
                b1.config(text=y)
                click = True
                checkWin()
            elif b2["text"] == " ":
                b2.config(text=y)
                click = True
                checkWin()
            elif b3["text"] == " ":
                b3.config(text=y)
                click = True
                checkWin()
            elif b4["text"] == " ":
                b4.config(text=y)
                click = True
                checkWin()
            elif b6["text"] == " ":
                b6.config(text=y)
                click = True
                checkWin()
            elif  b7["text"] == " ":
                b7.config(text=y)
                click = True
                checkWin()
            elif  b8["text"] == " ":
                b8.config(text=y)
                click = True
                checkWin()
            elif  b9["text"] == " ":
                b9.config(text=y)
                click = True
                checkWin()

    elif b == b6:
        #b6
        if b6["text"] == " " and click == True:
            y = 'X'
            b6.config(text=y)
            click = False
            checkWin()
            y = 'O'
            if b5["text"] == " ":
                b5.config(text=y)
                click = True
                checkWin()
            elif b3["text"] == " ":
                b3.config(text=y)
                click = True
                checkWin()
            elif b7["text"] == " ":
                b7.config(text=y)
                click = True
                checkWin()
            elif b9["text"] == " ":
                b9.config(text=y)
                click = True
                checkWin()
            elif b4["text"] == " ":
                b4.config(text=y)
                click = True
                checkWin()
            elif b1["text"] == " ":
                b1.config(text=y)
                click = True
                checkWin()
            elif b2["text"] == " ":
                b2.config(text=y)
                click = True
                checkWin()
            elif b8["text"] == " ":
                b8.config(text=y)
                click = True
                checkWin()

    elif b == b7:
        #b7
        if b7["text"] == " " and click == True:
            y = 'X'
            b7.config(text=y)
            click = False
            checkWin()
            y = 'O'
            if b5["text"] == " ":
                b5.config(text=y)
                click = True
                checkWin()
            elif  b1["text"] == " ":
                b1.config(text=y)
                click = True
                checkWin()
            elif b3["text"] == " ":
                b3.config(text=y)
                click = True
                checkWin()
            elif b9["text"] == " ":
                b9.config(text=y)
                click = True
                checkWin()
            elif b4["text"] == " ":
                b4.config(text=y)
                click = True
                checkWin()
            elif b8["text"] == " ":
                b8.config(text=y)
                click = True
                checkWin()
            elif b2["text"] == " ":
                b2.config(text=y)
                click = True
                checkWin()
            elif b6["text"] == " ":
                b6.config(text=y)
                click = True
                checkWin()

    elif b == b8:
        #b8
        if b8["text"] == " " and click == True:
            y = 'X'
            b8.config(text=y)
            click = False
            checkWin()
            y = 'O'
            if b5["text"] == " ":
                b5.config(text=y)
                click = True
                checkWin()
            elif b7["text"] == " ":
                b7.config(text=y)
                click = True
                checkWin()
            elif b9["text"] == " ":
                b9.config(text=y)
                click = True
                checkWin()
            elif b1["text"] == " ":
                b1.config(text=y)
                click = True
                checkWin()
            elif b3["text"] == " ":
                b3.config(text=y)
                click = True
                checkWin()
            elif b2["text"] == " ":
                b2.config(text=y)
                click = True
                checkWin()
            elif b4["text"] == " ":
                b4.config(text=y)
                click = True
                checkWin()
            elif b6["text"] == " ":
                b6.config(text=y)
                click = True
                checkWin()

    elif b == b9:
        #b9
        if b9["text"] == " " and click == True:
            y = 'X'
            b9.config(text=y)
            click = False
            checkWin()
            y = 'O'
            if b5["text"] == " ":
                b5.config(text=y)
                click = True
                checkWin()
            elif b1["text"] == " ":
                b1.config(text=y)
                click = True
                checkWin()
            elif b3["text"] == " ":
                b3.config(text=y)
                click = True
                checkWin()
            elif b6["text"] == " ":
                b6.config(text=y)
                click = True
                checkWin()
            elif b7["text"] == " ":
                b7.config(text=y)
                click = True
                checkWin()
            elif b8["text"] == " ":
                b8.config(text=y)
                click = True
                checkWin()
            elif b2["text"] == " ":
                b2.config(text=y)
                click = True
                checkWin()
            elif b4["text"] == " ":
                b4.config(text=y)
                click = True
                checkWin()

#mode random
def startGameFacile(b):
    global x, y
    global player, playerBot
    global click
    global winBot
    global winUser
    #b1

    if b == b1:
        if b1["text"] == " " and click == True:
            y = 'X'
            b1.config(text=y)
            click = False
            checkWin()
            #bot's strategy
            randomChoice()

    elif b == b2:
        #b2
        if b2["text"] == " " and click == True:
            y = 'X'
            b2.config(text=y)
            click = False
            checkWin()
            randomChoice()

    elif b == b3:
        #b3
        if b3["text"] == " " and click == True:
            y = 'X'
            b3.config(text=y)
            click = False
            checkWin()
            randomChoice()

    elif b == b4:
        #b4
        if b4["text"] == " " and click == True:
            y = 'X'
            b4.config(text=y)
            click = False
            checkWin()
            randomChoice()

    elif b == b5:
        #b5
        if b5["text"] == " " and click == True:
            y = 'X'
            b5.config(text=y)
            click = False
            checkWin()
            randomChoice()

    elif b == b6:
        #b6
        if b6["text"] == " " and click == True:
            y = 'X'
            b6.config(text=y)
            click = False
            checkWin()
            randomChoice()

    elif b == b7:
        #b7
        if b7["text"] == " " and click == True:
            y = 'X'
            b7.config(text=y)
            click = False
            checkWin()
            randomChoice()

    elif b == b8:
        #b8
        if b8["text"] == " " and click == True:
            y = 'X'
            b8.config(text=y)
            click = False
            checkWin()
            randomChoice()

    elif b == b9:
        #b9
        if b9["text"] == " " and click == True:
            y = 'X'
            b9.config(text=y)
            click = False
            checkWin()
            randomChoice()
#=====================================

#INIT
def initialisation():
    global gamesNb
    global diffMode
    global winUser
    global winBot
    global draw

    winUser = 0
    winBot = 0
    draw = 0
    gamesNb = nb.get()
    diffMode = df.get()

    pygame.mixer.init()



    lDf = ["facile", "moyen", "difficile", "extreme", "cauchemar", "virtuoso"] #current difficulties : Extreme + Cauchemar


    if diffMode in lDf:
        try:
            gamesNb = int(gamesNb)
            if (gamesNb > 5):
                pygame.mixer.music.load('./sound/error.ogg')
                pygame.mixer.music.play()
                nb.set("No life! joue - !")
            elif (gamesNb > 0):
                # SOUND===
                pygame.mixer.music.load('./sound/play.ogg')
                pygame.mixer.music.play()
                gameOpen(gamesNb)
            else:
                pygame.mixer.music.load('./sound/error.ogg')
                pygame.mixer.music.play()
                nb.set("WHUT")

        except ValueError:
            pygame.mixer.music.load('./sound/error.ogg')
            pygame.mixer.music.play()
            nb.set("ERROR VALUE")
            print("small error")

    elif (diffMode == "I SEE YOU"):
        try:
            gamesNb = int(gamesNb)
            if (gamesNb > 5):
                pygame.mixer.music.load('./sound/error.ogg')
                pygame.mixer.music.play()
                nb.set("No life! joue - !")
            elif (gamesNb > 0):
                # SOUND===
                pygame.mixer.music.load('./sound/play.ogg')
                pygame.mixer.music.play()
                #hardcoreOpen(gamesNb)


            else:
                pygame.mixer.music.load('./sound/error.ogg')
                pygame.mixer.music.play()
                nb.set("WHUT")

        except ValueError:
            pygame.mixer.music.load('./sound/error.ogg')
            pygame.mixer.music.play()
            nb.set("ERROR VALUE")
            print("small error")

    else:
        print("small error")
        pygame.mixer.music.load('./sound/error.ogg')
        pygame.mixer.music.play()
        df.set("ERROR NAME")


#tkinter custom=====================================================================================================================

app.withdraw() #hide app
app.update_idletasks()  # Update "requested size" from geometry manager
app.iconbitmap("./image/icon.ico/")
app.geometry("650x390")


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
nb = tk.StringVar() #nombre de round
df = tk.StringVar() #difficulte
playerShow = tk.StringVar()
#Labels==============================================================
#TITRE


#number of match
nbMatchLabel = tk.Label(app, text="Nombre de Round:", font="Helvetica 11 italic bold", bg='black', fg="#ff8d00")
nbMatchLabel.place(x=160, y=120)
nbMatch = tk.Entry(app, textvariable=nb, font="Helvetica 11 italic bold")
nb.set("1")
nbMatch.place(x=320, y=120)

#Difficulty status
nbDiffLabel = tk.Label(app, text="Niveau de difficulter:", font="Helvetica 11 italic bold", bg='black', fg="#ff8d00")
nbDiffLabel.place(x=160, y=150)

difflist = ["facile", "moyen", "difficile", "extreme", "cauchemar", "virtuoso"]
difficulty = tk.Spinbox(app, textvariable=df, from_=0, to=6, values=difflist, state='readonly', font="Helvetica 11 italic bold")
df.set("facile")
difficulty.place(x=325, y=150)


#player
plLabel = tk.Label(app, text="Bienvenue: ", font="Endgame 11 italic bold")
playerLabelShow = tk.Label(app, textvariable=playerShow, bg="pink", font="Helvetica 11 italic bold")
playerShow.set("Joueur: ???")
playerLabelShow.place(x= 102, y=300)
plLabel.place(x=10, y=300)

#Bottom
matchValidate = tk.Button(app, text="JOUER", font="Helvetica 11 italic bold", command=initialisation, bg='#ff8d00', fg="black")
matchValidate.place(x=270, y=190)
#=====================================================================

#LOGIN WINDOW=========================================================
#variable
collectNameLogin = tk.StringVar()
collectPassLogin = tk.StringVar()
#===========================
#onlineLB===
onlineTOP1 = tk.StringVar()
onlineTOP2 = tk.StringVar()
onlineTOP3 = tk.StringVar()
#===
virtuosoScore = tk.IntVar()
cauchemarScore = tk.IntVar()
extremeScore = tk.IntVar()
difficileScore = tk.IntVar()
moyenScore = tk.IntVar()
facileScore = tk.IntVar()
#===============================
#===LOGIN WINDOW====
userInfo = tk.Toplevel()
userInfo.protocol("WM_DELETE_WINDOW", closeRegistration)
userInfo.geometry('350x300')
userInfo.title("CONNECTION A VOTRE COMPTE")
userInfo.configure(background='white')
fontPhoto = tk.PhotoImage(file='./image/logoAPOCS.png')
fontPhotoResize = fontPhoto.subsample(30, 30) #resize pic
photoLabel = tk.Label(userInfo, image=fontPhotoResize, bg='white')
userInfo.resizable(False, False)

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


# LB LABEL===========================================================================================================
vicLabel = tk.Label(app, width=15, text="⭐MES VICTOIRES⭐", bg='black', fg='yellow')
vicLabel.place(x='510', y='200')

onlineVicLabel = tk.Label(app, width=15, text="⭐ONLINE TOP 3⭐", bg='black', fg='yellow')
onlineVicLabel.place(x='20', y='200')

virtuoso = tk.Label(app, width=12, text="VIRTUOSE >", bg='black', fg='DeepSkyBlue2', font="Helvetica 9")
virtuoso.place(x='490', y='220')
cauchemar = tk.Label(app, width=12, text="CAUCHEMAR >", bg='black', fg='DeepSkyBlue2', font="Helvetica 9")
cauchemar.place(x='490', y='240')
extreme = tk.Label(app, width=12, text="EXTREME >", bg='black', fg='DeepSkyBlue2', font="Helvetica 9")
extreme.place(x='490', y='260')
difficile = tk.Label(app, width=12, text="DIFFICILE >", bg='black', fg='DeepSkyBlue2', font="Helvetica 9")
difficile.place(x='490', y='280')
moyen = tk.Label(app, width=12, text="MOYEN >", bg='black', fg='DeepSkyBlue2', font="Helvetica 9")
moyen.place(x='490', y='300')
facile = tk.Label(app, width=12, text="FACILE >", bg='black', fg='DeepSkyBlue2', font="Helvetica 9")
facile.place(x='490', y='320')

#ONLINE LEADERBOARD
topPlayer1 = tk.Label(app, width=15, textvariable=onlineTOP1, bg='black', fg='cyan', font='Helvetica 9')
topPlayer1.place(x='20', y='225')
topPlayer1 = tk.Label(app, width=15, textvariable=onlineTOP2, bg='black', fg='cyan', font='Helvetica 9')
topPlayer1.place(x='20', y='250')
topPlayer1 = tk.Label(app, width=15, textvariable=onlineTOP3, bg='black', fg='cyan', font='Helvetica 9')
topPlayer1.place(x='20', y='275')

infoOnline = tk.Label(app, width=95, text="Pour pouvoir observer/mettre a jour le leaderboard en ligne il vous faut joue une partie! Critere du Leader: nombre de victoire", bg='green', fg='black', font='Times 9')
infoOnline.place(x="10", y="360")
#====OFFLINE RESULTS
virtuoseLabel = tk.Label(app, width=7, textvariable=virtuosoScore, bg='black', fg='white', font="Helvetica 9")
virtuoseLabel.place(x='580', y='220')
cauchemarLabel = tk.Label(app, textvariable=cauchemarScore, width=7, bg='black', fg='white', font="Helvetica 9")
cauchemarLabel.place(x='580', y='240')
extremeLabel = tk.Label(app, textvariable=extremeScore, width=7, bg='black', fg='white', font="Helvetica 9")
extremeLabel.place(x='580', y='260')
difficileLabel = tk.Label(app, textvariable=difficileScore, width=7, bg='black', fg='white', font="Helvetica 9")
difficileLabel.place(x='580', y='280')
moyenLabel = tk.Label(app, textvariable=moyenScore, width=7, bg='black', fg='white', font="Helvetica 9")
moyenLabel.place(x='580', y='300')
facileLabel = tk.Label(app, textvariable=facileScore, width=7, bg='black', fg='white', font="Helvetica 9")
facileLabel.place(x='580', y='320')
# ==================================================================================================

#Cancel
buttonCancel = tk.Button(userInfo, text='ANNULER', bg='black', fg='red2', font=("Helvetica 10 bold"), command=lambda: exit())

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


#Tkinter loop
app.mainloop()