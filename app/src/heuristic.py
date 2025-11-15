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

    # Placeholder scoring values (as in your progress)
    if window.count(piece) == 3 and window.count(0) == 1:
        score += 100
    if window.count(piece) == 2 and window.count(0) == 2:
        score += 10

    # Defensive scoring
    if window.count(opp) == 3 and window.count(0) == 1:
        score -= 80

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

    score += evaluate_window(board, piece)

    return score
