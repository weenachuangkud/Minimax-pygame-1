from object import Button
from tictactoe import check_tie, check_winner
from tictactoe import PLAYER, AI
import math

LARGE_VALUE = 1e5  # large value used in minimax

def find_win_possibly(board : list[list[Button]], symbol : str) -> tuple[int, int] | None:
    ROWS = len(board)
    COLS = len(board[0])

    # Check rows
    for r in range(ROWS):
        empty_c = None
        count_symbol = 0
        count_empty = 0
        for c in range(COLS):
            if board[r][c].text == symbol:
                count_symbol += 1
            elif board[r][c].text == "":
                count_empty += 1
                empty_c = c
       # print(f"Checking row {r} for symbol '{symbol}': count_symbol={count_symbol}, count_empty={count_empty}")
        if count_symbol == COLS - 1 and count_empty == 1:
           # print(f"Winning/blocking position found at row {r}, col {empty_c} for symbol '{symbol}'")
            return (r, empty_c)


    # Check columns
    for c in range(COLS):
        empty_r = None
        count_symbol = 0
        count_empty = 0
        for r in range(ROWS):
            if board[r][c].text == symbol:
                count_symbol += 1
            elif board[r][c].text == "":
                count_empty += 1
                empty_r = r
       # print(f"Checking column {c} for symbol '{symbol}': count_symbol={count_symbol}, count_empty={count_empty}")
        if count_symbol == ROWS - 1 and count_empty == 1:
           # print(f"Winning/blocking position found at row {empty_r}, col {c} for symbol '{symbol}'")
            return (empty_r, c)


    # Diagonal top-left -> bottom-right
    empty_pos = None
    count_symbol = 0
    count_empty = 0
    for i in range(min(ROWS, COLS)):
        if board[i][i].text == symbol:
            count_symbol += 1
        elif board[i][i].text == "":
            count_empty += 1
            empty_pos = (i, i)
    #print(f"Checking diagonal TL-BR for symbol '{symbol}': count_symbol={count_symbol}, count_empty={count_empty}")
    if count_symbol == min(ROWS, COLS) - 1 and count_empty == 1:
       # print(f"Winning/blocking position found at diagonal TL-BR: {empty_pos} for symbol '{symbol}'")
        return empty_pos


    # Diagonal top-right -> bottom-left
    empty_pos = None
    count_symbol = 0
    count_empty = 0
    for i in range(min(ROWS, COLS)):
        r = i
        c = COLS - 1 - i
        if board[r][c].text == symbol:
            count_symbol += 1
        elif board[r][c].text == "":
            count_empty += 1
            empty_pos = (r, c)
   # print(f"Checking diagonal TR-BL for symbol '{symbol}': count_symbol={count_symbol}, count_empty={count_empty}")
    if count_symbol == min(ROWS, COLS) - 1 and count_empty == 1:
        #print(f"Winning/blocking position found at diagonal TR-BL: {empty_pos} for symbol '{symbol}'")
        return empty_pos

    return None

def minimax(board: list[list[Button]], depth: int, is_maximizing: bool) -> int:
    """
    Minimax implementation for a board of Buttons.
    Returns score: +1 (AI win), -1 (player win), 0 (draw).
    """
    winner = check_winner(board)
    # FUCK FUCK FUCK
    if winner == AI:
        return 1
    if winner == PLAYER:
        return -1
    if check_tie(board):
        return 0

    ROWS = len(board)
    COLS = len(board[0]) if ROWS > 0 else 0

    if is_maximizing:
        best_score = -LARGE_VALUE
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c].text == "":
                    board[r][c].text = AI
                    score = minimax(board, depth + 1, False)
                    board[r][c].text = ""
                    if score > best_score:
                        best_score = score
        return best_score
    else:
        best_score = LARGE_VALUE
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c].text == "":
                    board[r][c].text = PLAYER
                    score = minimax(board, depth + 1, True)
                    board[r][c].text = ""
                    if score < best_score:
                        best_score = score
        return best_score

def find_best_move(board: list[list[Button]]) -> tuple[int, int]:
    """
    Given the current board (list[list[Button]]), return best (row, col) move for AI.
    Returns (-1, -1) if no moves available.
    """
    best_score = -LARGE_VALUE
    best_move = (-1, -1)
    ROWS = len(board)
    COLS = len(board[0]) if ROWS > 0 else 0

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c].text == "":
                board[r][c].text = AI
                score = minimax(board, 0, False)
                board[r][c].text = ""
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
    return best_move
