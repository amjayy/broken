import random

def drawBoard(board):
 #This function prints out the board.

# board = 10 strings repping board 0 index not included
    print('   |   |')
    print(' ' + board[7] +' | ' + board[8] + ' | '+ board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '  + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |') 
    print('-----------')
    print('   |     |')
    print(' '  + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |     |')

def inputPlayerLetter():
#lets player type which letter they want to be
#returns list with player's letter as first item and the computer's as the second
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print ('Do you want to be X or O?')
        letter = input().upper()
        
        # the first element in thr list in the player's number, the second letter is the computer's
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst():
    #Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playagain():
    #This function returns True if player wants to play again, otherwise it returns False.
    print(' Do you want to play again?(yes or no)')
    return input().lower().startswith('y')

def makeMove(board,letter,move):
    board[move] = letter

