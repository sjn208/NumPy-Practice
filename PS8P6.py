# Jasmine Sajna
# Problem 6. TicTacToe -- board size given by user
import numpy as np

# grab dimension from user and create board (numpy array) of empty spaces
size = int(input('Enter size of square board: '))
board = np.full((size, size), '[]')
print('BOARD:\n', board)
turn = 'X'  # x-player goes first

End = False  # set a loop to repeat forever to check end
while not End:

    value = False  # set a loop to make sure the position values are valid, and that user gets their turn
    while not value:
        try:
            print(f"\n======Player {turn}'s turn!======")
            colpos = int(input(f'Enter col position 1-{size}: ')) - 1
            rowpos = int(input(f'Enter row position 1-{size}: ')) - 1
            if colpos not in range(0, size) or rowpos not in range(0, size):
                print('Invalid position values! Try again!')
                continue
            else:
                if board[rowpos, colpos] == '[]':
                    board[rowpos, colpos] = turn
                    value = True
                else:
                    print('Spot taken! Try again! ')
                    continue
        except:
            TypeError: print('Not valid type!')  # for case that user enters invalid type in positions

    print('\nBOARD:\n', board)  # display board to user

    # go through row and column of position to check win by making a new array of true/false values
    rowtf = board[rowpos, :] == turn
    coltf = board[:, colpos] == turn

    # check diagonals of board to see if all are same by making array of true/false values
    diag1 = board.diagonal() == turn
    diag2 = np.fliplr(board).diagonal() == turn  # flips board "90 degrees" to check the other diagonal

    # checks if the above arrays are all true values
    if np.all(rowtf) or np.all(coltf) or np.all(diag1) or np.all(diag2):
        End = True
        print(f'\n*******Player {turn} won!********')
    elif '[]' not in board:  # if empty space not in board but no winner, state draw
        print('*******Draw!!********')
        End = True  # loop does not repeat

    # switching turns
    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'
