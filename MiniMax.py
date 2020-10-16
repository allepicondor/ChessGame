import Pieces
import pygame
import numpy as np
from board import Board
import copy

def minimax(board, depth,alpha,beta, maximizingPlayer,moves):
    def evaluation(board):
        whitePieces = 0
        blackPieces = 0 
        blackCount = 0
        whiteCount = 0
        blackYaverage = 0
        WhiteYaverage = 0
        for x in range(board.BoardSize):
            for y in range(board.BoardSize):
                piece = board.board[x][y]
                if piece != None:
                    if piece.side == "white":
                        whitePieces += piece.worth
                        WhiteYaverage += abs(piece.y - board.BoardSize)
                        blackCount += 1
                    else:
                        blackPieces += piece.worth
                        blackYaverage += piece.y
                        whiteCount += 1
        blackYaverage = blackYaverage/blackCount
        WhiteYaverage = WhiteYaverage/whiteCount
        #print(blackPieces,whitePieces)
        return blackPieces - whitePieces
        
    board.FindPieces()
    if depth == 0 or board.WhitePiecesLeft == 0 or board.blackPiecesLeft == 0 or board.CheckKings() != None:
        return evaluation(board)
    if maximizingPlayer:
        maxEval = -100000
        board.FindPlayersPossibleMoves('white')
        board.FindPlayersPossibleMoves('black')
        for piece in board.BlackPossibleMoves:
            startingPos = piece[0]
            for move in piece[1]:
                newBoard = copy.deepcopy(board)
                newMoves = moves.copy()
                newMoves.append([startingPos,move])

                newBoard.move(startingPos,move)

                evaluation = minimax(newBoard,depth -1,alpha,beta,False,newMoves)
                maxEval = max(evaluation,maxEval)
                alpha = max(alpha,evaluation)
                if beta <= alpha:
                    return maxEval
        return maxEval
    else:
        minEval = 1000000
        move = []
        board.FindPlayersPossibleMoves('white')
        board.FindPlayersPossibleMoves('black')
        for piece in board.WhitePossibleMoves:
            startingPos = piece[0]
            for move in piece[1]:
                newBoard = copy.deepcopy(board)
                newMoves = moves.copy()
                newMoves.append([startingPos,move])
                
                newBoard.move(startingPos,move)

                evaluation = minimax(newBoard,depth -1,alpha,beta,True,moves)
                minEval = min(evaluation,minEval)
                beta = min(beta,evaluation)
                if beta <= alpha:
                    return minEval
        return minEval

            


