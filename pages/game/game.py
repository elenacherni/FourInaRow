from flask import Blueprint, render_template, request
import numpy as np

# Game variables

ROW_COUNT = 6
COLUMN_COUNT = 7
game_over = False
turn = 1
board = np.zeros((ROW_COUNT, COLUMN_COUNT))

# Game Functions

def message():
    if game_over:
        # returns who is the winner
        return "Player "+str(turn)+" wins!"
    # returns who is the next player
    return "Now's the turn of player "+str(turn)


def empty_row_num(col_num):
    # returns the first empty row from bottom
    for row in range(ROW_COUNT-1, -1, -1):
        if board[row][col_num] == 0:
            return row
    return -1


def update_board(col_num):
    empty_row = empty_row_num(col_num)
    if empty_row >= 0:
        board[empty_row][col_num] = turn


def is_winner():
    # Check horizontal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == turn and board[r][c+1] == turn and board[r][c+2] == turn and board[r][c+3] == turn:
                return True

    # Check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == turn and board[r+1][c] == turn and board[r+2][c] == turn and board[r+3][c] == turn:
                return True

    # Check right diaganal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == turn and board[r+1][c+1] == turn and board[r+2][c+2] == turn and board[r+3][c+3] == turn:
                return True

    # Check left diaganal
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == turn and board[r-1][c+1] == turn and board[r-2][c+2] == turn and board[r-3][c+3] == turn:
                return True
    return False


# game blueprint definition
game = Blueprint('game', __name__, static_folder='static', static_url_path='/game', template_folder='templates')


# Routes
@game.route('/')
def reset_game():
    global game_over, turn, board
    game_over = False
    turn = 1
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return render_template('game.html', board=board, message=message(), turn=turn)


@game.route('/makeMove', methods=['POST'])
def make_a_move():
    global turn, game_over
    if request.method == 'POST':
        col_num = request.form['colNum']
    update_board(int(col_num))
    game_over = is_winner()
    if game_over:
        return render_template('game.html', board=board, message=message(), turn=turn)

    # update next player turn
    if turn == 1:
        turn = 2
    else:
        turn = 1
    return render_template('game.html', board=board, message=message(), turn=turn)
