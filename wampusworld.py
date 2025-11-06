# W = Wumpus, P = Pit, G = Gold, A = Agent, . = Empty
world = [
    ['.', '.', '.', 'P'],
    ['W', 'G', 'P', '.'],
    ['.', '.', '.', '.'],
    ['A', '.', 'P', '.']
]

def get_perceptions(x, y):
    perceptions = []
    n = len(world)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if world[nx][ny] == 'W':
                perceptions.append('Stench')
            elif world[nx][ny] == 'P':
                perceptions.append('Breeze')
            elif world[nx][ny] == 'G':
                perceptions.append('Glitter')
    return perceptions

agent_x, agent_y = 3, 0
moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # Right, Up, Left, Down
visited = set()
found_gold = False

def is_safe(x, y):
    return world[x][y] not in ('W', 'P')

def move_agent(x, y):
    global found_gold
    if (x, y) in visited or found_gold:
        return

    visited.add((x, y))
    perceptions = get_perceptions(x, y)
    print(f"\nAgent at ({x}, {y}) perceives: {perceptions}")

    if 'Glitter' in perceptions:
        print("Agent found the GOLD at", (x, y))
        found_gold = True
        return

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) not in visited and is_safe(nx, ny):
            move_agent(nx, ny)

move_agent(agent_x, agent_y)

if not found_gold:
    print("\nGold not found, but agent stayed safe!")
