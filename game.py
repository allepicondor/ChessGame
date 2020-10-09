import numpy as np
import pygame
import Pieces
from board import Board

board = Board(800)
win = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
board.reset_Board()
print(board.board)
selected = False
selectedPosition = []
while True:
    clock.tick()
    board.EveryFrame() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    if pygame.mouse.get_pressed()[0]:
        if not selected:
            selectedPosition = board.GrabPos(pygame.mouse.get_pos())
            if board.board[selectedPosition[0]][selectedPosition[1]] != None:
                print("selected ", selectedPosition)
                selected = True
            else:
                selectedPosition = []
        else:
            if board.checkIfPossibleMove(selectedPosition,board.GrabPos(pygame.mouse.get_pos())):
                new = board.GrabPos(pygame.mouse.get_pos())

                board.board[selectedPosition[0]][selectedPosition[1]].x = new[0]
                board.board[selectedPosition[0]][selectedPosition[1]].y = new[1]
                print(board.board[selectedPosition[0]][selectedPosition[1]].x,board.board[selectedPosition[0]][selectedPosition[1]].y)
                Old = board.board[selectedPosition[0]][selectedPosition[1]]

                board.board[selectedPosition[0]][selectedPosition[1]] = None
                board.board[new[0]][new[1]] = Old


                selected = False
                selectedPosition = []

            
            
        



    board.DrawBoard(win)
    board.drawPieces(win)
    pygame.display.update()
