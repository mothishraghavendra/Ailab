import random
import math

# we are using sin(x) as our huristic function because it have good number of oscillations
def f(x):
    return math.sin(x)

def hill_climbing(x_start,f,step=0.1,iter=1000):
    x = x_start
    for i in range(iter):
        left,right = x-step,x+step
        if f(left)>f(x):
            x = left
        elif f(right)>f(x):
            x = right
        else:
            break
    return x,f(x)

def random_hill(f,restarts=10):
    bestx = None
    best_val = float('-inf')
    for i in range(restarts):
        x_start = random.uniform(-10,10)
        # uniform(a,b) pis a number x such that a<x<b
        x,val = hill_climbing(x_start,f)

        if val>best_val:
            best_val=val
            bestx = x
        print(f"restart {i+1} : start {x_start} , local max {x} , value = {val}")
    return bestx,best_val

x , val = random_hill(f)
print("\n")
print(f"Global max : {x} and value = {val}")