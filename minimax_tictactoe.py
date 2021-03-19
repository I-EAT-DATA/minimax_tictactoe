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

def terminal(board, lines, count):
    # all squares are filled
    if count == 8:
        return True

    # somebody won
    for l in range(8):
        [a, b, c] = lines[l]
        if not board[a].isdigit() and board[a] == board[b] and board[a] == board[c]:
            return True

def utility(board, lines, count):
    # all squares are filled
    if count == 8:
        return 0

    # somebody won
    for l in range(8):
        [a, b, c] = lines[l]
        if not board[a].isdigit() and board[a] == board[b] and board[a] == board[c]:
            if board[a] == 'X':
                return 1
            else:
                return -1

def min_value(board, lines, count):
    if terminal(board, lines, count):
        return utility(board, lines, count)

    v = 1

    for action in actions(board):
        v = max(v, max_value(result(board, action), lines, count))
    return v

def max_value(board, lines, count):
    if terminal(board, lines, count):
        return utility(board, lines, count)

    v = -1

    for action in actions(board):
        v = max(v, min_value(result(board, action), lines, count))
    return v
    

def print_board(board):
    for l in range(0, 9, 3):
        print(board[l] + '|' + board[l + 1] + '|' + board[l + 2])
        print('-+-+-')

# gameplay 
def tictactoe():

    turn = 'X'
    tictactoe_board = [str(i + 1) for i in range(9)]


    for count in range(9):
        # print(random.choice(actions(tictactoe_board)))
        # print(player(tictactoe_board))
        
        turn = player(tictactoe_board)

        print_board(tictactoe_board)
        # print_board( result( tictactoe_board, random.choice(actions(tictactoe_board)) ) )
        print(f"Your move {turn}.")

        if turn == 'X':
            move = ''

            while move == '':
                move = int(input()) - 1

                if tictactoe_board[move].isdigit():
                    tictactoe_board[move] = turn
                else:
                    move = ''
                    print('That place is already filled. Still your move.')
        else:
            tictactoe_board = result( tictactoe_board, random.choice(actions(tictactoe_board)) )

        if terminal(tictactoe_board, lines, count):
            winner = utility(tictactoe_board, lines, count)

            print_board(tictactoe_board)
            print('\nGame Over.\n')
            if winner == 1 or winner == -1:
                print(f'**** {turn} won ****')    
            else:         
                print('Tie game.')
            break
    
    # play again?
    restart = input("Do want to play Again? (y/n) > ")
    if restart.lower().strip() == 'y':  
        # for sn in range(len(tictactoe_board)):
        #     tictactoe_board[sn] = ' '
        tictactoe()

tictactoe()