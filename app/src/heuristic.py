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


def score_position(board, piece):
    score = 0

    # Center preference (placeholder)
    center_col = [row[3] for row in board]
    score += center_col.count(piece) * 5

    # TODO: Add horizontal, vertical, diagonal scanning later
    # (This matches your progress level)

    return score
