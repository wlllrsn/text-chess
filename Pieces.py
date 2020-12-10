'''
General class that can store piece attributes. Will have subclasses for every other type of piece (Rook, Queen, etc.)

'''


class Piece:
    def __init__(self, row, col, white):
        """
        :param row: represents the row of the piece (0-7)
        :type row: int
        :param col: represents the column of the piece (0-7)
        :type col: int
        :param white: True if the piece is white, False if the piece is black
        :type white: bool
        """
        self.row = row
        self.col = col
        self.white = white

        self.__moves = 0

    def squareOnBoard(self, square):
        if square[0] in range(0, 8) and square[1] in range(0, 8):
            return True
        else:
            return False

    def isValidMove(self, destinationSquare, position, attributeDict):
        pass

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

        y_count = diff_y
        for x in range(x1 + diff_x, x2, diff_x):
            if position[y1 + y_count][x] != ' ':
                return True
            y_count += diff_y

        return False

    def increment_moves(self):
        """
        increases the number of moves the piece has made by 1
        """
        self.__moves += 1

    def hasMoved(self):
        """
        Indicates if the piece has already moved in the game or not. Useful for castling and pawn movement.

        :return: boolean. True if the piece has moved, False if it hasn't
        """
        return bool(self.__moves)


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
            return not self.pieceBetweenRook(position, self.col, self.row, destinationSquare[1], destinationSquare[0])

        # bishop rules
        if destinationSquare[1] - destinationSquare[0] == self.col - self.row:
            return not self.pieceBetweenBishop(position, self.col, self.row, destinationSquare[1], destinationSquare[0])

        elif destinationSquare[1] + destinationSquare[0] == self.col + self.row:
            return not self.pieceBetweenBishop(position, self.col, self.row, destinationSquare[1], destinationSquare[0])

        else:
            return False


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
            # first move? can move two spaces
            if self.row == 6:
                if destinationSquare[0] == 4 and destinationSquare[1] == self.col:
                    if destination == ' ' and position[self.row - 1][self.col]:
                        return True

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
            if self.row == 1:
                if destinationSquare[0] == 3 and destinationSquare[1] == self.col:
                    if destination == ' ' and position[self.row + 1][self.col]:
                        return True

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


