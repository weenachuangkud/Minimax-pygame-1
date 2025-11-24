from random import choice
from config import *
from object import Button

teams = ["O", "X"]

PLAYER = None
AI = None

def init():
    global PLAYER, AI
    PLAYER = choice(teams)
    AI = "O" if PLAYER == "X" else "X"

def check_winner(board : list[list[Button]]):
    ROWS = len(board)
    if ROWS == 0:
        return False
    COLS = len(board[0])

    # Check rows
    for r in range(ROWS):
        first = board[r][0].text
        if first != "" and all(board[r][c].text == first for c in range(1, COLS)):
            return first

    # Check columns
    for c in range(COLS):
        first = board[0][c].text
        if first != "" and all(board[r][c].text == first for r in range(1, ROWS)):
            return first

    # Check main diagonal (top-left -> bottom-right)
    n = min(ROWS, COLS)
    top_left = board[0][0].text
    if top_left != "" and all(board[i][i].text == top_left for i in range(1, n)):
        return top_left

    # Check anti-diagonal (top-right -> bottom-left)
    top_right = board[0][COLS - 1].text
    if top_right != "" and all(board[i][COLS - 1 - i].text == top_right for i in range(1, n)):
        return top_right

    return None
            

def check_tie(board : list[list[Button]]) -> bool:
    ROWS = len(board)
    COLS = len(board[0]) if ROWS > 0 else 0
    return all([board[i][j].text != "" for i in range(ROWS) for j in range(COLS)])

#def is_board_filled(section) -> bool:
#    return section.text == ""

#def is_able_to_fill(board, row : int, col : int) -> bool:
#   return board[row][col] == ""

