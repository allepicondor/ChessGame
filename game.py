import numpy as np
import pygame
import Pieces
from board import Board
WIN_SIZE = 600

board = Board(WIN_SIZE,8)
win = pygame.display.set_mode((WIN_SIZE,WIN_SIZE))
clock = pygame.time.Clock()
board.reset_Board()
currentSide = "white"
selected = False
selectedPosition = []
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    if pygame.mouse.get_pressed()[0]:
        if not selected:
            selectedPosition = board.GrabPos(pygame.mouse.get_pos())
            if board.board[selectedPosition[0]][selectedPosition[1]] != None:
                if board.board[selectedPosition[0]][selectedPosition[1]].side == currentSide:
                    print("selected ", selectedPosition)
                    selected = True
                else:
                    selectedPosition = []
            else:
                selectedPosition = []
        else:
            if board.move_Check(selectedPosition,board.GrabPos(pygame.mouse.get_pos())):
                new = board.GrabPos(pygame.mouse.get_pos())

                board.board[selectedPosition[0]][selectedPosition[1]].x = new[0]
                board.board[selectedPosition[0]][selectedPosition[1]].y = new[1]
                Old = board.board[selectedPosition[0]][selectedPosition[1]]

                board.board[selectedPosition[0]][selectedPosition[1]] = None
                board.board[new[0]][new[1]] = Old
                board.board[new[0]][new[1]].possibleMoves = []
                if isinstance(board.board[new[0]][new[1]], Pieces.Pawn):
                    if board.board[new[0]][new[1]].FirstMove:
                        board.board[new[0]][new[1]].FirstMove = False
                if currentSide == 'white':
                    currentSide = 'black'
                else:
                    currentSide = 'white'
                selected = False
                selectedPosition = []
    board.DrawBoard(win)
    board.drawPieces(win)
    board.DrawPossibleMoves(win,selectedPosition) 
    pygame.display.update()
