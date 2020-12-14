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

        # The number of moves the piece has made in a game
        self.__moves = 0

        # a list of destination squares that the piece can legally move to
        self.legal_moves = []

    def squareOnBoard(self, square):
        if square[0] in range(0, 8) and square[1] in range(0, 8):
            return True
        else:
            return False

    def isValidMove(self, board, destinationSquare):
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
                if not position[y1][x].is_empty():
                    return True

        return False

    # method to determine if there are any pieces between two squares diagonally
    def pieceBetweenBishop(self, position, x1, y1, x2, y2):
        diff_y = 1 if y1 < y2 else -1
        diff_x = 1 if x1 < x2 else -1

        y_count = diff_y
        for x in range(x1 + diff_x, x2, diff_x):
            if not position[y1 + y_count][x].is_empty():
                return True
            y_count += diff_y

        return False

    # increments the total moves by 1
    def increment_moves(self):
        """
        increases the number of moves the piece has made by 1
        """
        self.__moves += 1

    # decrements teh total moves by 1
    def decrement_moves(self):
        """
        decreases the number of moves the piece has made by 1
        """

        self.__moves -= 1

    # returns true if the piece has moved in the game
    def hasMoved(self):
        """
        Indicates if the piece has already moved in the game or not. Useful for castling and pawn movement.

        :return: boolean. True if the piece has moved, False if it hasn't
        """
        return bool(self.__moves)

    # updates the legal move list
    def update_legal_moves(self, board):
        """
        updates the legal_moves attribute of the class

        :param position: the position matrix of the current game
        :type position: list
        :param attributeDict: the dictionary of attributes for the current game
        :type attributeDict: dict
        """
        board_positions = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                           'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
                           'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
                           'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
                           'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
                           'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                           'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                           'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']

        # empty the list first. Probably not the most efficient but a simple solution
        self.legal_moves.clear()

        for square in board_positions:
            pos = self.algebraicToCoordinate(square)
            if self.isValidMove(board, board.positions[pos[0]][pos[1]]):
                self.legal_moves.append(square)

    # returns legal moves
    def get_legal_moves(self):
        return self.legal_moves

    # returns moves that result in check (i.e. squares that a piece can capture)
    def get_check_moves(self):
        return self.legal_moves

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
        string += str(8-row)

        return string


class Rook(Piece):
    def __init__(self, row, col, white):
        super().__init__(row, col, white)

    def isValidMove(self, board, destination):

        # # can't move if it isn't your turn
        # if attributeDict['whiteTurn'] != self.white:
        #     return False

        # you can't move onto the same square as your own piece
        if destination.get_piece() is not None and destination.get_piece().white == self.white:
            return False

        # can't move to the square you are currently on
        if destination.row == self.row and destination.col == self.col:
            return False

        if destination.row == self.row or destination.col == self.col:
            return not self.pieceBetweenRook(board.positions, self.col, self.row, destination.col, destination.row)

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

    def isValidMove(self, board, destination):

        # # can't move if it isn't your turn
        # if attributeDict['whiteTurn'] != self.white:
        #     return False

        # you can't move onto the same square as your own piece
        if destination.get_piece() is not None and destination.get_piece().white == self.white:
            return False

        # can't move to the square you are currently on
        if destination.row == self.row and destination.col == self.col:
            return False

        if abs(destination.row - self.row) == 2 and abs(destination.col - self.col) == 1:
            return True

        elif abs(destination.row - self.row) == 1 and abs(destination.col - self.col) == 2:
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

    def isValidMove(self, board, destination):

        # # can't move if it isn't your turn
        # if attributeDict['whiteTurn'] != self.white:
        #     return False

        # you can't move onto the same square as your own piece
        if destination.get_piece() is not None and destination.get_piece().white == self.white:
            return False

        # can't move to the square you are currently on
        if destination.row == self.row and destination.col == self.col:
            return False

        if destination.col - destination.row == self.col - self.row:
            return not self.pieceBetweenBishop(board.positions, self.col, self.row, destination.col, destination.row)

        elif destination.col + destination.row == self.col + self.row:
            return not self.pieceBetweenBishop(board.positions, self.col, self.row, destination.col, destination.row)

    def __str__(self):
        if self.white:
            return 'B'
        else:
            return 'b'


