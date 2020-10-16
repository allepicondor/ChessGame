import pygame
MOVE_IMAGE = pygame.image.load('PiecesImg/PossibleMove.png')
PAWN_WHITE = pygame.image.load('PiecesImg/White/pawn.png')
PAWN_BLACK = pygame.image.load('PiecesImg/Black/pawn.png')
ROOK_WHITE = pygame.image.load('PiecesImg/White/rook.png')
ROOK_BLACK = pygame.image.load('PiecesImg/Black/Rook.png')
KING_WHITE = pygame.image.load('PiecesImg/White/King.png')
KING_BLACK = pygame.image.load('PiecesImg/Black/King.png')
QUEEN_WHITE = pygame.image.load('PiecesImg/White/Queen.png')
QUEEN_BLACK = pygame.image.load('PiecesImg/Black/Queen.png')
BISHOP_BLACK = pygame.image.load('PiecesImg/Black/Bishop.png')
BISHOP_WHITE = pygame.image.load('PiecesImg/White/Bishop.png')
KNIGHT_BLACK = pygame.image.load('PiecesImg/Black/Knight.png')
KNIGHT_WHITE = pygame.image.load('PiecesImg/White/Knight.png')
class Pawn:
    def __init__(self,x,y,side,board):
        self.x = x
        self.y = y
        self.worth = 1
        self.board = board
        self.possibleMoves = []
        self.attackingMoves = []
        self.moves = []
        self.side = side
        self.FirstMove = True

    def draw(self,win):
        if self.side == "white":
            pos = self.board.GrabPixel([self.x,self.y])
            win.blit(pygame.transform.scale(PAWN_WHITE,(int(self.board.segment),int(self.board.segment))), (pos[0]-1,pos[1]-2))
        else:
            pos = self.board.GrabPixel([self.x,self.y])
            win.blit(pygame.transform.scale(PAWN_BLACK,(int(self.board.segment),int(self.board.segment))), (pos[0]-1,pos[1]-2))
    def drawPossibleMoves(self,win):
        for pos in self.possibleMoves:
            pos = self.board.GrabPixel(pos)
            win.blit(pygame.transform.scale(MOVE_IMAGE,(int(self.board.segment/2),int(self.board.segment/2))), (pos[0]+self.board.segment/4,pos[1]+self.board.segment/4))
    def PossibleMoves(self):
        self.possibleMoves = []
        self.moves = []
        board = self.board.board
        x = self.x
        y = self.y
        if self.side == "black":
            if not (x+1 >= self.board.BoardSize or y+1 >= self.board.BoardSize):
                if board[x+1][y+1] != None:
                    if board[x+1][y+1].side == "white":
                        self.possibleMoves.append([x+1,y+1])
                    else:
                        self.moves.append([x+1,y+1])
                else:
                    self.attackingMoves.append([x+1,y+1])
                    self.moves.append([x+1,y+1])

            if not (x-1 < 0 or y+1 >= self.board.BoardSize):
                if board[x-1][y+1] != None:
                    if board[x-1][y+1].side == "white":
                        self.possibleMoves.append([x-1,y+1])
                    else:
                        self.moves.append([x-1,y+1])
                else:
                    self.attackingMoves.append([x-1,y+1])
                    self.moves.append([x+1,y+1])
            if not (y+1 >= self.board.BoardSize):
                if board[x][y+1] == None:
                    self.possibleMoves.append([x,y+1])
            if not (y+2 >= self.board.BoardSize):
                if self.FirstMove:
                    if board[x][y+2] == None and board[x][y+1] == None:
                        self.possibleMoves.append([x,y+2])
       
        else:
            if not (y-1 < 0):
                if board[x][y-1] == None:
                    self.possibleMoves.append([x,y-1])
            if not (x+1 >= self.board.BoardSize or y-1 < 0):
                if board[x+1][y-1] != None:
                    if board[x+1][y-1].side == "black":
                        self.possibleMoves.append([x+1,y-1])
                else:
                    self.attackingMoves.append([x+1,y-1])
            if not (x-1 < 0 or y-1 < 0):
                if board[x-1][y-1] != None:
                    if board[x-1][y-1].side == "black":
                        self.possibleMoves.append([x-1,y-1])
                else:
                    self.attackingMoves.append([x-1,y-1])
            if not (y-2 < 0):
                if self.FirstMove:
                    if board[x][y-2] == None and board[x][y-1] == None:
                        self.possibleMoves.append([x,y-2])
