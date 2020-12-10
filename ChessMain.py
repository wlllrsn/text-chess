# A sample text-based chess game created by William Larson

from Board import Board
from Move import Move
from defaultBoardPositions import *

board1 = Board('8/8/1n3r2/8/1R1B1Q2/8/1p3n2/8 w - - 0 1')

# board1.boardFromFEN('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')

print(board1)

move1 = Move('f4', 'f1')
#move2 = Move('f6', 'd4')


board1.applyMove(move1)
#board1.applyMove(move2)

print(board1)

