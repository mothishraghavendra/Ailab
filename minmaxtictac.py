import math

def pboard(board):
    print("\n")
    print(f"{board[0]}\t{board[1]}\t{board[2]}")
    print(f"{board[3]}\t{board[4]}\t{board[5]}")
    print(f"{board[6]}\t{board[7]}\t{board[8]}")

def win(board):
    winseq = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[6,4,2],[0,3,6],[1,4,7],[2,5,8]]
    for a,b,c in winseq:
        if board[a] == board[b] == board[c] and board[a] != '':
            return board[a]
    return None

def isfull(board):
    return '' not in board

def minimax(board, depth, ismaximizing):
    winner = win(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif isfull(board):
        return 0

    if ismaximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ''
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ''
                best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == '':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                move = i
    return move

def play():
    board = [''] * 9
    print("---- Welcome to Tic Tac Toe ----")
    pboard(board)
    print("You are O and AI is X")

    while True:
        
        while True:
            player_move = int(input("Enter your move (0-8): "))
            if 0 <= player_move <= 8 and board[player_move] == '':
                board[player_move] = 'O'
                break
            else:
                print("Invalid move, try again.")

        pboard(board)
        if win(board) == 'O':
            print("You win!")
            break
        if isfull(board):
            print("It's a draw!")
            break

        ai_move = best_move(board)
        board[ai_move] = 'X'
        print(f"AI chose position {ai_move}")
        pboard(board)

        if win(board) == 'X':
            print("AI wins!")
            break
        if isfull(board):
            print("It's a draw!")
            break

play()