import random
from IPython.display import clear_output

def display_board(board):
    print('\n'*100)
    print(" {} * {} * {}".format(board[1],board[2],board[3]))
    print("***********")
    print(" {} * {} * {}".format(board[4],board[5],board[6]))
    print("***********")
    print(" {} * {} * {}".format(board[7],board[8],board[9]))

def player_input():
    choice = ""
    while choice != "X" and choice != "0":
        choice = input('Chose your marked[x or 0]:')
        choice = choice.upper()
    return choice

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    if board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    if board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    if board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    if board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    if board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    if board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    if board[3] == mark and board[2] == mark and board[7] == mark:
        return True
    return False

def choose_first():
    turn = random.randint(1,2)
    return turn

def space_check(board, position):
    if position not in range(1,10):
        print("Position needs to be between 1 and 9")
        return False
    if board[position] == " ":
        print(board[position])
        return True
    return False

def full_board_check(board):
    for position in board:
        if board[position] == ' ':
            return False        
    return True

def player_choice(board):
    position = 0
    while not space_check(board, position):
        position = int(input('Please enter a number[1-9]:'))
    return position

def full_board_check(board):
    if " " not in board:
        return True
    return False

print('Welcome to Tic Tac Toe!')
board = ['##',' ',' ',' ',' ',' ',' ',' ',' ',' ']
p1_xo = ""
p2_xo = ""
print("Player 1, please chose if you want to play with X or 0")
p1_xo = player_input()
if p1_xo == "X":
    p2_xo = "0"
else:
    p2_xo = "X"
turn = choose_first()
while True:
    if turn == 1:
        print("Player 1 turn!")
        pos = player_choice(board)
        board[pos] = p1_xo
        display_board(board)
        if win_check(board, p1_xo):
            print("Player 1 is the winner!!!!")
            break
        if full_board_check(board):
            print("It's a tie")
            break
        turn = 2
    else:
        print("Player 2 Turn!")
        pos = player_choice(board)
        board[pos] = p2_xo
        display_board(board)
        if win_check(board, p2_xo):
            print("Player 2 is the winner!!!")
            break
        if full_board_check(board):
            print("It's a tie")
            break
        turn = 1