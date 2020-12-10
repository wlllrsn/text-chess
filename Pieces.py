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
        destination = position[destinationSquare[0]][destinationSquare[1]]

        # can't move if it isn't your turn
        if attributeDict['whiteTurn'] != self.white:
            return False

        # you can't move onto the same square as your own piece
        if destination != ' ' and destination.white == self.white:
            return False

        # can't move to the square you are currently on
        if destinationSquare[0] == self.row and destinationSquare[1] == self.col:
            return False

        if destinationSquare[0] == self.row or destinationSquare[1] == self.col:
            return not self.pieceBetweenRook(position, self.col, self.row, destinationSquare[1], destinationSquare[0])

        else:
            return False

    # returns true or false depending on if there is a piece between two squares, vertically or horizontally
    def pieceBetweenRook(self, position, x1, y1, x2, y2):
        diff_y = 1 if y1 < y2 else -1
        diff_x = 1 if x1 < x2 else -1

        # check vertical
        if x1 == x2:
            for y in range(y1 + diff_y, y2, diff_y):
                if position[y][x1] != ' ':
                    return True

        # check horizontal
        elif y1 == y2:
            for x in range(x1 + diff_x, x2, diff_x):
                if position[y1][x] != ' ':
                    return True

        return False

    def __str__(self):
        if self.white:
            return 'R'
        else:
            return 'r'


class Knight(Piece):
    def __init__(self, row, col, white):
        super().__init__(row, col, white)

    def isValidMove(self, destinationSquare, position, attributeDict):
        destination = position[destinationSquare[0]][destinationSquare[1]]

        # can't move if it isn't your turn
        if attributeDict['whiteTurn'] != self.white:
            return False

        # you can't move onto the same square as your own piece
        if destination != ' ' and destination.white == self.white:
            return False

        # can't move to the square you are currently on
        if destinationSquare[0] == self.row and destinationSquare[1] == self.col:
            return False

        if abs(destinationSquare[0] - self.row) == 2 and abs(destinationSquare[1] - self.col) == 1:
            return True

        elif abs(destinationSquare[0] - self.row) == 1 and abs(destinationSquare[1] - self.col) == 2:
            return True

        else:
            return False

    def __str__(self):
        if self.white:
            return 'N'
        else:
            return 'n'


class Bishop(Piece):
    def __init__(self, row, col, white):
        super().__init__(row, col, white)

    def isValidMove(self, destinationSquare, position, attributeDict):
        destination = position[destinationSquare[0]][destinationSquare[1]]

        # can't move if it isn't your turn
        if attributeDict['whiteTurn'] != self.white:
            return False

        # you can't move onto the same square as your own piece
        if destination != ' ' and destination.white == self.white:
            return False

        # can't move to the square you are currently on
        if destinationSquare[0] == self.row and destinationSquare[1] == self.col:
            return False

        if destinationSquare[1] - destinationSquare[0] == self.col - self.row:
            return not self.pieceBetweenBishop(position, self.col, self.row, destinationSquare[1], destinationSquare[0])

        elif destinationSquare[1] + destinationSquare[0] == self.col + self.row:
            return not self.pieceBetweenBishop(position, self.col, self.row, destinationSquare[1], destinationSquare[0])

    # method to determine if there are any pieces between two squares diagonally
    def pieceBetweenBishop(self, position, x1, y1, x2, y2):
        diff_y = 1 if y1 < y2 else -1
        diff_x = 1 if x1 < x2 else -1

        y_count = 1
        for x in range(x1 + diff_x, x2, diff_x):

            print("X: {}, Y: {}".format(x, y1 + y_count*diff_y))
            if position[y1 + y_count*diff_y][x] != ' ':
                return True
            y_count += 1

        return False

    def __str__(self):
        if self.white:
            return 'B'
        else:
            return 'b'


