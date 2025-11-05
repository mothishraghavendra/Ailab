N = 8;

def printboard(board):
    for row in board:
        print("".join(row))
    print("\n")
def issafe(board,row,col):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    i,j = row-1,col-1
    while i>=0 and j>=0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    i,j = row-1,col+1
    while i>=0 and j<N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    return True

def nqueen(board,row):
    if row==N:
        printboard(board)
        return True
    
    for col in range(N):
        if issafe(board,row,col):
            board[row][col] = 'Q'
            if nqueen(board,row+1):
                return True
            board[row][col] = '.'
    return False

board = [["." for i in range(N)]for _ in range(N)]
nqueen(board,0)