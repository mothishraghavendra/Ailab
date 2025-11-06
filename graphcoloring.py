def issafe(color,vertix,graph,c):
    for i in range(len(graph)):
        if graph[vertix][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring(color,graph,m,vertex=0):
    if vertex == len(graph):
        return True
    for c in range(1,m+1):
        if issafe(color,vertex,graph,c):
            color[vertex] = c
            if graph_coloring(color,graph,m,vertex+1):
                return True
            color[vertex] = 0
    return False

def solve_graph(graph,m):
    color = [0] * len(graph)
    if graph_coloring(color,graph,m):
        print("Solution exist")
        for v in range(len(graph)):
            print(f"vertex {v} --> color {color[v]}")
    else:
        print("No solution exits")
graph = [
        [0,1,1,1],
        [1,0,1,0],
        [1,1,0,1],
        [1,0,1,0]
    ]
m= 3
solve_graph(graph,3)
