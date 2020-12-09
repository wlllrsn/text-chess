# A class that contains a chess board, with piece positions

from defaultBoardPositions import *

class Board:
    def __init__(self, starting_position=STARTING_POSITION, castling='KQkq', whiteTurn=True, enPassant='-', halfMove=0,
                 fullMove=1):

        # The two-dimensional list that holds the positions of the pieces. By default it is the regular starting
        # locations of the pieces
        self.positions = starting_position

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
    def boardFromFEN(self, FEN):
        FEN_list = FEN.split()

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

    def __str__(self):
        string = '+ - + - + - + - + - + - + - + - +\n'

        for row in self.positions:
            for position in row:
                string += '| {} '.format(position)
            string += '|\n'
            string += '+ - + - + - + - + - + - + - + - +\n'

        return string
