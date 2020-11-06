#TIC TAC TOE GAME

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-" ]

game_still_going = True

winner = None

current_player = "X"

# Display board
def display_board(board):

    for i,pole in enumerate(board,1):
        print(pole) if i%3 == 0 else print(pole, end=" | ")

# play game
def play_game():
    #Display board
    display_board(board)
    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()



    print_winner()

# turning function
def handle_turn(current_player):

    print(current_player,"'s turn.")
    position = input("Choose a position from 1-9: ")

    # corner cases
    while position not in ["1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9"]:

            position = input("Invalid input. Choose a position from 1-9: ")

    position  = int(position) - 1

    while board[position] != "-":
        position = input("THAT PLACE IS OCCUPIED, CHOOSE ANOTHER.Choose a position from 1-9: ")
        position = int(position) - 1

    board[position] = current_player
    display_board(board)

# win or not to win
def check_if_win():

    global winner

    row_winner      = check_rows()
    column_winner   = check_columns()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

# win by row correctness
def check_rows():
    global game_still_going

    for i in range(3):
        row = board[0+3*i] == board[1+3*i] == board[2+3*i] != "-"

        #Return the winner
        if row:
            game_still_going = False
            if i==0:
                return  board[0]
            elif i==1:
                return  board[3]
            elif i==2:
                return  board[6]
        return

# win by column correctness
def check_columns():
    global game_still_going

    for i in range(3):
        column = board[0+i] == board[3+i] == board[6+i] != "-"

        if column:
            game_still_going = False
            if i==0:
                return board[0]
            elif i==1:
                return board[1]
            elif i==2:
                return board[2]
        return

# win by diagonal correctness
def check_diagonal():
    global game_still_going

    diagonal_1 = board[0]==board[4]==board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

# tie?
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def check_if_game_over():

    check_if_win()
    check_if_tie()

#filp players
def flip_player():
    global current_player
    if current_player =="X": current_player ="O"
    else: current_player = "X"
    return

def print_winner():
    if winner == 'X' or winner == '0':
        print(winner + " won.")
    elif winner == None:
        print("Tie.")
    return


play_game()


