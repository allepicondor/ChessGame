import numpy as np
import pygame
import Pieces
class Board:
    def __init__(self,Size,BoardSize):
        self.Sizex = Size
        self.Sizey = Size
        self.segment = Size/BoardSize
        self.BoardSize = BoardSize

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
        self.board[3][3] = Pieces.Rook(3,3,"white",self)
        self.board[4][2] = Pieces.Pawn(4,2,"black",self)
    def DrawPossibleMoves(self,win,selectedPiece):
        if selectedPiece != []:
            print()
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
                pygame.draw.rect(win, color, [DrawPos[0],DrawPos[1], self.segment,self.segment])


