import random
import time
from itertools import combinations
def g(N):
    items = []
    for i in range(1,N+1):
        item = [f"item {i}",random.randint(1,5),random.randint(1,10)]
        
        items.append(item)
    return items
def bag(N):
    s = random.choice((2.5,1,4.0))
    size = int(s * N)
    return size

start = time.time()

def knapsack(items,Max_size):
    N = len(items)
    best_value = 0
    best_combination = []
    for r in range(1,N+1):
        for combo in combinations(items,r):
            total_size = sum(item[1] for item in combo)
            total_val = sum(item[2] for item in combo)
            if total_size <= Max_size and total_val>best_value:
                best_value = total_val
                best_combination = combo
    return best_value,best_combination

problem_sizes = [10,12,14,16,18,20,22]
runs_per_size = 10

for N in problem_sizes:
    times = []
    for i in range(runs_per_size):
        items = g(N)
        size = bag(N)
        start=time.time()
        value,combination = knapsack(items,size)
        end=time.time()
        times.append(end-start)
    avg_time = sum(times)/len(times)
    print(f"N = {N} and average time = {avg_time:.4f} Seconds")