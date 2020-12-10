# A sample text-based chess game created by William Larson

from Board import Board
from Move import Move
from defaultBoardPositions import *

board1 = Board('3qk3/8/1n3r2/8/1Q3K2/1B3Q2/8/8 w - - 0 1')

print('\n PRINT "QUIT" TO QUIT THE GAME WHEN MOVING PIECES')

while True:

    print(board1)

    if board1.whiteTurn:
        print('\n-- WHITE TO MOVE --\n\n')
    else:
        print('\n-- BLACK TO MOVE --\n\n')

    startSquare = None
    while startSquare is None:
        temp = input("Select a piece to move: ")

        # quit game
        if temp == 'QUIT':
            startSquare = 'QUIT'
            break

        if board1.getPiece(temp):
            startSquare = temp
        else:
            print('Invalid piece location. Try again.\n')

    # quit game
    if startSquare == 'QUIT':
        break

    while True:
        temp = input("Select a destination for your {}: ".format(str(board1.getPiece(startSquare))))
        move = Move(startSquare, temp)
        if board1.applyMove(move):
            break
        else:
            print('Invalid location. Try again.\n')

    print('\n')
    print(board1)

    board1.whiteTurn = False

    print('\n RANDOM MOVE BY BLACK \n')
    random_move = board1.getRandomMove()
    print(random_move)
    board1.applyMove(random_move)

    board1.whiteTurn = True