class Queen(Piece):
    def __init__(self, row, col, white):
        super().__init__(row, col, white)

    def isValidMove(self, board, destination):

        # # can't move if it isn't your turn
        # if attributeDict['whiteTurn'] != self.white:
        #     return False

        # you can't move onto the same square as your own piece
        if destination.get_piece() is not None and destination.get_piece().white == self.white:
            return False

        # can't move to the square you are currently on
        if destination.row == self.row and destination.col == self.col:
            return False

        # rook rule
        if destination.row == self.row or destination.col == self.col:
            return not self.pieceBetweenRook(board.positions, self.col, self.row, destination.col, destination.row)

        # bishop rules
        if destination.col - destination.row == self.col - self.row:
            return not self.pieceBetweenBishop(board.positions, self.col, self.row, destination.col, destination.row)

        elif destination.col + destination.row == self.col + self.row:
            return not self.pieceBetweenBishop(board.positions, self.col, self.row, destination.col, destination.row)

        else:
            return False

    def __str__(self):
        if self.white:
            return 'Q'
        else:
            return 'q'


class King(Piece):
    def __init__(self, row, col, white):
        super().__init__(row, col, white)

    def isValidMove(self, board, destination):

        # # can't move if it isn't your turn
        # if attributeDict['whiteTurn'] != self.white:
        #     return False

        # you can't move onto the same square as your own piece
        if destination.get_piece() is not None and destination.get_piece().white == self.white:
            return False

        # can't move to the square you are currently on
        if destination.row == self.row and destination.col == self.col:
            return False

        # can't move more than two spaces away
        if abs(destination.row - self.row) > 1 or abs(destination.col - self.col) > 1:
            return False

        # can't move onto a square that can be captured by an opposing piece
        if self.coordinateToAlgebraic(destination.row, destination.col) in board.get_check_moves(not self.white):
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

    def isValidMove(self, board, destination):

        # # can't move if it isn't your turn
        # if attributeDict['whiteTurn'] != self.white:
        #     return False

        # you can't move onto the same square as one of your other pieces
        if not destination.is_empty() and destination.get_piece().white == self.white:
            return False

        # can't move to the square you are currently on
        if destination.row == self.row and destination.col == self.col:
            return False

        if self.white:
            if self.row == 0:  # remove once pawn promotion is added
                return False
            # first move? can move two spaces
            if not self.hasMoved():
                if destination.row == self.row - 2 and destination.col == self.col:
                    if destination.get_piece() is None and board.positions[self.row - 1][self.col].is_empty():
                        return True

            # pawns must move to the next row every move
            if destination.row != self.row - 1:
                return False

            # move directly in forward
            elif destination.col == self.col and destination.is_empty():
                return True

            # capture a piece diagonally
            elif abs(destination.col - self.col) == 1 and not destination.is_empty():
                return True

            else:
                return False

        else:
            if self.row == 7:  # remove once pawn promotion is added
                return False
            if not self.hasMoved():
                if destination.row == self.row + 2 and destination.col == self.col:
                    if destination.is_empty() and board.positions[self.row + 1][self.col].is_empty():
                        return True

            if destination.row != self.row + 1:
                return False

            elif destination.col == self.col and destination.get_piece() is None:
                return True

            elif abs(destination.col - self.col) == 1 and not destination.is_empty():
                return True

            else:
                return False

    def get_check_moves(self):
        check_list = []

        if self.white:

            if self.row == 0:  # remove once pawn promotion is added
                return []
            if self.col < 7:
                check_list.append(self.coordinateToAlgebraic(self.row - 1, self.col + 1))
            if self.col > 0:
                check_list.append(self.coordinateToAlgebraic(self.row - 1, self.col - 1))

        else:
            if self.row == 7:  # remove once pawn promotion is added
                return []
            if self.col < 7:
                check_list.append(self.coordinateToAlgebraic(self.row + 1, self.col + 1))
            if self.col > 0:
                check_list.append(self.coordinateToAlgebraic(self.row + 1, self.col - 1))

        return check_list

    def __str__(self):
        if self.white:
            return 'P'
        else:
            return 'p'


