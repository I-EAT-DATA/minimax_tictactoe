
theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

lines = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['1', '4', '7'],
    ['2', '5', '8'],
    ['3', '6', '9'],
    ['1', '5', '9'],
    ['3', '5', '7']
]


def printBoard(board):
    for l in range(0, 9, 3):
        print(board[str(l + 1)] + '|' + board[str(l + 2)] + '|' + board[str(l + 3)])
        print('-+-+-')

# all the gameplay functionality.
def game():

    turn = 'X'

    for count in range(10):
        printBoard(theBoard)
        print(f"Your move {turn}.")

        move = ''

        while move == '':
            move = input()

            if theBoard[move] == ' ':
                theBoard[move] = turn
            else:
                move = ''
                print("That place is already filled. Still your move.")

        # check for win
        if count >= 4:
            for l in range(len(lines)):
                [a, b, c] = lines[l]
                if theBoard[a] != ' ' and theBoard[a] == theBoard[b] and theBoard[a] == theBoard[c]:
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    print(f"**** {turn} won ****")                
                    break
            else:
                continue
            break

        # If neither X nor O wins and the board is full, the result is tie.
        if count == 8:
            print("\nGame Over.\n")                
            print("Tie Game")
            break

        # Change the player after every move.    
        turn = 'O' if turn == 'X' else 'X'
    
    # Play again?
    restart = input("Do want to play Again? (y/n) > ")
    if restart.lower().strip() == 'y':  
        for key in range(1, len(theBoard) + 1):
            theBoard[str(key)] = ' '
        game()

if __name__ == "__main__":
    game()