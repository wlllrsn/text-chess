"""
A player class.
Attributes include:
- if the player is controlled manually or by a computer
- what color the player controls in the game


"""

from Move import Move


class Player:
    _counter = 0

    def __init__(self, isWhite, manual=True, name=None):
        """
        :param bool isWhite: True if the player controls white pieces, False if black
        :param bool manual: True if the pieces are controlled manually, False if by the computer
        :param str name: Optional string for the player's name.
        """
        self.__isWhite = isWhite
        self.__isManual = manual

        # set the name of the player. By default it is PLAYER X
        Player._counter += 1
        if name is None:
            self.name = "PLAYER " + str(Player._counter)
        else:
            self.name = name

        self.color = "WHITE" if self.__isWhite else "BLACK"

    def isWhite(self):
        return self.__isWhite

    def isManual(self):
        return self.__isManual

    def get_move(self, board):
        """
        uses player input to get a move if the player is manual, otherwise uses a driver to get a move for the computer
        :return: the player's move
        """
        pass


class ManualPlayer(Player):
    def __init__(self, isWhite, name=None):
        super().__init__(isWhite, manual=True, name=name)

    def get_move(self, board):
        print("-- {} TO MOVE --".format(self.color))

        startSquare = None
        while startSquare is None:
            temp = input("Select a piece to move: ")

            # quit game
            if temp == 'QUIT':
                startSquare = 'QUIT'
                break

            if board.getPiece(temp) and board.getPiece(temp).white == board.whiteTurn:
                startSquare = temp
            else:
                print('Invalid piece location. Try again.\n')

        # quit game
        if startSquare == 'QUIT':
            return "QUIT"

        while True:
            temp = input("Select a destination for your {}: ".format(str(board.getPiece(startSquare))))
            move = Move(board, startSquare, temp)
            if board.applyMove(move):
                return move
            else:
                print('Invalid location. Try again.\n')


class ComputerPlayer(Player):
    def __init__(self, isWhite, name=None):
        super().__init__(isWhite, manual=False, name=name)

    def get_move(self, board):
        print('\n RANDOM MOVE BY {} \n'.format(self.color))

        random_move = board.getRandomMove()
        print(random_move)
        if board.applyMove(random_move):
            return random_move
