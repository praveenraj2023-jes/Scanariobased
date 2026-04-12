from collections import deque


def validstate(m, c):
    
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and c > m:
        return False

    if (3-m) > 0 and (3-c) > (3-m):
        return False

    return True


def bfs():

    start = (3,3,1)
    goal = (0,0,0)

    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

    queue = deque()
    queue.append((start,[start]))

    visited = set()

    while queue:

        state,path = queue.popleft()

        if state == goal:
            return path

        visited.add(state)

        m,c,b = state

        for move in moves:

            dm,dc = move

            if b == 1:
                newstate = (m-dm,c-dc,0)
            else:
                newstate = (m+dm,c+dc,1)

            nm,nc,nb = newstate

            if validstate(nm,nc) and newstate not in visited:
                queue.append((newstate,path+[newstate]))

    return None


solution = bfs()

print("Minimum Path:")
for step in solution:
    print(step)

print("\nMinimum crossings:",len(solution)-1)
