from collections import deque
MAXA = 4
MAXB = 3
def bfs(start,goal):
    queue = deque()
    visited = set()
    queue.append((start,[]))
    while queue:
        (a,b),path = queue.popleft()
        if (a,b) in visited:
            continue
        visited.add((a,b))
        if a == goal[0] and b == goal[1]:
            return path + [(a,b)]
        next_state = []
        next_state.append((MAXA,b))
        next_state.append((a,MAXB))
        next_state.append((0,b))
        next_state.append((a,0))
        pour_a_b = min(a,MAXB-b)
        next_state.append((a-pour_a_b,b+pour_a_b))
        pour_b_a = min(MAXA-a,b)
        next_state.append((a+pour_b_a,b-pour_b_a))

        for state in next_state:
            if state not in visited:
                queue.append((state,path+[(a,b)]))
    return None

start = (0, 0)
goal = (2, 0)  # want 2 liters in jug A
solution = bfs(start, goal)
print("Solution path:")
for step in solution:
    print(step)