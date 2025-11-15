DEBUG = True  # set to False to turn off debugging text

POSITION_WEIGHTS = [
    [3, 4, 5, 7, 5, 4, 3],
    [4, 6, 8,10, 8, 6, 4],
    [5, 8,11,13,11, 8, 5],
    [5, 8,11,13,11, 8, 5],
    [4, 6, 8,10, 8, 6, 4],
    [3, 4, 5, 7, 5, 4, 3]
]


def evaluate_window(window, piece):
    score = 0
    opp = 2 if piece == 1 else 1

    # Offensive (The AI's opportunities)
    if window.count(piece) == 4:
        score += 100000  # Winning move
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 500  # Strong threat (4-in-a-row on next turn)
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 20  # Minor threat

    # Defensive (Blocking the opponent)
    if window.count(opp) == 3 and window.count(0) == 1:
        # Crucial defense: Block opponent's immediate win.
        # Needs to be a high score, but less than an AI win.
        score -= 400

        # You generally don't need to score 4 opponent pieces
    # as the terminal check handles that loss.

    return score

def position_weight(board, piece):
    score = 0
    for r in range(6):
        for c in range(7):
            cell = board[r][c]
            if cell == piece:
                if DEBUG:
                    print(f"AI piece at ({r},{c}) adds {POSITION_WEIGHTS[r][c]}")
                score += POSITION_WEIGHTS[r][c]
            elif cell != 0:
                if DEBUG:
                    print(f"OPP piece at ({r},{c}) subtracts {POSITION_WEIGHTS[r][c]}")
                score -= POSITION_WEIGHTS[r][c]
    return score




def score_position(board, piece):
    score = 0

    score += position_weight(board, piece)

    # Horizontal scoring
    for r in range(6):
        row_array = board[r]
        for c in range(7 - 3):  # Iterate over possible starting columns
            window = row_array[c:c + 4]
            score += evaluate_window(window, piece)

    # Vertical scoring
    for c in range(7):
        col_array = [board[r][c] for r in range(6)]
        for r in range(6 - 3):
            window = col_array[r:r + 4]
            score += evaluate_window(window, piece)

    # Positive slope diagonal scoring
    for r in range(6 - 3):
        for c in range(7 - 3):
            window = [board[r + i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Negative slope diagonal scoring
    for r in range(6 - 3):
        for c in range(3, 7):  # Start at column 3 and go left
            window = [board[r + i][c - i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score
