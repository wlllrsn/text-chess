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
from Pieces import *
from Move import Move


class Board:
    def __init__(self, starting_position=STARTING_POSITION):

        # The two-dimensional list that holds the positions of the pieces. By default it is the regular starting
        # locations of the pieces
        self.positions = [[' ' for x in range(8)] for x in range(8)]

        # attribute that describes whether each side can castle
        self.castling = None

        # attribute that holds which turn it is. True is white's turn
        self.whiteTurn = None

        # the current square that can be captured via en passant
        self.enPassantTarget = None

        # half move counter - cycles between 0 and 1
        self.halfMoveCounter = None

        # full move counter - used for the 50 move rule
        self.fullMoveCounter = None

        self.__boardFromFEN(starting_position)

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
                self.positions[row][col] = self.pieceFromCharacter(char, row, col)
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

    # applies a move to the board
    def applyMove(self, move):
        piece = self.getPiece(move.currentSquare)
        if piece.isValidMove(self.algebraicToCoordinate(move.destinationSquare), self.positions, self.__getAttributeDict()):
            self.clearSquare(move.currentSquare)
            self.setSquare(move.destinationSquare, piece)

    # returns the type of piece that is at a certain location on the board, and None if there is nothing there
    def getPiece(self, location):
        coordinates = self.algebraicToCoordinate(location)

        #print(self.positions[coordinates[0]][coordinates[1]].col)

        if self.positions[coordinates[0]][coordinates[1]] != ' ':
            return self.positions[coordinates[0]][coordinates[1]]
        else:
            return None

    # converts from a letter-number sequence (i.e. e4, h2, etc.) to a row-column tuple
    def algebraicToCoordinate(self, notation):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        return 8 - int(notation[1]), letters.index(notation[0])

    # empties a square
    def clearSquare(self, coordinates):
        square = self.algebraicToCoordinate(coordinates)
        self.positions[square[0]][square[1]] = ' '

    # sets a square to a piece value
    def setSquare(self, coordinates, piece):
        square = self.algebraicToCoordinate(coordinates)
        self.positions[square[0]][square[1]] = piece

    # returns a dictionary of the board's attributes
    # for use by pieces and moves to determine if they are valid
    def __getAttributeDict(self):
        dict = {'whiteTurn': self.whiteTurn,
                'castling': self.castling,
                'enPassantTarget': self.enPassantTarget,
                'halfMoveCounter': self.halfMoveCounter,
                'fullMoveCounter': self.fullMoveCounter}

        return dict

    # returns a Piece object from a given character and coordinates
    def pieceFromCharacter(self, piece, row, col):
        pieceDict = {'r': Rook(row, col, False),
                     'n': Knight(row, col, False),
                     'b': Bishop(row, col, False),
                     'q': Queen(row, col, False),
                     'k': King(row, col, False),
                     'p': Pawn(row, col, False),
                     'R': Rook(row, col, True),
                     'N': Knight(row, col, True),
                     'B': Bishop(row, col, True),
                     'Q': Queen(row, col, True),
                     'K': King(row, col, True),
                     'P': Pawn(row, col, True)}
        return pieceDict[piece]

    def __str__(self):
        string = '+ - + - + - + - + - + - + - + - +\n'

        for row in self.positions:
            for position in row:
                string += '| {} '.format(str(position))
            string += '|\n'
            string += '+ - + - + - + - + - + - + - + - +\n'

        return string

