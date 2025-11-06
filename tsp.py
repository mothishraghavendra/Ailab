from itertools import permutations
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
n = len(dist)
start = 0
nodes = range(n)
min_cost = float('inf')
best_path = []

for perm in permutations([i for i in nodes if i!= start]):
    path = [start]+list(perm)+[start]
    cost = sum(dist[path[i]][path[i+1]] for i in range(len(path)-1))
    if cost < min_cost:
        min_cost = cost
        best_path = path
print("Minimum cost :",min_cost)
print("Best path :",best_path)