import math
def checkwinner(board):
    winlines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for line in winlines:
        if board[line[0]] == board[line[1]] == board[line[2]] and board[line[0]] != ' ':
            return board[line[0]]
    if ' ' not in board:
        return 'Tie'
    return None
def minimaxalphabeta(board, depth, ismaximizingplayer, alpha, beta):
    result = checkwinner(board)
    if result == 'X':
        return 10 - depth
    elif result == 'O':
        return -10 + depth
    elif result == 'Tie':
        return 0
    if ismaximizingplayer:
        bestscore = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimaxalphabeta(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                bestscore = max(score, bestscore)
                alpha = max(alpha, bestscore)
                if beta <= alpha:
                    break
        return bestscore
    else:
        bestscore = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimaxalphabeta(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                bestscore = min(score, bestscore)
                beta = min(beta, bestscore)
                if beta <= alpha:
                    break
        return bestscore
def findsmartestmove(board):
    bestscore = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimaxalphabeta(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > bestscore:
                bestscore = score
                move = i
    return move
def printboard(b):
    print(f"\n {b[0]} | {b[1]} | {b[2]} ")
    print("---+---+---")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("---+---+---")
    print(f" {b[6]} | {b[7]} | {b[8]} \n")
if __name__ == "__main__":
    currentboard = ['X', 'O', 'X',
                     ' ', 'O', ' ',
                     ' ', ' ', ' ']
    printboard(currentboard)
    bestmoveindex = findsmartestmove(currentboard)
    print(f"Best move for X: index {bestmoveindex}")
    currentboard[bestmoveindex] = 'X'
    printboard(currentboard)
