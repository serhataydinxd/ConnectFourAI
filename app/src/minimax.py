import math
from board import is_valid_move, get_next_open_row, drop_piece
from game import winning_move
from heuristic import score_position

DEBUG = True  # set to False to turn off debugging text

def debug_print(msg):
    if DEBUG:
        print(msg)

def minimax(board, depth, alpha, beta, maximizingPlayer):
    indent = "   " * (3 - depth)  # visual indentation based on depth

    # --- Terminal / depth check ---
    if depth == 0:
        score = score_position(board, 1)
        debug_print(f"{indent}Depth 0 reached → Heuristic score = {score}")
        return None, score

    # --- Maximizing player (AI) ---
    if maximizingPlayer:
        max_score = -math.inf
        best_col = None

        debug_print(f"{indent}MAX player evaluating depth {depth}")

        for col in range(7):
            if is_valid_move(board, col):
                debug_print(f"{indent}→ MAX considers column {col}")

                temp_board = [row[:] for row in board]
                row = get_next_open_row(temp_board, col)
                drop_piece(temp_board, row, col, 1)

                _, score = minimax(temp_board, depth - 1, alpha, beta, False)

                debug_print(f"{indent}   Column {col} gives score {score}")

                if score > max_score:
                    max_score = score
                    best_col = col
                    debug_print(f"{indent}   NEW BEST for MAX: col {col} score {score}")

                alpha = max(alpha, score)
                if alpha >= beta:
                    debug_print(f"{indent}   PRUNING for MAX! alpha {alpha} >= beta {beta}")
                    break

        return best_col, max_score

    # --- Minimizing player (Opponent) ---
    else:
        min_score = math.inf
        best_col = None

        debug_print(f"{indent}MIN player evaluating depth {depth}")

        for col in range(7):
            if is_valid_move(board, col):
                debug_print(f"{indent}→ MIN considers column {col}")

                temp_board = [row[:] for row in board]
                row = get_next_open_row(temp_board, col)
                drop_piece(temp_board, row, col, 2)

                _, score = minimax(temp_board, depth - 1, alpha, beta, True)

                debug_print(f"{indent}   Column {col} gives score {score}")

                if score < min_score:
                    min_score = score
                    best_col = col
                    debug_print(f"{indent}   NEW BEST for MIN: col {col} score {score}")

                beta = min(beta, score)
                if beta <= alpha:
                    debug_print(f"{indent}   PRUNING for MIN! beta {beta} <= alpha {alpha}")
                    break

        return best_col, min_score
