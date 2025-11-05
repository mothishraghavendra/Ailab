from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbours = []

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_nodes(self, val):
        if val not in self.nodes:
            self.nodes[val] = Node(val)

    def add_edges(self, fromm, to):
        if fromm in self.nodes and to in self.nodes:
            from_node = self.nodes[fromm]
            to_node = self.nodes[to]
            from_node.neighbours.append(to_node)
            to_node.neighbours.append(from_node)

def bfs(graph, stv):
    visited = set()
    q = deque()
    q.append(graph.nodes[stv])
    visited.add(stv)

    while q:
        current = q.popleft()
        print(current.val, end=" ")
        for neighbor in current.neighbours:
            if neighbor.val not in visited:
                visited.add(neighbor.val)
                q.append(neighbor)

def dfs(graph, stv, visited=None):
    if visited is None:
        visited = set()

    node = graph.nodes[stv]
    visited.add(node.val)
    print(node.val, end=" ")
    for neighbor in node.neighbours:
        if neighbor.val not in visited:
            dfs(graph, neighbor.val, visited)

g = Graph()
g.add_nodes('A')
g.add_nodes('B')
g.add_nodes('C')
g.add_nodes('D')
g.add_nodes('E')

g.add_edges('A', 'B')
g.add_edges('A', 'C')
g.add_edges('B', 'D')
g.add_edges('D', 'E')
g.add_edges('E', 'C')

print("BFS traversal:")
bfs(g, 'A')

print("\n\nDFS traversal:")
dfs(g, 'A')
