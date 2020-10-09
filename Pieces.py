import pygame

class Pawn:
    def __init__(self,x,y,side,board):
        self.x = x
        self.y = y
        self.board = board
        self.possibleMoves = []
        self.side = side
        self.Image = pygame.image.load('PiecesImg/pawn.png')
        
        if side == 'white':
            self.Image = pygame.image.load('PiecesImg/pawn.png')
        else:
            self.color = [0,0,0]
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
        if self.side == "white":
            try:
                if board[x][y+1] == None:
                    self.possibleMoves.append([x,y+1])
                if board[x+1][y+1] != None:
                    if board[x+1][y+1].side == "black":
                        self.possibleMoves.append([x+1,y+1])
                if board[x-1][y+1] != None:
                    if board[x-1][y+1].side == "black":
                        self.possibleMoves.append([x-1,y+1])
            except IndexError:
                pass
        else:
            try:
                if board[x][y-1] == None:
                    self.possibleMoves.append([x,y-1])
                if board[x+1][y-1] != None:
                    if board[x+1][y-1].side == "white":
                        self.possibleMoves.append([x+1,y-1])
                if board[x-1][y-1] != None:
                    if board[x-1][y-1].side == "white":
                        self.possibleMoves.append([x-1,y-1])
            except IndexError:
                pass
class Rook:
    def __init__(self,x,y,side,board):
        self.x = x
        self.y = y
        self.board = board
        self.possibleMoves = []
        self.side = side
        if side == 'white':
            self.color = [150,150,150]
        else:
            self.color = [0,0,0]
    def draw(self,win):
        pos = self.board.GrabPixel([self.x,self.y])
        pos[0] += int(self.board.segment/2)
        pos[1] += int(self.board.segment/2)
        pygame.draw.circle(win,self.color, pos, int(self.board.segment/2)-10)
        
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
            CheckingPosition = board[x][y-up]
            if CheckingPosition != None:
                if CheckingPosition.side != self.side:
                    self.possibleMoves.append([x,y-up])
                    break
                else:
                    self.possibleMoves.append([x,y-(up-1)])
                    break
            else:
                self.possibleMoves.append([x,y-up])
            up += 1