class Rook:
    def __init__(self,x,y,side,board):
        self.x = x
        self.y = y
        self.worth = 5
        self.board = board
        self.possibleMoves = []
        self.side = side
        self.moves = []
        self.FirstMove = True
        
    def draw(self,win):
        if self.side == "white":
            pos = self.board.GrabPixel([self.x,self.y])
            win.blit(pygame.transform.scale(ROOK_WHITE,(int(self.board.segment),int(self.board.segment))), (pos[0]-1,pos[1]-2))
        else:
            pos = self.board.GrabPixel([self.x,self.y])
            win.blit(pygame.transform.scale(ROOK_BLACK,(int(self.board.segment),int(self.board.segment))), (pos[0]-1,pos[1]-2))
        
    def drawPossibleMoves(self,win):
        for pos in self.possibleMoves:
            pos = self.board.GrabPixel(pos)
            win.blit(pygame.transform.scale(MOVE_IMAGE,(int(self.board.segment/2),int(self.board.segment/2))), (pos[0]+self.board.segment/4,pos[1]+self.board.segment/4))
    def PossibleMoves(self):
        self.possibleMoves = []
        self.moves = []
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
                        self.moves.append([x,y-up])
                        break
                    else:
                        self.moves.append([x,y-up])
                        break
                else:
                    self.possibleMoves.append([x,y-up])
                    self.moves.append([x,y-up])
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
                        self.moves.append([x,y+down])
                        break
                    else:
                        self.moves.append([x,y+down])
                        break
                else:
                    self.possibleMoves.append([x,y+down])
                    self.moves.append([x,y+down])
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
                        self.moves.append([x-left,y])
                        self.possibleMoves.append([x-left,y])
                        break
                    else:
                        self.moves.append([x-left,y])
                        break
                else:
                    self.moves.append([x-left,y])
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
                        self.moves.append([x+right,y])
                        break
                    else:
                        self.moves.append([x+right,y])
                        break
                else:
                    self.moves.append([x+right,y])
                    self.possibleMoves.append([x+right,y])
                right += 1
            else:
                break
