"""
A class that contains a chess board, with piece positions
The class can be initialized in multiple ways:
Default: The board is given the typical chess starting position and all attributes are given accordingly
Manual: Using the parameters in the constructor, each attribute can be controlled individually when the class is 
        instantiated. This requires an 8x8 list for the board position and correct values for the other attributes.
        Probably the most difficult method. Might phase out in the future.
Automatic: Pass the class a valid FEN string when created and all values will be filled out automatically based on
           string.
"""

from defaultBoardPositions import *


class Board:
    def __init__(self, starting_position=STARTING_POSITION, castling='KQkq', whiteTurn=True, enPassant='-', halfMove=0,
                 fullMove=1):

        # The two-dimensional list that holds the positions of the pieces. By default it is the regular starting
        # locations of the pieces
        if type(starting_position) == list:
            self.positions = starting_position
        elif type(starting_position) == str:
            self.positions = EMPTY_POSITION
            self.__boardFromFEN(starting_position)
        else:
            print('Invalid board position given. Board is given the default starting position.\n')
            self.positions = STARTING_POSITION
            return

        # attribute that describes whether each side can castle
        self.castling = castling

        # attribute that holds which turn it is. True is white's turn
        self.whiteTurn = whiteTurn

        # the current square that can be captured via en passant
        self.enPassantTarget = enPassant

        # half move counter - cycles between 0 and 1
        self.halfMoveCounter = halfMove

        # full move counter - used for the 50 move rule
        self.fullMoveCounter = fullMove

    # method that sets all attributes of the board from a given FEN string
    def __boardFromFEN(self, FEN):
        FEN_list = FEN.split()
        if len(FEN_list) != 6:
            print('Invalid FEN string given. Board is given the default starting position.\n')
            self.positions = STARTING_POSITION
            self.__giveAttributesDefaultValues()

        # set piece positions
        row = 0
        col = 0
        for char in FEN_list[0]:
            if char.isalpha():
                self.positions[row][col] = char
                col += 1

            elif char == '/':
                row += 1
                col = 0

            elif char.isnumeric():
                for x in range(int(char)):
                    self.positions[row][col] = ' '
                    col += 1

        # set move
        self.whiteTurn = True if FEN_list[1] == 'w' else False

        # set castling
        self.castling = FEN_list[2]

        # set en passant
        self.enPassantTarget = FEN_list[3]

        # set half and full move counters
        self.halfMoveCounter = int(FEN_list[4])
        self.fullMoveCounter = int(FEN_list[5])

    # used by boardFromFEN method when given an invalid FEN string
    def __giveAttributesDefaultValues(self):
        self.castling = 'KQkq'
        self.whiteTurn = True
        self.enPassantTarget = '-'
        self.halfMoveCounter = 0
        self.fullMoveCounter = 1

    def __str__(self):
        string = '+ - + - + - + - + - + - + - + - +\n'

        for row in self.positions:
            for position in row:
                string += '| {} '.format(position)
            string += '|\n'
            string += '+ - + - + - + - + - + - + - + - +\n'

        return string
