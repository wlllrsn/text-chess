"""
A game class, which will hold a board, players, and store information about the turn.
Controls player input too.
"""

from Board import *
from Move import *
from Pieces import *
from defaultBoardPositions import *
from time import sleep


class Game:
    def __init__(self, position=STARTING_POSITION, ):
        self.__board = Board(position)

        self.whitePlayer = None

        self.blackPlayer = None

    def play(self):
        print('\n PRINT "QUIT" TO QUIT THE GAME WHEN MOVING PIECES')

        while True:

            print(self.__board)

            if self.__board.whiteTurn:
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

                if self.__board.getPiece(temp) and self.__board.getPiece(temp).white == self.__board.whiteTurn:
                    startSquare = temp
                else:
                    print('Invalid piece location. Try again.\n')

            # quit game
            if startSquare == 'QUIT':
                break

            while True:
                temp = input("Select a destination for your {}: ".format(str(self.__board.getPiece(startSquare))))
                move = Move(startSquare, temp)
                if self.__board.applyMove(move):
                    break
                else:
                    print('Invalid location. Try again.\n')

            print('\n')
            print(self.__board)

            self.__board.whiteTurn = False

            print('\n RANDOM MOVE BY BLACK \n')

            sleep(3)

            random_move = self.__board.getRandomMove()
            print(random_move)
            self.__board.applyMove(random_move)

            self.__board.whiteTurn = True


