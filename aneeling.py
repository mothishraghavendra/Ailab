import random
import math
def f(x):
    return math.sin(x)
def annealing(f, temp=1000, cooling=0.99, step=0.1, iterations=1000):
    x = random.uniform(-10, 10)
    for i in range(iterations):
        new_x = x + random.uniform(-step, step)
        delta = f(new_x) - f(x)
        if delta > 0 or random.random() < math.exp(delta / temp):
            x = new_x
        temp *= cooling
    return x, f(x)
best_x, best_y = annealing(f)
print("best x =", best_x)
print("best y =", best_y)
