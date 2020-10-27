the_board = {'top-L': '', 'top-C': '', 'top-R': '','mid-L': '', 'mid-C': '', 'mid-R': '','bottom-L': '', 'bottom-C': '', 'bottom-R': ''}

def print_board(board):
    print(board['top-L'] + '  |  ' + board['top-C'] + '  |  ' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '  |  ' + board['mid-C'] + '  |  ' + board['mid-R'])
    print('---+---+---')
    print(board['bottom-L'] + '   |  ' + board['bottom-C'] + ' |  ' + board['bottom-R'])

turn = 'X'
for i in range(9):
    print_board(the_board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(the_board)