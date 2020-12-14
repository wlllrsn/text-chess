"""
A class for the squares that will populate a chess board
"""

class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col

        self.__piece = piece

    def get_piece(self):
        return self.__piece

    def set_piece(self, piece):
        self.__piece = piece

    def is_empty(self):
        return True if self.__piece is None else False