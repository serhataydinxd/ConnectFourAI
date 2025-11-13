from board import *
from game import winning_move
from minimax import minimax

def main():
    board = create_board()
    turn = 0

    while True:
        print_board(board)

        if turn == 0:
            print("Player 1 turn")
            col = int(input("Choose a column (0-6): "))
        else:
            print("AI choosing move...")
            col, _ = minimax(board, 2, -99999999, 99999999, True)
            print(f"AI chooses column {col}")

        if is_valid_move(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, turn+1)

            if winning_move(board, turn+1):
                print_board(board)
                print(f"Player {turn+1} wins!")
                break

            turn = 1 - turn

        else:
            print("Invalid move!")

if __name__ == "__main__":
    main()
