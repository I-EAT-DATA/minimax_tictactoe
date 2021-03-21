''' 
Todo:
    - Bookeep the actual value for both best_min_v (high as possible) and best_max_v (low as possible) for better alpha beta pruning

Done:
    - 

Notes:
    - 
'''

import random
import time

class MinimaxTictactoe:
    def __init__(self):
        self.lines = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        self.best_min_v = -float('inf')
        self.best_max_v = float('inf')


    def player(self, board):
        return 'O' if board.count('X') > board.count('O') else 'X'

    def actions(self, board):
        return [sn for sn, sv in enumerate(board) if sv.isdigit()]

    def result(self, board, action):
        result = board[:]
        result[action] = self.player(board)
        return result

    def terminal(self, board, lines):

        # somebody won
        for l in range(8):
            [a, b, c] = lines[l]
            if not board[a].isdigit() and board[a] == board[b] and board[a] == board[c]:
                return True

        # all squares are filled
        if len([sq for sq in board if sq.isdigit()]) == 0:
            return True

    def utility(self, board, lines):

        # somebody won
        for l in range(8):
            [a, b, c] = lines[l]
            if not board[a].isdigit() and board[a] == board[b] and board[a] == board[c]:
                if board[a] == 'X':
                    return 1
                else:
                    return -1

        # all squares are filled
        if len([sq for sq in board if sq.isdigit()]) == 0:
            return 0

    def min_value(self, board, lines):
        if self.terminal(board, lines):
            return self.utility(board, lines)

        v = float('inf')

        for action in self.actions(board):
            v = min(v, self.max_value(self.result(board, action), lines))
            if v < self.best_min_v:
                break
        return v

    def max_value(self, board, lines):
        if self.terminal(board, lines):
            return self.utility(board, lines)

        v = -float('inf')

        for action in self.actions(board):
            v = max(v, self.min_value(self.result(board, action), lines))
            if v > self.best_max_v:
                break
        return v
        

    def print_board(self, board):
        for l in range(0, 9, 3):
            print(board[l] + '|' + board[l + 1] + '|' + board[l + 2])
            print('-+-+-')

    # gameplay 
    def tictactoe(self):

        print("Do you want to play as 'X' or 'O'?")
        human = 'X' if input().lower().strip() == 'x' else 'O'

        turn = 'X'
        tictactoe_board = [str(i + 1) for i in range(9)]


        for count in range(9):
            turn = self.player(tictactoe_board)

            print(f"Your move {turn}.")
            self.print_board(tictactoe_board)

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

                start = time.time()

                self.best_min_v = -float('inf')
                best_action = None
                for action in self.actions(tictactoe_board):
                    min_v = self.min_value(self.result(tictactoe_board, action), self.lines)
                    print(self.best_min_v)
                    if min_v > self.best_min_v:
                        self.best_min_v = min_v
                        best_action = action

                tictactoe_board = self.result( tictactoe_board, best_action )

                print(f'Calculation time: {time.time() - start}')
            else:
                # min player

                self.best_max_v = float('inf')
                best_action = None

                for action in self.actions(tictactoe_board):
                    max_v = self.max_value(self.result(tictactoe_board, action), self.lines)

                    if max_v < self.best_max_v:
                        self.best_max_v = max_v
                        best_action = action

                tictactoe_board = self.result( tictactoe_board, best_action )


            if self.terminal(tictactoe_board, self.lines):
                winner = self.utility(tictactoe_board, self.lines)

                self.print_board(tictactoe_board)
                print('\nGame Over.\n')
                if winner == 1 or winner == -1:
                    print(f'**** {turn} won ****')    
                else:         
                    print('Tie game.')
                break
        
        # play again?
        restart = input("Do want to play Again? (y/n) > ")
        if restart.lower().strip() == 'y':  
            self.tictactoe()


MinimaxTictactoe().tictactoe()