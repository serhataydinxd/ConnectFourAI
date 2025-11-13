def winning_move(board, piece):

    # Horizontal check
    for r in range(6):
        for c in range(4):
            if (board[r][c] == piece and board[r][c+1] == piece and
                board[r][c+2] == piece and board[r][c+3] == piece):
                return True

    # Vertical check
    for r in range(3):
        for c in range(7):
            if (board[r][c] == piece and board[r+1][c] == piece and
                board[r+2][c] == piece and board[r+3][c] == piece):
                return True

    # Positive diagonal
    for r in range(3):
        for c in range(4):
            if (board[r][c] == piece and board[r+1][c+1] == piece and
                board[r+2][c+2] == piece and board[r+3][c+3] == piece):
                return True

    # Negative diagonal
    for r in range(3, 6):
        for c in range(4):
            if (board[r][c] == piece and board[r-1][c+1] == piece and
                board[r-2][c+2] == piece and board[r-3][c+3] == piece):
                return True

    return False
