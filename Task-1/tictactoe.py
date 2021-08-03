
# initialising the tictactoe game
def display_board(board):
    mainBoard = """
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
"""

    # code to enter the input of the position of x or o in the board
    for i in range(1, 10):
        if (board[i] == 'O' or board[i] == 'X'):
            mainBoard = mainBoard.replace(str(i), board[i])
        else:
            mainBoard = mainBoard.replace(str(i), ' ')
    print(mainBoard)

# code for user to select which symbol we wants to choose


def player_input():
    symbol1 = input("Please pick an option 'X' or 'O' ")
    while True:
        if symbol1.upper() == 'X':
            symbol2 = 'O'
            print("You've choosen " + symbol1 +
                  ". Player 2 will be " + symbol2)
            return symbol1.upper(), symbol2
        elif symbol1.upper() == 'O':
            symbol2 = 'X'
            print("You've choosen " + symbol1 +
                  ". Player 2 will be " + symbol2)
            return symbol1.upper(), symbol2
        else:
            symbol1 = input("Please pick an option 'X' or 'O' ")


def place_marker(board, marker, position):
    board[position] = marker
    return board


def space_check(board, position):
    return board[position] == '#'


# code to check the whole board and return the boolean value of true or false whether the board is full or not
def full_board_check(board):
    return len([x for x in board if x == '#']) == 1

# to check if the user has won


def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:  # horizontal check
        return True
    if board[4] == board[5] == board[6] == mark:  # horizontal check
        return True
    if board[7] == board[8] == board[9] == mark:  # horizontal check
        return True
    if board[1] == board[4] == board[7] == mark:  # vertical check
        return True
    if board[2] == board[5] == board[8] == mark:  # vertical check
        return True
    if board[3] == board[6] == board[9] == mark:  # vertical check
        return True
    if board[1] == board[5] == board[9] == mark:  # diagonal check
        return True
    if board[3] == board[5] == board[7] == mark:  # diagonal check
        return True
    return False


def player_selection(board):
    selection = input("Please select an empty space between 1 and 9 : ")
    while not space_check(board, int(selection)):
        selection = input(
            "This space isn't free. Please choose a different number between 1 to 9 : ")
    return selection


def replay():
    playAgain = input("Do you want to play again (y/n) ? ")
    if playAgain.lower() == 'y':
        return True
    if playAgain.lower() == 'n':
        return False


if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    i = 1
    # Choose your side
    players = player_input()
    # Empty board init
    board = ['#'] * 10
    while True:
        # Set the game up here
        game_on = full_board_check(board)
        while not game_on:
            # Player to choose where to put the mark
            position = player_selection(board)
            # Who's playin ?
            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]
            # Play !
            place_marker(board, marker, int(position))
            # Check the board
            display_board(board)
            i += 1
            if win_check(board, marker):
                print("You won !")
                break
            game_on = full_board_check(board)
        if not replay():
            break
        else:
            i = 1
            # Choose your side
            players = player_input()
            # Empty board init
            board = ['#'] * 10
