import random

tictactoe_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def player(board):
    return 'O' if board.count('X') > board.count('O') else 'X'

def actions(board):
    return [sn for sn, sv in enumerate(board) if sv == ' ']

def result(board, action):
    result = board[:]
    result[action] = player(board)
    return result

def terminal(board, lines, count):
    # all squares are filled
    if count == 8:
        return 0

    # somebody won
    for l in range(8):
        [a, b, c] = lines[l]
        if board[a] != ' ' and board[a] == board[b] and board[a] == board[c]:
            if board[a] == "X":
                return 1
            else:
                return -1

def print_board(board):
    for l in range(0, 9, 3):
        print(board[l] + '|' + board[l + 1] + '|' + board[l + 2])
        print('-+-+-')

# gameplay 
def tictactoe():

    turn = 'X'

    for count in range(9):
        # print(random.choice(actions(tictactoe_board)))
        # print(player(tictactoe_board))
        
        turn = player(tictactoe_board)

        print_board(tictactoe_board)
        # print_board( result( tictactoe_board, random.choice(actions(tictactoe_board)) ) )
        print(f"Your move {turn}.")

        move = ''

        while move == '':
            move = int(input()) - 1

            if tictactoe_board[move] == ' ':
                tictactoe_board[move] = turn
            else:
                move = ''
                print('That place is already filled. Still your move.')

        is_terminal = terminal(tictactoe_board, lines, count)

        if is_terminal is not None:
            print_board(tictactoe_board)
            print('\nGame Over.\n')
            if is_terminal == 1 or is_terminal == -1:
                print(f'**** {turn} won ****')    
            else:         
                print('Tie game.')
            break

        # check for win
        # if count >= 5:
        #     for l in range(8):
        #         [a, b, c] = lines[l]
        #         if tictactoe_board[a] != ' ' and tictactoe_board[a] == tictactoe_board[b] and tictactoe_board[a] == tictactoe_board[c]:
        #             print_board(tictactoe_board)
        #             print("\nGame Over.\n")                
        #             print(f"**** {turn} won ****")                
        #             break
        #     else:
        #         # check if the board is full
        #         if count == 8:
        #             print_board(tictactoe_board)
        #             print("\nGame Over.\n")                
        #             print("Tie Game")
        #             break
        #         continue
        #     break
    
    # play again?
    restart = input("Do want to play Again? (y/n) > ")
    if restart.lower().strip() == 'y':  
        for sn in range(len(tictactoe_board)):
            tictactoe_board[sn] = ' '
        tictactoe()

tictactoe()