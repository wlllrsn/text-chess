# A class that contains a chess board, with piece positions

from defaultBoardPositions import *

class Board:
    def __init__(self, starting_position = STARTING_POSITION):

        # The two-dimensional list that holds the positions of the pieces. By default it is the regular starting
        # locations of the pieces
        self.positions = starting_position

    def __str__(self):
        string = '+ - + - + - + - + - + - + - + - +\n'

        for row in self.positions:
            for position in row:
                string += '| {} '.format(position)
            string += '|\n'
            string += '+ - + - + - + - + - + - + - + - +\n'

        return string
