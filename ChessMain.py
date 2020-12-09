# A sample text-based chess game created by William Larson

from Board import Board
from Move import Move
from defaultBoardPositions import *

board1 = Board(123)

# board1.boardFromFEN('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')

print(board1)

print("\n\n doing move 1. e4\n\n")

move1 = Move('e2', 'e4')

board1.applyMove(move1)
print(board1)