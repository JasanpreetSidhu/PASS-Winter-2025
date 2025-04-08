# Tic-Tac-Toe
# Below function checks for invalid board state
# Look for April preLabQ2Complete.py for full solution

gameBoard = [
    ['x', ' ', ' '],
    ['x', 'o', 'o'],
    ['x', ' ', 'o']
    ]

def getGameStatus(board):
    isGameWon = False

    # check if board is invalid
    
    xCount = board[0].count('x')
    xCount = xCount + board[1].count('x')
    xCount = xCount + board[2].count('x')

    oCount = board[0].count('o')
    oCount = oCount + board[1].count('o')
    oCount = oCount + board[2].count('o')

    if (xCount < oCount or xCount > oCount + 1):
        raise ValueError("Invalid board state")
    
    return isGameWon

result = getGameStatus(gameBoard)
print(result)
