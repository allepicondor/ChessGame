import numpy as np
import pygame
import Pieces
import copy
class Board:
    def __init__(self,Size,BoardSize):
        self.Sizex = Size
        self.Sizey = Size
        self.BoardSize = BoardSize
        self.segment = Size/BoardSize
        self.BoardSize = BoardSize
        self.whitePieces = {'king':[],'queen':[],'knight':[],'bishop':[],'rook':[],'pawn':[]}
        self.blackPieces = {'king':[],'queen':[],'knight':[],'bishop':[],'rook':[],'pawn':[]}
        self.WhiteMoves = []
        self.BlackMoves = []
        self.WhitePossibleMoves = []
        self.BlackPossibleMoves = []
        self.WhitePiecesLeft = 1
        self.blackPiecesLeft = 1

        self.board = np.ndarray((BoardSize,BoardSize),dtype=np.object)

        self.reset_Board()

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
        Attacker.PossibleMoves()
        for Pmove in Attacker.possibleMoves:
            if AtackeCord == [Pmove[0],Pmove[1]]:
                return True
        return False
    def FindPieces(self):
        self.whitePieces = {'king':[],'queen':[],'knight':[],'bishop':[],'rook':[],'pawn':[]}
        self.blackPieces = {'king':[],'queen':[],'knight':[],'bishop':[],'rook':[],'pawn':[]}
        for x in range(self.BoardSize):
            for y in range(self.BoardSize):
                if isinstance(self.board[x][y], Pieces.King):
                    if self.board[x][y].side == "white":
                        self.whitePieces["king"].append(self.board[x][y])
                        self.WhitePiecesLeft += 1
                    else:
                        self.blackPieces["king"].append(self.board[x][y])
                        self.blackPiecesLeft += 1
                if isinstance(self.board[x][y], Pieces.Pawn):
                    if self.board[x][y].side == "white":
                        self.whitePieces["pawn"].append(self.board[x][y])
                        self.WhitePiecesLeft += 1
                    else:
                        self.blackPieces["pawn"].append(self.board[x][y])
                        self.blackPiecesLeft += 1
                if isinstance(self.board[x][y], Pieces.Knight):
                    if self.board[x][y].side == "white":
                        self.whitePieces["knight"].append(self.board[x][y])
                        self.WhitePiecesLeft += 1
                    else:
                        self.blackPieces["knight"].append(self.board[x][y])
                        self.blackPiecesLeft += 1
                if isinstance(self.board[x][y], Pieces.Bishop):
                    if self.board[x][y].side == "white":
                        self.whitePieces["bishop"].append(self.board[x][y])
                        self.WhitePiecesLeft += 1
                    else:
                        self.blackPieces["bishop"].append(self.board[x][y])
                        self.blackPiecesLeft += 1
                if isinstance(self.board[x][y], Pieces.Rook):
                    if self.board[x][y].side == "white":
                        self.whitePieces["rook"].append(self.board[x][y])
                        self.WhitePiecesLeft += 1
                    else:
                        self.blackPieces["rook"].append(self.board[x][y])
                        self.blackPiecesLeft += 1
                if isinstance(self.board[x][y], Pieces.Queen):
                    if self.board[x][y].side == "white":
                        self.whitePieces["queen"].append(self.board[x][y])
                        self.WhitePiecesLeft += 1
                    else:
                        self.blackPieces["queen"].append(self.board[x][y])
                        self.blackPiecesLeft += 1
    def CheckKings(self):
        try:
            WhiteX = self.whitePieces["king"][0].x
            WhiteY = self.whitePieces["king"][0].y
            if not isinstance(self.board[WhiteX][WhiteY], Pieces.King):
                return "black"
            elif self.board[WhiteX][WhiteY].side != "white":
                return "black"
        except IndexError:
            return "black"
        try:
            BlackX = self.blackPieces["king"][0].x
            BlackY = self.blackPieces["king"][0].y
            if not isinstance(self.board[BlackX][BlackY], Pieces.King):
                return "white"
            elif self.board[BlackX][BlackY].side != "black":
                return "white"
        except IndexError:
            return "white"
        return None
            
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
        self.board[3][0] = Pieces.Queen(3,0,"black",self)
        self.board[4][7] = Pieces.King(4,7,"white",self)
        self.board[4][0] = Pieces.King(4,0,"black",self)
        '''self.board[2][2] = Pieces.Bishop(2,2,"black",self)
        self.board[4][4] = Pieces.Pawn(4,4,"black",self)
        self.board[3][5] = Pieces.Pawn(3,5,"white",self)
        self.board[5][3] = Pieces.Pawn(5,3,"black",self)
        self.board[5][5] = Pieces.Pawn(5,5,"white",self)'''
    def move(self,previousPoistion,NextPosition):
        #print(previousPoistion,NextPosition)
        px = previousPoistion[0]
        py = previousPoistion[1]
        for move in self.board[px][py].possibleMoves:
            if [move[0],move[1]] == NextPosition:
                if len(move) <= 2:
                    nx = NextPosition[0]
                    ny = NextPosition[1]
                    if self.board[px][py] != None:
                        self.board[px][py].x = nx
                        self.board[px][py].y = ny
                        Old = self.board[px][py]
                        self.board[px][py] = None
                        self.board[nx][ny] = Old
                        self.board[nx][ny].possibleMoves = []
                        if self.board[nx][ny].FirstMove:
                            self.board[nx][ny].FirstMove = False
                        self.FindPlayersPossibleMoves('white')
                        self.FindPlayersPossibleMoves('black')
                else:
                    nx = move[0]
                    ny = move[1]
                    if self.board[px][py] != None:
                        self.board[px][py].x = nx
                        self.board[px][py].y = ny
                        Old = self.board[px][py]
                        self.board[px][py] = None
                        self.board[nx][ny] = Old
                        self.board[nx][ny].possibleMoves = []
                        if self.board[nx][ny].FirstMove:
                            self.board[nx][ny].FirstMove = False
                    px = move[2]
                    py = move[3]
                    nx = move[4]
                    ny = move[5]
                    if self.board[px][py] != None:
                        self.board[px][py].x = nx
                        self.board[px][py].y = ny
                        Old = self.board[px][py]
                        self.board[px][py] = None
                        self.board[nx][ny] = Old
                        self.board[nx][ny].possibleMoves = []
                        if self.board[nx][ny].FirstMove:
                            self.board[nx][ny].FirstMove = False
                        self.FindPlayersPossibleMoves('white')
                        self.FindPlayersPossibleMoves('black')

                    
                        self.FindPlayersPossibleMoves('white')
                        self.FindPlayersPossibleMoves('black')

    def FindPlayersPossibleMoves(self,side):
        if side == 'white':
            self.WhitePossibleMoves = []
            self.WhiteMoves = []
            for typeOfPiece in self.whitePieces.values():
                for piece in typeOfPiece:
                    piece.PossibleMoves()
                    moves = piece.possibleMoves
                    if moves != []:
                        self.WhitePossibleMoves.append([[piece.x,piece.y],moves])
                    try:
                        self.WhiteMoves.extend(piece.attackingMoves)
                    except Exception:
                        self.WhiteMoves.extend(piece.moves)
        elif side == 'black':
            self.BlackPossibleMoves = []
            self.BlackMoves = []
            for typeOfPiece in self.blackPieces.values():
                for piece in typeOfPiece:
                    piece.PossibleMoves()
                    moves = piece.possibleMoves
                    if moves != [] or moves == None:
                        self.BlackPossibleMoves.append([[piece.x,piece.y],moves])
                    try:
                        self.BlackMoves.extend(piece.attackingMoves)
                    except Exception:
                        self.BlackMoves.extend(piece.moves)
        '''print(self.WhitePossibleMoves)
        print(self.BlackPossibleMoves)'''
        
                    
        
    def DrawPossibleMoves(self,win,selectedPiece):
        if selectedPiece != []:
            self.board[selectedPiece[0]][selectedPiece[1]].drawPossibleMoves(win)
    def DrawPlayersPossibleMoves(self,win,player):
        if player == 'white':
            for piece in self.WhitePossibleMoves:
                for move in piece[1]:
                    move = self.GrabPixel(move)
                    pygame.draw.circle(win,[0,0,0], [int(move[0]+self.segment/2),int(move[1]+self.segment/2)], 10)
        if player == 'black':
            for piece in self.BlackPossibleMoves:
                for move in piece[1]:
                    move = self.GrabPixel(move)
                    pygame.draw.circle(win,[0,0,0], [int(move[0]+self.segment/2),int(move[1]+self.segment/2)], 10)
        pygame.display.update()

    def drawPieces(self,win):
        self.WhitePiecesLeft = 0
        self.blackPiecesLeft = 0
        for x in range(self.BoardSize):
            for y in range(self.BoardSize):
                if self.board[x][y] != None:
                    self.board[x][y].draw(win)
                    if self.board[x][y].side == 'white':
                        self.WhitePiecesLeft += 1
                    else:
                        self.blackPiecesLeft += 1

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


