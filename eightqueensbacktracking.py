def printboard(boardstate, n):
    print("\n   " + " ".join([str(i) for i in range(n)]))
    print("  " + "-" * (n * 2 + 1))
    for row in range(n):
        rowstr = f"{row} | "
        for col in range(n):
            if boardstate[row] == col:
                rowstr += "Q "
            else:
                rowstr += ". "
        print(rowstr)
    print("\n")
def issafe(boardstate, currentrow, testcol):
    for previousrow in range(currentrow):
        previouscol = boardstate[previousrow]
        if previouscol == testcol:
            return False
        rowdiff = abs(currentrow - previousrow)
        coldiff = abs(testcol - previouscol)
        if rowdiff == coldiff:
            return False
    return True
def solvequeensbacktracking(boardstate, currentrow, n):
    if currentrow == n:
        return True
    for col in range(n):
        if issafe(boardstate, currentrow, col):
            boardstate[currentrow] = col
            success = solvequeensbacktracking(boardstate, currentrow + 1, n)
            if success:
                return True
            boardstate[currentrow] = -1
    return False
if __name__ == "__main__":
    n = 8
    chessboard = [-1] * n
    solutionfound = solvequeensbacktracking(chessboard, 0, n)
    if solutionfound:
        print("Solution:")
        printboard(chessboard, n)
        print(chessboard)
    else:
        print("No solution")
