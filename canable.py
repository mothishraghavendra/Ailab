from collections import deque;
canable = 3
man = 3

boat_cap = [(1,0),(0,1),(2,0),(0,2),(1,1)]

def isvalid(state):
    ml,cl,boat = state
    mr = man - ml
    cr = canable - cl

    if ml < 0 or cl < 0 or ml>man or cl>canable:
        return False
    if (ml > 0 and ml<cl or mr > 0 and mr<cr):
        return False
    return True

def bfs(start,goal):
    queue = deque()
    visited = set()
    queue.append((start,[start]))
    while queue:
        state , path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        if goal == state:
            return path
        
        ml , cl , boat = state
        for m,c in boat_cap:
            new_state = None
            if boat == 0:
                new_state = (ml-m,cl-c,1)
            else:
                new_state = (ml+m,cl+c,0)
            if isvalid(new_state):
                queue.append((new_state,path+[new_state]))
    return None

start = (3,3,0)
goal = (0,0,1)

solution = bfs(start,goal)
for sol in solution:
    print(sol)