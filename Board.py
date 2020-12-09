# A class that contains a chess board, with piece positions

class Board:
    def __init__(self, default=True, positions=None):

        # The two-dimensional list that holds the positions of the pieces
        self.positions = [[' ' for x in range(8)] for y in range(8)]

        # if no parameters are passed, put the pieces in their starting positions
        pass # will do later

    def __str__(self):
        string = '+ - + - + - + - + - + - + - + - +\n'

        for row in self.positions:
            for position in row:
                string += '| {} '.format(position)
            string += '|\n'
            string += '+ - + - + - + - + - + - + - + - +\n'

        return string