class King:
    def __init__(self,x,y,side,board):
        self.x = x
        self.y = y
        self.worth = 10000
        self.board = board
        self.possibleMoves = []
        self.moves = []
        self.side = side
        self.FirstMove = True
        
    def draw(self,win):
        if self.side == "white":
            pos = self.board.GrabPixel([self.x,self.y])
            win.blit(pygame.transform.scale(KING_WHITE,(int(self.board.segment),int(self.board.segment))), (pos[0]-1,pos[1]-2))
        else:
            pos = self.board.GrabPixel([self.x,self.y])
            win.blit(pygame.transform.scale(KING_BLACK,(int(self.board.segment),int(self.board.segment))), (pos[0]-1,pos[1]-2))

    def drawPossibleMoves(self,win):
        for pos in self.possibleMoves:
            pos = self.board.GrabPixel(pos)
            win.blit(pygame.transform.scale(MOVE_IMAGE,(int(self.board.segment/2),int(self.board.segment/2))), (pos[0]+self.board.segment/4,pos[1]+self.board.segment/4))
    def PossibleMoves(self):
        self.possibleMoves = []
        self.moves = []
        board = self.board.board
        attackermoves = self.board.WhiteMoves
        if self.side == 'white':
            attackermoves = self.board.BlackMoves
        x = self.x
        y = self.y
        if not (y-1 < 0):
            if board[x][y-1] != None:# top
                if board[x][y-1].side != self.side:
                    self.possibleMoves.append([x,y-1])
                    self.moves.append([x,y-1])
                else:
                    self.moves.append([x,y-1])
            else:
                self.possibleMoves.append([x,y-1])
                self.moves.append([x,y-1])
        if not (x+1 >= self.board.BoardSize or y-1 < 0):
            if board[x+1][y-1] != None:#top right
                if board[x+1][y-1].side != self.side:
                    self.possibleMoves.append([x+1,y-1])
                    self.moves.append([x+1,y-1])
                else:
                    self.moves.append([x+1,y-1])
            else:
                self.possibleMoves.append([x+1,y-1])
                self.moves.append([x+1,y-1])

        if not (x-1 < 0 or y-1 < 0):
            if board[x-1][y-1] != None:#Top Left
                if board[x-1][y-1].side != self.side:
                    self.possibleMoves.append([x-1,y-1])
                    self.moves.append([x-1,y-1])
                    
                else:
                    self.moves.append([x-1,y-1])
            else:
                self.possibleMoves.append([x-1,y-1])
                self.moves.append([x-1,y-1])
        if not (y+1 >= self.board.BoardSize):
            if board[x][y+1] != None:# bottom
                if board[x][y+1].side != self.side:
                    self.possibleMoves.append([x,y+1])
                    self.moves.append([x,y+1])
                else:
                    self.moves.append([x,y+1])
            else:
                self.possibleMoves.append([x,y+1])
                self.moves.append([x,y+1])
        if not (x+1 >= self.board.BoardSize or y+1 >= self.board.BoardSize):
            if board[x+1][y+1] != None:#bottom Right
                if board[x+1][y+1].side != self.side:
                    self.possibleMoves.append([x+1,y+1])
                    self.moves.append([x+1,y+1])
                else:
                    self.moves.append([x+1,y+1])
            else:
                self.possibleMoves.append([x+1,y+1])
                self.moves.append([x+1,y+1])

        if not (x-1 < 0 or y+1 >= self.board.BoardSize):
            if board[x-1][y+1] != None:#bottom Left
                if board[x-1][y+1].side != self.side:
                    self.possibleMoves.append([x-1,y+1])
                    self.moves.append([x-1,y+1])
                else:
                    self.moves.append([x-1,y+1])
            else:
                self.possibleMoves.append([x-1,y+1])
                self.moves.append([x-1,y+1])

        if not (x-1 < 0):
            if board[x-1][y] != None:# Left
                if board[x-1][y].side != self.side:
                    self.possibleMoves.append([x-1,y])
                    self.moves.append([x-1,y])
                else:
                    self.moves.append([x-1,y])
            else:
                self.possibleMoves.append([x-1,y])
                self.moves.append([x-1,y])

        if not (x+1 >= self.board.BoardSize):
            if board[x+1][y] != None:# Right
                if board[x+1][y].side != self.side:
                    self.possibleMoves.append([x+1,y])
                    self.moves.append([x+1,y])
                else:
                    self.moves.append([x+1,y])
            else:
                self.possibleMoves.append([x+1,y])
                self.moves.append([x+1,y])
        if self.FirstMove:
            right = True
            left = True
            leftX = int((self.board.BoardSize/2)-1)
            rightX = int(self.board.BoardSize/2)
            for x in range(int(self.board.BoardSize/2)):
                if board[leftX][self.y] != None:
                    if isinstance(board[leftX][self.y],Rook) and left:
                        if board[leftX][self.y].FirstMove:
                            self.possibleMoves.append([self.x - 2,y,leftX,y,self.x-1,y])
                    else:
                        left = False
                if board[rightX][self.y] != None:
                    if rightX != self.x:
                        if isinstance(board[rightX][self.y],Rook) and right:
                            if board[rightX][self.y].FirstMove:
                                self.possibleMoves.append([self.x + 2,y,rightX,y,self.x+1,y])
                        else:
                            right = False
                leftX -= 1
                rightX += 1
