import chess
import chess.pgn
import chess.engine
import numpy as np
import random
import tensorflow as tf
from tensorflow.keras import datasets, layers, models,datasets
import matplotlib.pyplot as plt
from keras.preprocessing import image
import cv2
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import scipy.io
import pickle
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
Xfile = open('trainingData/trainX.p', 'rb')  
trainX = pickle.load(Xfile)
Yfile = open('trainingData/trainY.p', 'rb')  
trainY = pickle.load(Yfile)
Yfile.close()
Xfile.close()
zipped = list(zip(trainX,trainY))
random.shuffle(zipped)
trainX,trainY = zip(*zipped)
trainX = np.array(trainX)
trainY = np.array(trainY)
trainX = trainX.reshape(len(trainX), 8, 8, 1)
index = int(len(trainX*.80))
print(len(trainX),len(trainY))
trainX, testX = trainX[:index,:], trainX[index:,:]
trainY, testY = trainY[:index], trainY[index:]
print(len(trainX),len(testX))
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(8, 8,1)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))
model.summary()

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
print(np.shape(np.asarray(trainX)))
#train.reshape(1,8,8)
model.fit(trainX,trainY, epochs=100,batch_size=100)
'''test_loss, test_acc = model.evaluate(testX,  testY, verbose=2)
print(test_acc)'''


print("TESTDATA3")
pgn = open("TestData3.pgn")
TestGame = chess.pgn.read_game(pgn)
board = TestGame.board()
testX = []
testY = []
for move in TestGame.mainline_moves():
    board.push(move)
testX.append(turnBoardIntoInputs(board.copy()))
score = stockfish_evaluation(board).white().score()
if score > 0:
    score = 2
elif score < 0:
    score = 0
elif score == 0:
    score = 1
testY.append(score)
testX = np.array(testX)
testX = testX.reshape(len(testX), 8, 8, 1)

print(board)
print(testY[0])
print(np.argmax(model.predict(testX)))