class Queen(Piece):
    def __init__(self, row, col, white):
        super().__init__(row, col, white)

    def isValidMove(self, destinationSquare, position, attributeDict):

        destination = position[destinationSquare[0]][destinationSquare[1]]

        # can't move if it isn't your turn
        if attributeDict['whiteTurn'] != self.white:
            return False

        # you can't move onto the same square as your own piece
        if destination != ' ' and destination.white == self.white:
            return False

        # can't move to the square you are currently on
        if destinationSquare[0] == self.row and destinationSquare[1] == self.col:
            return False

        # rook rule
        if destinationSquare[0] == self.row or destinationSquare[1] == self.col:
            return not self.pieceBetweenRook(position, self.col, destinationSquare[1], self.row, destinationSquare[0])

        if destinationSquare[1] - destinationSquare[0] == self.col - self.row:
            return not self.pieceBetweenBishop(position, self.col, self.row, destinationSquare[1], destinationSquare[0])

        elif destinationSquare[1] + destinationSquare[0] == self.col + self.row:
            return not self.pieceBetweenBishop(position, self.col, self.row, destinationSquare[1], destinationSquare[0])

        else:
            return False

    # returns true or false depending on if there is a piece between two squares, vertically or horizontally
    def pieceBetweenRook(self, position, x1, y1, x2, y2):
        diff_y = 1 if y1 < y2 else -1
        diff_x = 1 if x1 < x2 else -1

        # check vertical
        if x1 == x2:
            for y in range(y1 + diff_y, y2, diff_y):
                if position[y][x1] != ' ':
                    return True

        # check horizontal
        elif y1 == y2:
            for x in range(x1 + diff_x, x2, diff_x):
                if position[y1][x] != ' ':
                    return True

        return False

    # method to determine if there are any pieces between two squares diagonally
    def pieceBetweenBishop(self, position, x1, y1, x2, y2):
        diff_y = 1 if y1 < y2 else -1
        diff_x = 1 if x1 < x2 else -1

        y_count = 1
        for x in range(x1 + diff_x, x2, diff_x):

            print("X: {}, Y: {}".format(x, y1 + y_count * diff_y))
            if position[y1 + y_count * diff_y][x] != ' ':
                return True
            y_count += 1

        return False

    def __str__(self):
        if self.white:
            return 'Q'
        else:
            return 'q'


class King(Piece):
    def __init__(self, row, col, white):
        super().__init__(row, col, white)

    def isValidMove(self, destinationSquare, position, attributeDict):
        destination = position[destinationSquare[0]][destinationSquare[1]]

        # can't move if it isn't your turn
        if attributeDict['whiteTurn'] != self.white:
            return False

        # you can't move onto the same square as your own piece
        if destination != ' ' and destination.white == self.white:
            return False

        # can't move to the square you are currently on
        if destinationSquare[0] == self.row and destinationSquare[1] == self.col:
            return False

        # can't move more than two spaces away
        if abs(destinationSquare[0] - self.row) > 1 or abs(destinationSquare[1] - self.col) > 1:
            return False

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
        destination = position[destinationSquare[0]][destinationSquare[1]]

        # can't move if it isn't your turn
        if attributeDict['whiteTurn'] != self.white:
            return False

        # you can't move onto the same square as one of your other pieces
        if destination != ' ' and destination.white == self.white:
            return False

        # can't move to the square you are currently on
        if destinationSquare[0] == self.row and destinationSquare[1] == self.col:
            return False

        if self.white:
            # pawns must move to the next row every move
            if destinationSquare[0] != self.row - 1:
                return False

            # move directly in forward
            elif destinationSquare[1] == self.col and destination == ' ':
                return True

            # capture a piece diagonally
            elif abs(destinationSquare[1] - self.col) == 1 and destination != ' ':
                return True

            else:
                return False

        else:
            if destinationSquare[0] != self.row + 1:
                return False

            elif destinationSquare[1] == self.col and destination == ' ':
                return True

            elif abs(destinationSquare[1] - self.col) == 1 and destination != ' ':
                return True

            else:
                return False




    def __str__(self):
        if self.white:
            return 'P'
        else:
            return 'p'
