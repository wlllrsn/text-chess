'''
A class that handles piece movement. Can be passed to a board object via its applyMove(Move) method

Methods:
    isValid: Currently returns True

'''


class Move:
    def __init__(self, board, currentSquare, destinationSquare):
        self.currentSquare = currentSquare
        self.destinationSquare = destinationSquare

        self.pieceTaken = board.getPiece(destinationSquare)

    def is_capture_move(self):
        """
        tells if the move involves capturing an opposing piece
        :return : True if the move captures another piece, false otherwise
        """

        return self.pieceTaken is not None

    def __str__(self):
        string = 'Starting square: {}\nEnding square: {}\n'.format(self.currentSquare, self.destinationSquare)
        return string
