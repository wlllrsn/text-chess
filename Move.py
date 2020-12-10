'''
A class that handles piece movement. Can be passed to a board object via its applyMove(Move) method

Methods:
    isValid: Currently returns True

'''


class Move:
    def __init__(self, currentSquare, destinationSquare):
        self.currentSquare = currentSquare
        self.destinationSquare = destinationSquare

    def isValid(self):
        return True

    def __str__(self):
        string = 'Starting square: {}\nEnding square: {}\n'.format(self.currentSquare, self.destinationSquare)
        return string
