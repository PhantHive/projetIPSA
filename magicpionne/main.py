#librairies
import tkinter as tk
import pymongo


class superPower:

    #25points
    def deleteCase(self):
        return

    #20points
    def moveCase(self):
        return

    #15points
    def blockCase(self):
        return

    #10points
    def rotateGame(self):
        return



class gameBoard:

    def __init__(self):

        #define empty case, player, bot and add size of our boardGame 3*3, then init a square dict
        self.empty = ' '
        self.player = 'X'
        self.bot = 'O'
        self.size = 3
        self.squares = {}
        # each square in squares must be define by x,y coordinate and be at first empty square
        for y in range(self.size):
            for x in range(self.size):
                self.squares[x, y] = self.empty

    #Only for player, he can make move in empty square
    def makeMove(self, x, y):
        board = gameBoard(self)
        self.squares[x, y] = self.player #display 'X'
        return board #so we can update board

    #MiniMax function return 2 things: totalPoint for each case
    def minimax(self):
        #we check possibilities of endGame then possibilities of player depending on what bot will choose best square
        return

    def draw(self):
        return


    def bestMove(self):
        return

    def win(self):
        return


'''
Goal: Make a game with perfect bot
      Make superPower works well!
'''