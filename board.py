import numpy as np
import pygame
import Pieces
class Board:
    def __init__(self,Size):
        self.Sizex = Size
        self.Sizey = Size
        self.segment = Size/8

        self.board = np.ndarray((8,8),dtype=np.object)

    def GrabPixel(self,pos):
        x = int(pos[0] * self.segment)
        y = int(pos[1] * self.segment)
        return [x,y]
    def GrabPos(self,pos):# pos != 659 pos == [659,800]
        x = int(pos[0] * .01)
        y = int(pos[1] * .01)
        return [x,y]
    def checkIfPossibleMove(self,AttackerCord,AtackeCord):
        Attacker = self.board[AttackerCord[0]][AttackerCord[1]]
        if AtackeCord in Attacker.possibleMoves:
            return True
        return False
    def reset_Board(self):
        self.board[4][7] = Pieces.Rook(4,7,[150,150,150],"white",self)
        self.board[4][2] = Pieces.Pawn(4,2,[0,0,0],"black",self)
    def EveryFrame(self):
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != None:
                    self.board[x][y].PossibleMoves(self)
    def drawPieces(self,win):
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != None:
                    self.board[x][y].draw(win)
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != None:
                    self.board[x][y].drawPossibleMoves(win)
    def DrawBoard(self,win):
        for x in range(8):
            for y in range(8):
                DrawPos = self.GrabPixel([x,y])
                color = [119,149,86]
                if x % 2 == 0:
                    if y % 2 == 0:
                        color = [235,236,208]
                else:
                    if y % 2 == 1:
                        color = [235,236,208]
                pygame.draw.rect(win, color, [DrawPos[0],DrawPos[1], self.segment,self.segment])

