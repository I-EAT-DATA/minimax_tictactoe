import random

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
    return [sn for sn, sv in enumerate(board) if sv.isdigit()]

def result(board, action):
    result = board[:]
    result[action] = player(board)
    return result

def terminal(board, lines):
    # all squares are filled
    if len([sq for sq in board if sq.isdigit()]) == 0:
        return True

    # somebody won
    for l in range(8):
        [a, b, c] = lines[l]
        if not board[a].isdigit() and board[a] == board[b] and board[a] == board[c]:
            return True

def utility(board, lines):
    # all squares are filled
    
    if len([sq for sq in board if sq.isdigit()]) == 0:
        return 0

    # somebody won
    for l in range(8):
        [a, b, c] = lines[l]
        if not board[a].isdigit() and board[a] == board[b] and board[a] == board[c]:
            if board[a] == 'X':
                return 1
            else:
                return -1

def min_value(board, lines):
    if terminal(board, lines):
        return utility(board, lines)

    v = float('inf')

    for action in actions(board):
        v = min(v, max_value(result(board, action), lines))
    return v

def max_value(board, lines):
    if terminal(board, lines):
        return utility(board, lines)

    v = -float('inf')

    for action in actions(board):
        v = max(v, min_value(result(board, action), lines))
    return v
    

def print_board(board):
    for l in range(0, 9, 3):
        print(board[l] + '|' + board[l + 1] + '|' + board[l + 2])
        print('-+-+-')

# gameplay 
def tictactoe():

    print("Do you want to play as 'X' or 'O'?")
    human = 'X' if input().lower().strip() == 'x' else 'O'
    print(human)

    turn = 'X'
    tictactoe_board = [str(i + 1) for i in range(9)]


    for count in range(9):
        turn = player(tictactoe_board)

        print(f"Your move {turn}.")
        print_board(tictactoe_board)

        if turn == human:
            move = ''

            while move == '':
                move = int(input()) - 1

                if tictactoe_board[move].isdigit():
                    tictactoe_board[move] = turn
                else:
                    move = ''
                    print('That place is already filled. Still your move.')
        elif turn == 'X':
            # max player

            v = -float('inf')
            best_action = None
            for action in actions(tictactoe_board):
                min_v = min_value(result(tictactoe_board, action), lines)
                # min_v = max(v, min_value(result(tictactoe_board, action), lines))
                # print(v)
                if min_v > v:
                    v = min_v
                    best_action = action

            # print(f'\n Max value: {v}\n')
            # tictactoe_board = result( tictactoe_board, random.choice(actions(tictactoe_board)) )

            tictactoe_board = result( tictactoe_board, best_action )
        else:
            # min player

            v = float('inf')
            best_action = None

            for action in actions(tictactoe_board):
                max_v = max_value(result(tictactoe_board, action), lines)

                if max_v < v:
                    v = max_v
                    best_action = action

            tictactoe_board = result( tictactoe_board, best_action )


        if terminal(tictactoe_board, lines):
            winner = utility(tictactoe_board, lines)

            # print_board(tictactoe_board)
            print('\nGame Over.\n')
            if winner == 1 or winner == -1:
                print(f'**** {turn} won ****')    
            else:         
                print('Tie game.')
            break
    
    # play again?
    restart = input("Do want to play Again? (y/n) > ")
    if restart.lower().strip() == 'y':  
        tictactoe()

tictactoe()