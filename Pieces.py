import pygame

class Pawn:
    def __init__(self,x,y,side,board):
        self.x = x
        self.y = y
        self.board = board
        self.possibleMoves = []
        self.side = side
        self.FirstMove = True#ONLY FOR PAWNSSSSSS
        self.Image = pygame.image.load('PiecesImg/Black/pawn.png')
        if side == 'white':
            self.Image = pygame.image.load('PiecesImg/White/pawn.png')
        self.Image = pygame.transform.scale(self.Image,(int(self.board.segment),int(self.board.segment)))
    def draw(self,win):
        pos = self.board.GrabPixel([self.x,self.y])
        win.blit(self.Image, (pos[0]-1,pos[1]-2))
        
        
    def drawPossibleMoves(self,win):
        for move in self.possibleMoves:
            pos = self.board.GrabPixel([move[0],move[1]])
            pos[0] += int(self.board.segment/2)
            pos[1] += int(self.board.segment/2)
            pygame.draw.circle(win,[255,255,255], pos, int(10))
    def PossibleMoves(self,board):
        self.possibleMoves = []
        self.board = board
        board = self.board.board
        x = self.x
        y = self.y
        if self.side == "black":
            if not (y+1 >= self.board.BoardSize or y+1 < 0):
                if board[x][y+1] == None:
                    self.possibleMoves.append([x,y+1])
            if not (x+1 >= self.board.BoardSize or x+1 < 0 or y+1 >= self.board.BoardSize or y+1 < 0):
                if board[x+1][y+1] != None:
                    if board[x+1][y+1].side == "white":
                        self.possibleMoves.append([x+1,y+1])
            if not (x-1 >= self.board.BoardSize or x-1 < 0 or y+1 >= self.board.BoardSize or y+1 < 0):
                if board[x-1][y+1] != None:
                    if board[x-1][y+1].side == "white":
                        self.possibleMoves.append([x-1,y+1])
            if not (y+2 >= self.board.BoardSize or y+2 < 0):
                if self.FirstMove:
                    if board[x][y+2] == None:
                        self.possibleMoves.append([x,y+2])
       
        else:
            if not (y-1 >= self.board.BoardSize or y-1 < 0):
                if board[x][y-1] == None:
                    self.possibleMoves.append([x,y-1])
            if not (x+1 >= self.board.BoardSize or x+1 < 0 or y-1 >= self.board.BoardSize or y-1 < 0):
                if board[x+1][y-1] != None:
                    if board[x+1][y-1].side == "black":
                        self.possibleMoves.append([x+1,y-1])
            if not (x-1 >= self.board.BoardSize or x-1 < 0 or y-1 >= self.board.BoardSize or y-1 < 0):
                if board[x-1][y-1] != None:
                    if board[x-1][y-1].side == "black":
                        self.possibleMoves.append([x-1,y-1])
            if not (y-2 >= self.board.BoardSize or y-2 < 0):
                if self.FirstMove:
                    if board[x][y-2] == None:
                        self.possibleMoves.append([x,y-2]) 
class Rook:
    def __init__(self,x,y,side,board):
        self.x = x
        self.y = y
        self.board = board
        self.possibleMoves = []
        self.side = side
        self.Image = pygame.image.load('PiecesImg/Black/Rook.png')
        if side == 'white':
            self.Image = pygame.image.load('PiecesImg/White/rook.png')
        self.Image = pygame.transform.scale(self.Image,(int(self.board.segment),int(self.board.segment)))
    def draw(self,win):
        pos = self.board.GrabPixel([self.x,self.y])
        win.blit(self.Image, (pos[0]-1,pos[1]-2))
        
    def drawPossibleMoves(self,win):
        for move in self.possibleMoves:
            pos = self.board.GrabPixel([move[0],move[1]])
            pos[0] += int(self.board.segment/2)
            pos[1] += int(self.board.segment/2)
            pygame.draw.circle(win,[0,255,0], pos, int(10))
    def PossibleMoves(self,board):
        self.possibleMoves = []
        self.board = board
        board = self.board.board
        x = self.x
        y = self.y
        #UP
        up = 1
        while True:
            if not (y-up < 0):
                CheckingPosition = board[x][y-up]
                if CheckingPosition != None:
                    if CheckingPosition.side != self.side:
                        self.possibleMoves.append([x,y-up])
                        break
                    else:
                        break
                else:
                    self.possibleMoves.append([x,y-up])
                up += 1
            else:
                break
        #DOWN
        down = 1
        while True:
            if not (y+down >= self.board.BoardSize):
                CheckingPosition = board[x][y+down]
                if CheckingPosition != None:
                    if CheckingPosition.side != self.side:
                        self.possibleMoves.append([x,y+down])
                        break
                    else:
                        break
                else:
                    self.possibleMoves.append([x,y+down])
                down += 1
            else:
                break
        #LEFT
        left = 1
        while True:
            if not (x-left < 0):
                CheckingPosition = board[x-left][y]
                if CheckingPosition != None:
                    if CheckingPosition.side !=self.side:
                        self.possibleMoves.append([x-left,y])
                        break
                    else:
                        break
                else:
                    self.possibleMoves.append([x-left,y])
                left += 1
            else:
                break
        #RIGHT
        right = 1
        while True:
            if not (x+right >= self.board.BoardSize):
                CheckingPosition = board[x+right][y]
                if CheckingPosition != None:
                    if CheckingPosition.side !=self.side:
                        self.possibleMoves.append([x+right,y])
                        break
                    else:
                        break
                else:
                    self.possibleMoves.append([x+right,y])
                right += 1
            else:
                break
