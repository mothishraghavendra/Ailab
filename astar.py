import heapq
def h(board,goal):
    misplaced = 0
    n = len(goal)
    for i in range(n):
        for j in range(n):
            if board[i][j] != goal[i][j] and board[i][j] != 0:
                misplaced += 1
    return misplaced
def blank(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return i,j
def neighbour(board):
    n = len(board)
    x,y = blank(board)
    neig = []

    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx,dy in directions:
        new_x , new_y = x+dx , y+dy
        if (0 <= new_x<n) and (0<=new_y <n):
            new_board = [row[:]for row in board]
            new_board[x][y],new_board[new_x][new_y] = new_board[new_x][new_y],new_board[x][y]
            neig.append(new_board)
    return neig
def astar(start,goal):
    open_list = []
    heapq.heappush(open_list,(h(start,goal),0,start,[]))
    visited = set()
    while open_list:
        f,g,board,path = heapq.heappop(open_list)
        set_tuple = tuple(tuple(row) for row in board)
        if set_tuple in visited:
            continue
        visited.add(set_tuple)

        if board == goal:
            print("Final goal is reached")
            for step in path+[board]:
                for row in step:
                    print(row)
                print()
            return True
        for nb in neighbour(board):
            if tuple(tuple(row) for row in nb)not in visited:
                heapq.heappush(open_list,(g+1+h(nb,goal),g+1,nb,path+[board]))
    print("No solution is found")
    return False
    
goal = [[1,2,3],[4,5,6],[7,8,0]]
board = board = [[1,2,3],
         [4,0,6],
         [7,5,8]]
astar(board,goal)