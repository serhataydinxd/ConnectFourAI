ROWS = 6
COLS = 7

def create_board():
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    for row in board:
        print("| " + " ".join(str(cell) for cell in row) + " |")
    print("  " + " ".join(str(i) for i in range(COLS)))

def is_valid_move(board, col):
    return board[0][col] == 0

def get_next_open_row(board, col):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == 0:
            return row
    return None

def drop_piece(board, row, col, piece):
    board[row][col] = piece