class Bishop:
    def __init__(self,x,y,side,board):
        self.x = x
        self.y = y
        self.board = board
        self.worth = 3.5
        self.possibleMoves = []
        self.FirstMove = True
        self.moves = []
        self.side = side
    def draw(self,win):
        if self.side == "white":
            pos = self.board.GrabPixel([self.x,self.y])
            win.blit(pygame.transform.scale(BISHOP_WHITE,(int(self.board.segment),int(self.board.segment))), (pos[0]-1,pos[1]-2))
        else:
            pos = self.board.GrabPixel([self.x,self.y])
            win.blit(pygame.transform.scale(BISHOP_BLACK,(int(self.board.segment),int(self.board.segment))), (pos[0]-1,pos[1]-2))
        
    def drawPossibleMoves(self,win):
        for pos in self.possibleMoves:
            pos = self.board.GrabPixel(pos)
            win.blit(pygame.transform.scale(MOVE_IMAGE,(int(self.board.segment/2),int(self.board.segment/2))), (pos[0]+self.board.segment/4,pos[1]+self.board.segment/4))
    def PossibleMoves(self):
        self.possibleMoves = []
        self.moves = []
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
                        self.moves.append([x+right,y-up])
                        break
                    else:
                        self.moves.append([x+right,y-up])
                        break
                else:
                    self.moves.append([x+right,y-up])
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
                        self.moves.append([x+right,y+down])
                        break
                    else:
                        self.moves.append([x+right,y+down])
                        break
                else:
                    self.moves.append([x+right,y+down])
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
                        self.moves.append([x-left,y-up])
                        break
                    else:
                        self.moves.append([x-left,y-up])
                        break
                else:
                    self.possibleMoves.append([x-left,y-up])
                    self.moves.append([x-left,y-up])
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
                        self.moves.append([x-left,y+down])
                        break
                    else:
                        self.moves.append([x-left,y+down])
                        break
                else:
                    self.moves.append([x-left,y+down])
                    self.possibleMoves.append([x-left,y+down])
                left += 1
                down += 1
            else:
                break
