#Librairies
import tkinter as tk


#Tkinter app
app = tk.Tk()
app.title("MORPION")


#Canvas
canvas = tk.Canvas(app, width=700, height=700)
canvas.pack()

#Fonctions


def boardCreate():
    #Vertical lines
    canvas.create_line(260, 300, 500, -100000, width = 10, fill="black") #vertical line 1
    canvas.create_line(380, 300, 500, -100000, width = 10, fill="black") #vertical line 2

    #Horizontal lines
    canvas.create_line(150, 100, 475, 100, width = 10, fill="black") #horizontal line 1
    canvas.create_line(150, 200, 475, 200, width = 10, fill="black") #horizontal line 2

    #Contour
    #Vertical lines
    canvas.create_line(150, 300, 255, -100000, width=10, fill="orange") #left
    canvas.create_line(480, 300, 255, -100000, width=10, fill="orange") #right
    #Horizontal lines
    canvas.create_line(150, 0, 480, 0, width=10, fill="orange") #top
    canvas.create_line(146, 305, 485, 305, width=10, fill="orange") #bottom

def initialisation():
    gamesNb = nb.get()
    if (gamesNb != 0):
        boardCreate()
        

#Entry

nb = tk.IntVar()
nbMatch = tk.Entry(app, textvariable=nb)
nb.set("Max 5")
nbMatch.place(x=250, y=350)




#Labels


#Bottom
matchValidate = tk.Button(app, text="Valider", command=initialisation)
matchValidate.place(x=380, y=347)

#tkinter customs
app.geometry("650x650")
app.iconbitmap("./image/icon.ico/")

#Tkinter loop
app.mainloop()