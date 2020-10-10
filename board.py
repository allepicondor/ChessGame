import numpy as np
import pygame
import Pieces
class Board:
    def __init__(self,Size,BoardSize):
        self.Sizex = Size
        self.Sizey = Size
        self.segment = Size/BoardSize
        self.BoardSize = BoardSize
        self.posurt = []

        self.board = np.ndarray((BoardSize,BoardSize),dtype=np.object)

    def GrabPixel(self,pos):
        x = int(pos[0] * self.segment)
        y = int(pos[1] * self.segment)
        return [x,y]
    def GrabPos(self,pos):# pos != 175 pos == [659,800]
        x = int(pos[0] / self.segment)
        y = int(pos[1] / self.segment)
        return [x,y]
    def move_Check(self,AttackerCord,AtackeCord):
        Attacker = self.board[AttackerCord[0]][AttackerCord[1]]
        Attacker.PossibleMoves(self)
        if AtackeCord in Attacker.possibleMoves:
            return True
        return False



    def reset_Board(self):#Starting Piece Position
        for x in range(self.BoardSize):
            self.board[x][1] = Pieces.Pawn(x,1,"black",self)
            self.board[x][6] = Pieces.Pawn(x,6,"white",self)
        self.board[7][7] = Pieces.Rook(7,7,"white",self)
        self.board[0][7] = Pieces.Rook(0,7,"white",self)
        self.board[7][0] = Pieces.Rook(7,0,"black",self)
        self.board[0][0] = Pieces.Rook(0,0,"black",self)
        self.board[2][7] = Pieces.Bishop(2,7,"white",self)
        self.board[5][7] = Pieces.Bishop(5,7,"white",self)
        self.board[2][0] = Pieces.Bishop(2,0,"black",self)
        self.board[5][0] = Pieces.Bishop(5,0,"black",self)
        self.board[6][0] = Pieces.Knight(6,0,"black",self)
        self.board[1][0] = Pieces.Knight(1,0,"black",self)
        self.board[6][7] = Pieces.Knight(6,7,"white",self)
        self.board[1][7] = Pieces.Knight(1,7,"white",self)
        self.board[3][7] = Pieces.Queen(3,7,"white",self)
        self.board[4][0] = Pieces.Queen(4,0,"black",self)
        self.board[3][3] = Pieces.King(3,3,"white",self)
    def DrawPossibleMoves(self,win,selectedPiece):
        if selectedPiece != []:
            self.board[selectedPiece[0]][selectedPiece[1]].drawPossibleMoves(win)

    def drawPieces(self,win):
        for x in range(self.BoardSize):
            for y in range(self.BoardSize):
                if self.board[x][y] != None:
                    self.board[x][y].draw(win)
    def DrawBoard(self,win):
        for x in range(self.BoardSize):
            for y in range(self.BoardSize):
                DrawPos = self.GrabPixel([x,y])
                color = [119,149,86]
                if x % 2 == 0:
                    if y % 2 == 0:
                        color = [235,236,208]
                else:
                    if y % 2 == 1:
                        color = [235,236,208]
                pygame.draw.rect(win, color, [DrawPos[0],DrawPos[1], self.segment+1,self.segment+1])


