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

from random import randint


class Board:
    def __init__(self, starting_position=STARTING_POSITION):

        # The two-dimensional list that holds the positions of the pieces. By default it is the regular starting
        # locations of the pieces
        self.positions = [[' ' for x in range(8)] for x in range(8)]

        # List of all the pieces on the board. First list is black pieces, second list is white pieces
        self.pieces = [[], []]

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

        self.update_pieces()
        self.update_moves()

    # used by boardFromFEN method when given an invalid FEN string
    def __giveAttributesDefaultValues(self):
        self.castling = 'KQkq'
        self.whiteTurn = True
        self.enPassantTarget = '-'
        self.halfMoveCounter = 0
        self.fullMoveCounter = 1

    # applies a move to the board
    def applyMove(self, move):
        """
        :param move: a Move object with the necessary attributes
        :type move: Move
        :return: True or False if the move was valid or not
        """

        if move is None:
            return True  # used as a placeholder - if a side has no legal moves, should be a stalemate. For now it passes

        self.update_moves()

        piece = self.getPiece(move.currentSquare)
        destination = self.algebraicToCoordinate(move.destinationSquare)
        if move.destinationSquare in piece.legal_moves and self.whiteTurn == piece.white:
            self.clearSquare(move.currentSquare)
            self.setSquare(move.destinationSquare, piece)
            piece.row = destination[0]
            piece.col = destination[1]
            piece.increment_moves()

            self.update_pieces()
            self.update_moves()
            return True
        return False

    # returns the type of piece that is at a certain location on the board, and None if there is nothing there
    def getPiece(self, location):
        coordinates = self.algebraicToCoordinate(location)
        if not coordinates:
            return None

        if self.positions[coordinates[0]][coordinates[1]] != ' ':
            return self.positions[coordinates[0]][coordinates[1]]
        else:
            return None

    # converts from a letter-number sequence (i.e. e4, h2, etc.) to a row-column tuple
    def algebraicToCoordinate(self, notation):
        """
        :param notation: the algebraic notation of a coordinate on a chess board (i.e. e5, b4)
        :type notation: str
        :return: a tuple with the format (row int, col int)
        """
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        try:
            return 8 - int(notation[1]), letters.index(notation[0])
        except ValueError:
            print("Error: Invalid algebraic notation provided.")
            return None

    def coordinateToAlgebraic(self, row, col):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        string = ''
        string += letters[col]
        string += str(8 - row)

        return string

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
                'fullMoveCounter': self.fullMoveCounter,
                'checkMoves': self.get_check_moves(not self.whiteTurn)}

        return dict

    # returns a Piece object from a given character and coordinates
    def pieceFromCharacter(self, piece, row, col):
        """
        :param piece: one-character string representing the piece to be created
        :type piece: str
        :param row: row of the piece to be created
        :type row: int
        :param col: column of the piece to be created
        :type col: int
        :return: a Piece object (or subclass) with necessary attributes
        """
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

    # returns a random move from every possible move
    def getRandomMove(self):
        self.update_pieces()
        self.update_moves()

        board_positions = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                           'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
                           'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
                           'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
                           'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
                           'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                           'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                           'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']

        move_list = []

        for piece in self.pieces[int(self.whiteTurn)]:
            for move in piece.legal_moves:
                move_list.append(Move(self.coordinateToAlgebraic(piece.row, piece.col), move))

        if len(move_list) == 0:
            return None

        return move_list[randint(0, len(move_list) - 1)]

    # updates the piece list
    def update_pieces(self):
        board_positions = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                           'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
                           'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
                           'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
                           'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
                           'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                           'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                           'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']

        self.pieces[0].clear()
        self.pieces[1].clear()

        for square in board_positions:
            current_piece = self.getPiece(square)
            if current_piece is not None:
                self.pieces[int(current_piece.white)].append(current_piece)

        # print(self.pieces)

    # updates the moves of every piece in the list
    def update_moves(self):
        attributes = self.__getAttributeDict()

        for piece in self.pieces[0]:
            piece.update_legal_moves(self.positions, attributes)

        for piece in self.pieces[1]:
            piece.update_legal_moves(self.positions, attributes)

        # for piece in self.pieces[0]:
        #     print(piece.legal_moves)
        # for piece in self.pieces[1]:
        #     print(piece.legal_moves)

    # returns a list of all legal moves of the given color
    def get_moves(self, color):
        """
        :param color: a bool or int of the desired color. 0 or False for black, >0 or True for white
        :type color: int
        :type color: bool
        :return: a list of legal moves for that color in algebraic notation (i.e. e4)
        """

        moves = []

        for piece in self.pieces[color]:
            for move in piece.get_legal_moves():
                moves.append(move)

        return moves

    # returns a list of all moves of a color that can check the opposing king (i.e. capture squares)
    def get_check_moves(self, color):
        """
        :param color: a bool or int of the desired color. 0 or False for black, >0 or True for white
        :type color: int
        :type color: bool
        :return: a list of legal moves for that color in algebraic notation (i.e. e4) that result in check of the
                opposing king
        """

        moves = []

        for piece in self.pieces[color]:
            for move in piece.get_check_moves():
                moves.append(move)

        return moves

    def __str__(self):
        string = '    a   b   c   d   e   f   g   h\n'
        string += '  + - + - + - + - + - + - + - + - +\n'

        row_val = 8
        for row in self.positions:
            string += '{} '.format(str(row_val))
            for position in row:
                string += '| {} '.format(str(position))
            string += '|\n'
            string += '  + - + - + - + - + - + - + - + - +\n'
            row_val -= 1

        return string

