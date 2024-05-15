import tkinter as tk
from tkinter import messagebox

# Constants
EMPTY = ' '
BLACK = 'B'
WHITE = 'W'

# Create a Tkinter window
window = tk.Tk()
window.title("Othello Game")

# Create a game board
board = [[EMPTY for _ in range(8)] for _ in range(8)]
board[3][3] = WHITE
board[3][4] = BLACK
board[4][3] = BLACK
board[4][4] = WHITE

# Current player (BLACK starts)
current_player = BLACK

# Function to handle button click event
def handle_click(row, col):
    if is_valid_move(row, col):
        make_move(row, col)
        update_gui()
        if is_game_over():
            show_winner(get_winner())
    else:
        messagebox.showinfo("Invalid Move", "This move is not valid.")

# Function to check if a move is valid
def is_valid_move(row, col):
    if board[row][col] != EMPTY:
        return False

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dir_row, dir_col in directions:
        r, c = row + dir_row, col + dir_col
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == get_opponent():
            r += dir_row
            c += dir_col
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == get_opponent():
                r += dir_row
                c += dir_col
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == current_player:
                return True
    return False

# Function to make a move
def make_move(row, col):
    board[row][col] = current_player

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dir_row, dir_col in directions:
        r, c = row + dir_row, col + dir_col
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == get_opponent():
            r += dir_row
            c += dir_col
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == get_opponent():
                r += dir_row
                c += dir_col
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == current_player:
                r -= dir_row
                c -= dir_col
                while board[r][c] == get_opponent():
                    board[r][c] = current_player
                    r -= dir_row
                    c -= dir_col

    switch_player()

# Function to switch the current player
def switch_player():
    global current_player
    if current_player == BLACK:
        current_player = WHITE
    else:
        current_player = BLACK

# Function to get the opponent's color
def get_opponent():
    if current_player == BLACK:
        return WHITE
    else:
        return BLACK

# Function to check if the game is over
def is_game_over():
    for row in range(8):
        for col in range(8):
            if board[row][col] == EMPTY and is_valid_move(row, col):
                return False
    return True

# Function to count the number of disks for each player
def count_disks():
    black_count = 0
    white_count = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] == BLACK:
                black_count += 1
            elif board[row][col] == WHITE:
                white_count += 1
    return black_count, white_count

# Function to get the winner of the game
def get_winner():
    black_count, white_count = count_disks()
    if black_count > white_count:
        return "Black"
    elif white_count > black_count:
        return "White"
    else:
        return "Tie"

# Function to update the GUI with the current board state
def update_gui():
    for row in range(8):
        for col in range(8):
            if board[row][col] == BLACK:
                buttons[row][col].config(text='B', bg='black')
            elif board[row][col] == WHITE:
                buttons[row][col].config(text='W', bg='white')
            else:
                buttons[row][col].config(text='', bg='green')

# Function to show a message box with the winner
def show_winner(winner):
    messagebox.showinfo("Game Over", "The winner is: " + winner)

# Create buttons for the game board
buttons = []
for row in range(8):
    button_row = []
    for col in range(8):
        button = tk.Button(window, width=4, height=2, command=lambda r=row, c=col: handle_click(r, c))
        button.grid(row=row, column=col, padx=2, pady=2)
        button_row.append(button)
    buttons.append(button_row)

# Update the GUI with the initial board state
update_gui()

# Start the Tkinter event loop
window.mainloop()
