"""
A game class, which will hold a board, players, and store information about the turn.
Controls player input too.
"""

from Board import *
from Move import *
from Pieces import *
from defaultBoardPositions import *
from ChessPlayer import *
from time import sleep


class Game:
    def __init__(self, position=STARTING_POSITION, player1Manual=True, player2Manual=False):
        self.__board = Board(position)

        self.whitePlayer = ManualPlayer(isWhite=True) if player1Manual else ComputerPlayer(isWhite=True)

        self.blackPlayer = ManualPlayer(isWhite=False) if player2Manual else ComputerPlayer(isWhite=False)

        self.__moves = []

    def play(self):
        print('\n PRINT "QUIT" TO QUIT THE GAME WHEN MOVING PIECES')

        while True:

            print('\n')
            print(self.__board)

            whitemove = self.whitePlayer.get_move(self.__board)
            if whitemove == "QUIT":
                break
            else:
                self.__moves.append(whitemove)

            print('\n')
            print(self.__board)

            self.__board.whiteTurn = False

            sleep(3)

            blackmove = self.blackPlayer.get_move(self.__board)
            if blackmove == "QUIT":
                break
            else:
                self.__moves.append(blackmove)

            self.__board.whiteTurn = True


