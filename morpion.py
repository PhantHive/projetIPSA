#Librairies
import tkinter as tk


#Tkinter app
app = tk.Tk()
app.title("MORPION")


#Canvas
canvas = tk.Canvas(app, width=700, height=700)
canvas.pack()

#Vertical lines
verticalLine1 = canvas.create_line(260, 300, 500, -100000, width = 10, fill="black")
verticalLine2 = canvas.create_line(380, 300, 500, -100000, width = 10, fill="black")

#Horizontal lines
horizontalLine1 = canvas.create_line(150, 100, 475, 100, width = 10, fill="black")
horizontalLine2 = canvas.create_line(150, 200, 475, 200, width = 10, fill="black")

#Contour

#Vertical lines
leftTour = canvas.create_line(150, 300, 255, -100000, width=10, fill="orange")
rightTour = canvas.create_line(480, 300, 255, -100000, width=10, fill="orange")
#Horizontal lines
toptour = canvas.create_line(150, 0, 480, 0, width=10, fill="orange")
bottomtour = canvas.create_line(146, 305, 485, 305, width=10, fill="orange")

#Entry


#Labels


#Bottom


#tkinter customs
app.geometry("650x650")
app.iconbitmap("./image/background.XBM/")





#Tkinter loop
app.mainloop()