class Knight:
    def __init__(self,x,y,side,board):
        self.x = x
        self.y = y
        self.worth = 3
        self.board = board
        self.possibleMoves = []
        self.moves = []
        self.FirstMove = True
        self.side = side
    def draw(self,win):
        if self.side == "white":
            pos = self.board.GrabPixel([self.x,self.y])
            win.blit(pygame.transform.scale(KNIGHT_WHITE,(int(self.board.segment),int(self.board.segment))), (pos[0]-1,pos[1]-2))
        else:
            pos = self.board.GrabPixel([self.x,self.y])
            win.blit(pygame.transform.scale(KNIGHT_BLACK,(int(self.board.segment),int(self.board.segment))), (pos[0]-1,pos[1]-2))
        
    def drawPossibleMoves(self,win):
        for pos in self.possibleMoves:
            pos = self.board.GrabPixel(pos)
            win.blit(pygame.transform.scale(MOVE_IMAGE,(int(self.board.segment/2),int(self.board.segment/2))), (pos[0]+self.board.segment/4,pos[1]+self.board.segment/4))
    def PossibleMoves(self):
        self.possibleMoves = []
        self.moves = []
        board = self.board.board
        x = self.x
        y = self.y
        if not (y-2 < 0):#UP
            if not (x+1 >= self.board.BoardSize): #UP RIGHT
                if board[x+1][y-2] != None:
                    if board[x+1][y-2].side != self.side:
                        self.possibleMoves.append([x+1,y-2])
                        self.moves.append([x+1,y-2])
                    else:
                        self.moves.append([x+1,y-2])
                else:
                    self.moves.append([x+1,y-2])
                    self.possibleMoves.append([x+1,y-2])
            if not (x-1 < 0): #UP LEFT
                if board[x-1][y-2] != None:
                    if board[x-1][y-2].side != self.side:
                        self.possibleMoves.append([x-1,y-2])
                        self.moves.append([x-1,y-2])
                    else:
                        self.moves.append([x-1,y-2])
                else:
                    self.possibleMoves.append([x-1,y-2])
                    self.moves.append([x-1,y-2])

        if not (y+2 >= self.board.BoardSize): #DOWN
            if not (x+1 >= self.board.BoardSize): #DOWN RIGHT
                if board[x+1][y+2] != None:
                    if board[x+1][y+2].side != self.side:
                        self.moves.append([x+1,y+2])
                        self.possibleMoves.append([x+1,y+2])
                    else:
                        self.moves.append([x+1,y+2])
                else:
                    self.moves.append([x+1,y+2])
                    self.possibleMoves.append([x+1,y+2])
            if not (x-1 < 0): #DOWN LEFT
                if board[x-1][y+2] != None:
                    if board[x-1][y+2].side != self.side:
                        self.possibleMoves.append([x-1,y+2])
                        self.moves.append([x-1,y+2])
                    else:
                        self.moves.append([x-1,y+2])
                else:
                    self.possibleMoves.append([x-1,y+2])
                    self.moves.append([x-1,y+2])

        if not (x+2 >= self.board.BoardSize): #RIGHT
            if not (y-1 < 0): #RIGHT UP
                if board[x+2][y-1] != None:
                    if board[x+2][y-1].side != self.side:
                        self.possibleMoves.append([x+2,y-1])
                        self.moves.append([x+2,y-1])
                    else:
                        self.moves.append([x+2,y-1])
                else:
                    self.possibleMoves.append([x+2,y-1])
                    self.moves.append([x+2,y-1])

            if not (y+1 >= self.board.BoardSize): #RIGHT DOWN
                if board[x+2][y+1] != None:
                    if board[x+2][y+1].side != self.side:
                        self.possibleMoves.append([x+2,y+1])
                        self.moves.append([x+2,y+1])
                    else:
                        self.moves.append([x+2,y+1])
                else:
                    self.possibleMoves.append([x+2,y+1])
                    self.moves.append([x+2,y+1])

        if not (x-2 < 0): #LEFT
            if not (y-1 < 0): #LEFT UP
                if board[x-2][y-1] != None:
                    if board[x-2][y-1].side != self.side:
                        self.possibleMoves.append([x-2,y-1])
                        self.moves.append([x-2,y-1])
                    else:
                        self.moves.append([x-2,y-1])
                else:
                    self.possibleMoves.append([x-2,y-1])
                    self.moves.append([x-2,y-1])
            if not (y+1 >= self.board.BoardSize): #LEFT DOWN
                if board[x-2][y+1] != None:
                    if board[x-2][y+1].side != self.side:
                        self.possibleMoves.append([x-2,y+1])
                        self.moves.append([x-2,y+1])
                    else:
                        self.moves.append([x-2,y+1])
                else:
                    self.possibleMoves.append([x-2,y+1])
                    self.moves.append([x-2,y+1])