class King:
    def __init__(self,x,y,side,board):
        self.x = x
        self.y = y
        self.board = board
        self.possibleMoves = []
        self.side = side
        
        self.Image = pygame.image.load('PiecesImg/Black/King.png')
        if side == 'white':
            self.Image = pygame.image.load('PiecesImg/White/King.png')
        self.Image = pygame.transform.scale(self.Image,(int(self.board.segment),int(self.board.segment)))
    def draw(self,win):
        pos = self.board.GrabPixel([self.x,self.y])
        win.blit(self.Image, (pos[0]-1,pos[1]-2))

    def drawPossibleMoves(self,win):
        for move in self.possibleMoves:
            pos = self.board.GrabPixel([move[0],move[1]])
            pos[0] += int(self.board.segment/2)
            pos[1] += int(self.board.segment/2)
            pygame.draw.circle(win,[255,255,255], pos, int(10))
    def PossibleMoves(self,board):
        self.possibleMoves = []
        self.board = board
        board = self.board.board
        x = self.x
        y = self.y
        try:
            if board[x][y-1] != None:# top
                if board[x][y-1].side != self.side:
                    self.possibleMoves.append([x,y-1])
            else:
                self.possibleMoves.append([x,y-1])

            if board[x+1][y-1] != None:#top right
                if board[x+1][y-1].side != self.side:
                    self.possibleMoves.append([x+1,y-1])
            else:
                self.possibleMoves.append([x+1,y-1])

            if board[x-1][y-1] != None:#Top Left
                if board[x-1][y-1].side != self.side:
                    self.possibleMoves.append([x-1,y-1])
            else:
                self.possibleMoves.append([x-1,y-1])

            if board[x][y+1] != None:# bottom
                if board[x][y+1].side != self.side:
                    self.possibleMoves.append([x,y+1])
            else:
                self.possibleMoves.append([x,y+1])

            if board[x+1][y+1] != None:#bottom Right
                if board[x+1][y+1].side != self.side:
                    self.possibleMoves.append([x+1,y+1])
            else:
                self.possibleMoves.append([x+1,y+1])

            if board[x-1][y+1] != None:#bottom Left
                if board[x-1][y+1].side != self.side:
                    self.possibleMoves.append([x-1,y+1])
            else:
                self.possibleMoves.append([x-1,y+1])

            if board[x-1][y] != None:# Left
                if board[x-1][y].side != self.side:
                    self.possibleMoves.append([x-1,y])
            else:
                self.possibleMoves.append([x-1,y])

            if board[x+1][y] != None:# Right
                if board[x+1][y].side != self.side:
                    self.possibleMoves.append([x+1,y])
            else:
                self.possibleMoves.append([x+1,y])

        except IndexError:
            pass
class Bishop:
    def __init__(self,x,y,side,board):
        self.x = x
        self.y = y
        self.board = board
        self.possibleMoves = []
        self.side = side
        self.Image = pygame.image.load('PiecesImg/Black/Bishop.png')
        if side == 'white':
            self.Image = pygame.image.load('PiecesImg/White/Bishop.png')
        self.Image = pygame.transform.scale(self.Image,(int(self.board.segment),int(self.board.segment)))
    def draw(self,win):
        pos = self.board.GrabPixel([self.x,self.y])
        win.blit(self.Image, (pos[0]-1,pos[1]-2))
        
    def drawPossibleMoves(self,win):
        for move in self.possibleMoves:
            pos = self.board.GrabPixel([move[0],move[1]])
            pos[0] += int(self.board.segment/2)
            pos[1] += int(self.board.segment/2)
            pygame.draw.circle(win,[0,255,0], pos, int(10))
    def PossibleMoves(self,board):
        self.possibleMoves = []
        self.board = board
        board = self.board.board
        x = self.x
        y = self.y
        #RIGHT UP
        up = 1
        right = 1
        while True:
            if not (x+right >= self.board.BoardSize or y-up < 0):
                CheckingPosition = board[x+right][y-up]
                if CheckingPosition != None:
                    if CheckingPosition.side != self.side:
                        self.possibleMoves.append([x+right,y-up])
                        break
                    else:
                        break
                else:
                    self.possibleMoves.append([x+right,y-up])
                up += 1
                right += 1
            else:
                break
        #RIGHT DOWN
        down = 1
        right = 1
        while True:
            if not (x+right >= self.board.BoardSize or y+down >= self.board.BoardSize):
                CheckingPosition = board[x+right][y+down]
                if CheckingPosition != None:
                    if CheckingPosition.side != self.side:
                        self.possibleMoves.append([x+right,y+down])
                        break
                    else:
                        break
                else:
                    self.possibleMoves.append([x+right,y+down])
                down += 1
                right += 1
            else:
                break
        #LEFT UP
        left = 1
        up = 1
        while True:
            if not (x-left < 0 or y-up < 0):
                CheckingPosition = board[x-left][y-up]
                if CheckingPosition != None:
                    if CheckingPosition.side !=self.side:
                        self.possibleMoves.append([x-left,y-up])
                        break
                    else:
                        break
                else:
                    self.possibleMoves.append([x-left,y-up])
                left += 1
                up += 1
            else:
                break
        #LEFT DOWN
        left = 1
        down = 1
        while True:
            if not (x-left < 0 or y+down >= self.board.BoardSize):
                CheckingPosition = board[x-left][y+down]
                if CheckingPosition != None:
                    if CheckingPosition.side !=self.side:
                        self.possibleMoves.append([x-left,y+down])
                        break
                    else:
                        break
                else:
                    self.possibleMoves.append([x-left,y+down])
                left += 1
                down += 1
            else:
                break
