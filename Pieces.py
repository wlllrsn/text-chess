'''
General class that can store piece attributes. Will have subclasses for every other type of piece (Rook, Queen, etc.)

'''

class Piece:
    def __init__(self, row, col, white):
        self.row = row
        self.col = col
        self.white = white

    def squareOnBoard(self, square):
        if square[0] in range(0, 8) and square[1] in range(0, 8):
            return True
        else:
            return False

    def isValidMove(self, destinationSqure, position, attributeDict):
        pass


class Rook(Piece):
    def __init__(self, row, col, white):
        super().__init__(row, col, white)

    def isValidMove(self, destinationSquare, position, attributeDict):
        # TODO make correct, now it only looks at rows and columns and not other pieces
        if (self.row == destinationSquare[0]) is not (self.col == destinationSquare[1]):
            return True

    def __str__(self):
        if self.white:
            return 'R'
        else:
            return 'r'


class Knight(Piece):
    def __init__(self, row, col, white):
        super().__init__(row, col, white)

    def isValidMove(self, destinationSquare, position, attributeDict):
        # TODO make correct, now it only looks at rows and columns and not other pieces
        if (self.row == destinationSquare[0]) is not (self.col == destinationSquare[1]):
            return True

    def __str__(self):
        if self.white:
            return 'N'
        else:
            return 'n'


class Bishop(Piece):
    def __init__(self, row, col, white):
        super().__init__(row, col, white)

    def isValidMove(self, destinationSquare, position, attributeDict):
        # TODO make correct, now it only looks at rows and columns and not other pieces
        if (self.row == destinationSquare[0]) is not (self.col == destinationSquare[1]):
            return True

    def __str__(self):
        if self.white:
            return 'B'
        else:
            return 'b'


class Queen(Piece):
    def __init__(self, row, col, white):
        super().__init__(row, col, white)

    def isValidMove(self, destinationSquare, position, attributeDict):
        # TODO make correct, now it only looks at rows and columns and not other pieces
        if (self.row == destinationSquare[0]) is not (self.col == destinationSquare[1]):
            return True

    def __str__(self):
        if self.white:
            return 'Q'
        else:
            return 'q'


class King(Piece):
    def __init__(self, row, col, white):
        super().__init__(row, col, white)

    def isValidMove(self, destinationSquare, position, attributeDict):
        # TODO make correct, now it only looks at rows and columns and not other pieces
        if (self.row == destinationSquare[0]) is not (self.col == destinationSquare[1]):
            return True

    def __str__(self):
        if self.white:
            return 'K'
        else:
            return 'k'


class Pawn(Piece):
    def __init__(self, row, col, white):
        super().__init__(row, col, white)

    def isValidMove(self, destinationSquare, position, attributeDict):
        # TODO make correct, now it only looks at rows and columns and not other pieces
        if (self.row == destinationSquare[0]) is not (self.col == destinationSquare[1]):
            return True

    def __str__(self):
        if self.white:
            return 'P'
        else:
            return 'p'
