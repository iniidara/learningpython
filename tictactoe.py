theBoard = {'top-L': 'X', 'top-M': ' ', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'O', 'mid-R': ' ',
            'low-L': 'X', 'low-M': '0', 'low-R': 'X'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)