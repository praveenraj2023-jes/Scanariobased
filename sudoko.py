
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]



def isvalid(board, row, col, num):
    
    
    for i in range(9):
        if board[row][i] == num:
            return False
    
    
    for i in range(9):
        if board[i][col] == num:
            return False
    
    
    startrow = row - row % 3
    startcol = col - col % 3
    
    for i in range(3):
        for j in range(3):
            if board[startrow + i][startcol + j] == num:
                return False
    
    return True



def solvesudoku(board):
    
    for row in range(9):
        for col in range(9):
            
            if board[row][col] == 0:
                
                for num in range(1, 10):
                    
                    if isvalid(board, row, col, num):
                        
                        board[row][col] = num  # Assign
                        
                        if solvesudoku(board):
                            return True
                        
                        board[row][col] = 0  
                
                return False
    
    return True



if solvesudoku(board):
    print("Solved Sudoku:")
    for row in board:
        print(row)
else:
    print("No solution exists")