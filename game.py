import numpy as np
import pygame
import Pieces
import threading
import progressbar
import copy
from MiniMax import minimax
import random
from board import Board
WIN_SIZE = 900
def runMinMax(board,depth,maximizing,win):
    Mainoutput = []
    Maincords = []
    if maximizing:
        print("finding Move For black")
        board.FindPieces()
        board.FindPlayersPossibleMoves('white')
        board.FindPlayersPossibleMoves('black')
        #print(board.BlackPossibleMoves)
        for piece in board.BlackPossibleMoves:
            startingPos = [piece[0][0],piece[0][1]]
            output = []
            cords = []
            for move in piece[1]:
                newBoard = copy.deepcopy(board)
                newBoard.move(startingPos,move)
                #print(startingPos,move)
                o = minimax(newBoard,depth-1,-1000,1000,False,[startingPos,move])

                if o >= 10000:
                    output.append(-10000)
                else:
                    output.append(o)
                #print([startingPos,move],output[-1])
                cords.append([startingPos,move])
            Mainoutput.append(max(output))
            cord = cords[output.index(max(output))]
            #print(cord,max(output))
            Maincords.append(cord)
        c = list(zip(Mainoutput, Maincords))
        random.shuffle(c)
        Mainoutput, Maincords = zip(*c)
        cord = Maincords[Mainoutput.index(max(Mainoutput))]
    else:
        print("finding Move For White")
        board.FindPieces()
        board.FindPlayersPossibleMoves('white')
        board.FindPlayersPossibleMoves('black')
        for piece in board.WhitePossibleMoves:
            startingPos = [piece[0][0],piece[0][1]]
            output = []
            cords = []
            for move in piece[1]:
                newBoard = copy.deepcopy(board)
                newBoard.move(startingPos,move)
                #print(startingPos,move)
                o = minimax(newBoard,depth-1,-10000000,10000000,True,[startingPos,move])
                if o <= -10000:
                    output.append(10000)
                else:
                    output.append(o)
                #print([startingPos,move],output[-1])
                cords.append([startingPos,move])

            Mainoutput.append(min(output))
            cord = cords[output.index(min(output))]
            #print(cord,min(output))
            Maincords.append(cord)
        c = list(zip(Mainoutput, Maincords))
        random.shuffle(c)
        Mainoutput, Maincords = zip(*c)
        cord = Maincords[Mainoutput.index(min(Mainoutput))]

    print(cord)
    return cord

board = Board(WIN_SIZE,8)
win = pygame.display.set_mode((WIN_SIZE,WIN_SIZE))
clock = pygame.time.Clock()
currentSide = "white"
selected = False
selectedPosition = []
board.FindPieces()
mouseClickedRecent = False
counter = 0
board.FindPlayersPossibleMoves('white')
board.FindPlayersPossibleMoves('black')
run = True
"""x = threading.Thread(target=runMinMax, args=(board,4,False))
x.start()"""
start = False
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    if start:
        if currentSide == 'black':
            output = runMinMax(board,4, True,win)
            board.move(output[0],output[1])
            if currentSide == 'white':
                currentSide = 'black'
            else:
                currentSide = 'white'
            '''if pygame.mouse.get_pressed()[0]:
                if not selected:
                    if board.GrabPos(pygame.mouse.get_pos()) != selectedPosition:
                        selectedPosition = board.GrabPos(pygame.mouse.get_pos())
                        if board.board[selectedPosition[0]][selectedPosition[1]] != None:
                            if board.board[selectedPosition[0]][selectedPosition[1]].side == currentSide:
                                board.board[selectedPosition[0]][selectedPosition[1]].PossibleMoves()
                                print("selected ", selectedPosition)
                                selected = True
                            else:
                                selectedPosition = []
                        else:
                            selectedPosition = []
                else:
                    MousePos = board.GrabPos(pygame.mouse.get_pos())
                    if MousePos != selectedPosition:
                        if board.board[MousePos[0]][MousePos[1]] != None:
                            if board.board[MousePos[0]][MousePos[1]].side == currentSide:
                                selected = True
                                selectedPosition = board.GrabPos(pygame.mouse.get_pos())
                                print("selected ", selectedPosition)
                    if board.move_Check(selectedPosition,board.GrabPos(pygame.mouse.get_pos())):
                            new = board.GrabPos(pygame.mouse.get_pos())
                            #print("selected",new, selectedPosition)
                            board.move(selectedPosition,new)
                            if currentSide == 'white':
                                currentSide = 'black'
                            else:
                                currentSide = 'white'
                            selected = False
                            selectedPosition = []
                            board.FindPieces()
                            board.FindPlayersPossibleMoves('white')
                            board.FindPlayersPossibleMoves('black')'''
        else:
            output = runMinMax(board,4, False,win)
            board.move(output[0],output[1])
            if currentSide == 'white':
                currentSide = 'black'
            else:
                currentSide = 'white'

    output = board.CheckKings()
    if board.CheckKings() == "white" or board.CheckKings() == "black":
        print(output,"Wins by CheckMate")
        break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        start =True

    board.DrawBoard(win)
    board.drawPieces(win)
    board.DrawPossibleMoves(win,selectedPosition) 
    #board.DrawPlayersPossibleMoves(win,'white')
    pygame.display.update()
