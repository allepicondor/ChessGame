import chess
import chess.pgn
import chess.engine
import numpy as np
import pickle
import keyboard
pgn = open("TrainingData.pgn")
engine = chess.engine.SimpleEngine.popen_uci("stockfish.exe")
def stockfish_evaluation(board, time_limit = 0.01):
    result = engine.analyse(board, chess.engine.Limit(time=time_limit))
    return result['score']
def ConvertPiece(piece):
    if piece.symbol() == 'P':
        return 1
    if piece.symbol() == 'p':
        return 7
    if piece.symbol() == 'R':
        return 2
    if piece.symbol() == 'r':
        return 8
    if piece.symbol() == 'N':
        return 3
    if piece.symbol() == 'n':
        return 9
    if piece.symbol() == 'B':
        return 4
    if piece.symbol() == 'b':
        return 10
    if piece.symbol() == 'Q':
        return 5
    if piece.symbol() == 'q':
        return 11
    if piece.symbol() == 'K':
        return 6
    if piece.symbol() == 'k':
        return 12
    
    


def turnBoardIntoInputs(board):
    ArrayBoard = np.zeros((8,8))
    for x in range(8):
        for y in range(8):
            piece = board.piece_at(chess.square(x, y))
            try:
                ArrayBoard[x][y] = ConvertPiece(piece)
            except AttributeError:
                pass
    
    return ArrayBoard / 12
trainX = []
trainY = []
x = 0
try:
    while True:
        if keyboard.is_pressed("s"):
            break
        first_game = chess.pgn.read_game(pgn)
        if first_game == None:
            break
        board = first_game.board()
        for move in first_game.mainline_moves():
            board.push(move)
            score = stockfish_evaluation(board).white().score()
            try:
                if score > 0:
                    score = 2
                elif score < 0:
                    score = 0
                elif score == 0:
                    score = 1
                trainY.append(score)
                trainX.append(turnBoardIntoInputs(board.copy()))
            except TypeError:
                pass
        x+=1
        print(f"game {x}")
        print(f"Total Moves {len(trainX)}")
except Exception:
    pass
print("SAVING DATA")
Xfile = open('trainingData/trainX.p', 'ab') 
pickle.dump(trainX, Xfile) 
Xfile.close()
Yfile = open('trainingData/trainY.p', 'ab') 
pickle.dump(trainY, Yfile) 
print("DATA SAVED")
Yfile.close()