class Queen:
    def __init__(self,x,y,side,board):
        self.x = x
        self.y = y
        self.worth = 12
        self.board = board
        self.possibleMoves = []
        self.FirstMove = True
        self.moves = []
        self.side = side
        
    def draw(self,win):
        if self.side == "white":
            pos = self.board.GrabPixel([self.x,self.y])
            win.blit(pygame.transform.scale(QUEEN_WHITE,(int(self.board.segment),int(self.board.segment))), (pos[0]-1,pos[1]-2))
        else:
            pos = self.board.GrabPixel([self.x,self.y])
            win.blit(pygame.transform.scale(QUEEN_BLACK,(int(self.board.segment),int(self.board.segment))), (pos[0]-1,pos[1]-2))
        
    def drawPossibleMoves(self,win):
        for pos in self.possibleMoves:
            pos = self.board.GrabPixel(pos)
            win.blit(pygame.transform.scale(MOVE_IMAGE,(int(self.board.segment/2),int(self.board.segment/2))), (pos[0]+self.board.segment/4,pos[1]+self.board.segment/4))
    def PossibleMoves(self):
        self.possibleMoves = []
        self.moves = []
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
                        self.moves.append([x,y-up])
                        break
                    else:
                        self.moves.append([x,y-up])
                        break
                else:
                    self.moves.append([x,y-up])
                    self.possibleMoves.append([x,y-up])
                up += 1
            else:
                break
        #UP RIGHT
        up = 1
        right = 1
        while True:
            if not (y-up < 0 or x+right >= self.board.BoardSize):
                CheckingPosition = board[x+right][y-up]
                if CheckingPosition != None:
                    if CheckingPosition.side != self.side:
                        self.possibleMoves.append([x+right,y-up])
                        self.moves.append([x+right,y-up])
                        break
                    else:
                        self.moves.append([x+right,y-up])
                        break
                else:
                    self.moves.append([x+right,y-up])
                    self.possibleMoves.append([x+right,y-up])
                up += 1
                right += 1
            else:
                break
        #RIGHT
        right = 1
        while True:
            if not (x+right >= self.board.BoardSize):
                CheckingPosition = board[x+right][y]
                if CheckingPosition != None:
                    if CheckingPosition.side != self.side:
                        self.possibleMoves.append([x+right,y])
                        self.moves.append([x+right,y])
                        break
                    else:
                        self.moves.append([x+right,y])
                        break
                else:
                    self.possibleMoves.append([x+right,y])
                    self.moves.append([x+right,y])
                right += 1
            else:
                break
        #DOWN RIGHT
        right = 1
        down = 1
        while True:
            if not (x+right >= self.board.BoardSize or y+down >= self.board.BoardSize):
                CheckingPosition = board[x+right][y+down]
                if CheckingPosition != None:
                    if CheckingPosition.side != self.side:
                        self.possibleMoves.append([x+right,y+down])
                        self.moves.append([x+right,y+down])
                        break
                    else:
                        self.moves.append([x+right,y+down])
                        break
                else:
                    self.moves.append([x+right,y+down])
                    self.possibleMoves.append([x+right,y+down])
                right += 1
                down += 1
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
                        self.moves.append([x,y+down])
                        break
                    else:
                        self.moves.append([x,y+down])
                        break
                else:
                    self.moves.append([x,y+down])
                    self.possibleMoves.append([x,y+down])
                down += 1
            else:
                break
        #DOWN LEFT
        down = 1
        left = 1
        while True:
            if not (y+down >= self.board.BoardSize or x-left < 0):
                CheckingPosition = board[x-left][y+down]
                if CheckingPosition != None:
                    if CheckingPosition.side != self.side:
                        self.possibleMoves.append([x-left,y+down])
                        self.moves.append([x-left,y+down])
                        break
                    else:
                        self.moves.append([x-left,y+down])
                        break
                else:
                    self.moves.append([x-left,y+down])
                    self.possibleMoves.append([x-left,y+down])
                down += 1
                left += 1
            else:
                break
        #LEFT
        left = 1
        while True:
            if not (x-left < 0):
                CheckingPosition = board[x-left][y]
                if CheckingPosition != None:
                    if CheckingPosition.side != self.side:
                        self.moves.append([x-left,y])
                        self.possibleMoves.append([x-left,y])
                        break
                    else:
                        self.moves.append([x-left,y])
                        break
                else:
                    self.moves.append([x-left,y])
                    self.possibleMoves.append([x-left,y])
                left += 1
            else:
                break
        #UP LEFT
        up = 1
        left = 1
        while True:
            if not (x-left < 0 or y-up < 0):
                CheckingPosition = board[x-left][y-up]
                if CheckingPosition != None:
                    if CheckingPosition.side != self.side:
                        self.possibleMoves.append([x-left,y-up])
                        self.moves.append([x-left,y-up])
                        break
                    else:
                        self.moves.append([x-left,y-up])
                        break
                else:
                    self.moves.append([x-left,y-up])
                    self.possibleMoves.append([x-left,y-up])
                up += 1
                left += 1
            else:
                break