class Knight:
    def __init__(self,x,y,side,board):
        self.x = x
        self.y = y
        self.board = board
        self.possibleMoves = []
        self.side = side
        self.Image = pygame.image.load('PiecesImg/Black/Knight.png')
        if side == 'white':
            self.Image = pygame.image.load('PiecesImg/White/Knight.png')
        self.Image = pygame.transform.scale(self.Image,(int(self.board.segment),int(self.board.segment)))
    def draw(self,win):
        pos = self.board.GrabPixel([self.x,self.y])
        win.blit(self.Image, (pos[0]-1,pos[1]-2))
        
    def drawPossibleMoves(self,win):
        for move in self.possibleMoves:
            pos = self.board.GrabPixel([move[0],move[1]])
            pos[0] += int(self.board.segment/2)
            pos[1] += int(self.board.segment/2) 
            pygame.draw.circle(win,[0,255,0], pos, int(10))
    def PossibleMoves(self,board):
        self.possibleMoves = []
        self.board = board
        board = self.board.board
        x = self.x
        y = self.y
        if not (y-2 < 0):#UP
            if not (x+1 >= self.board.BoardSize): #UP RIGHT
                if board[x+1][y-2] != None:
                    if board[x+1][y-2].side != self.side:
                        self.possibleMoves.append([x+1,y-2])
                else:
                    self.possibleMoves.append([x+1,y-2])
            if not (x-1 < 0): #UP LEFT
                if board[x-1][y-2] != None:
                    if board[x-1][y-2].side != self.side:
                        self.possibleMoves.append([x-1,y-2])
                else:
                    self.possibleMoves.append([x-1,y-2])

        if not (y+2 >= self.board.BoardSize): #DOWN
            if not (x+1 >= self.board.BoardSize): #DOWN RIGHT
                if board[x+1][y+2] != None:
                    if board[x+1][y+2].side != self.side:
                        self.possibleMoves.append([x+1,y+2])
                else:
                    self.possibleMoves.append([x+1,y+2])
            if not (x-1 < 0): #DOWN LEFT
                if board[x-1][y+2] != None:
                    if board[x-1][y+2].side != self.side:
                        self.possibleMoves.append([x-1,y+2])
                else:
                    self.possibleMoves.append([x-1,y+2])

        if not (x+2 >= self.board.BoardSize): #RIGHT
            if not (y-1 < 0): #RIGHT UP
                if board[x+2][y-1] != None:
                    if board[x+2][y-1].side != self.side:
                        self.possibleMoves.append([x+2,y-1])
                else:
                        self.possibleMoves.append([x+2,y-1])

            if not (y+1 >= self.board.BoardSize): #RIGHT DOWN
                if board[x+2][y+1] != None:
                    if board[x+2][y+1].side != self.side:
                        self.possibleMoves.append([x+2,y+1])
                else:
                    self.possibleMoves.append([x+2,y+1])

        if not (x-2 < 0): #LEFT
            if not (y-1 < 0): #LEFT UP
                if board[x-2][y-1] != None:
                    if board[x-2][y-1].side != self.side:
                        self.possibleMoves.append([x-2,y-1])
                else:
                    self.possibleMoves.append([x-2,y-1])
            if not (y+1 >= self.board.BoardSize): #LEFT DOWN
                if board[x-2][y+1] != None:
                    if board[x-2][y+1].side != self.side:
                        self.possibleMoves.append([x-2,y+1])
                else:
                    self.possibleMoves.append([x-2,y+1])



