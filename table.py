def layout(N,L,C):
    assignment = {i:None for i in range(N)}
    def issafe(guest,table):
        for x,y in L:
            if guest == x and assignment[y] == table:
                return False
            if guest==y and assignment[x] == table:
                return False
        return True
    def backtrack(guest):
        if guest == N:
            return True
        for table in range(C):
            if issafe(guest,table):
                assignment[guest] = table
                if backtrack(guest+1):
                    return True
                assignment[guest] = None
        return False
    if backtrack(0):
        return assignment
    else:
        return None
    

n = 4
c = 2
l = [(0,1),(2,3)]
print(layout(n,l,c))
