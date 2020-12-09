# A sample text-based chess game created by William Larson

from Board import Board
from defaultBoardPositions import *

board1 = Board()

board1.boardFromFEN('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')

print(board1)