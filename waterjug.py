from collections import deque

def waterjug(jug1,jug2,target):
    visited=set()
    queue=deque()

    queue.append((0,0))

    while queue:
        x,y=queue.popleft()

        if (x,y) in visited:
            continue

        visited.add((x,y))

        print((x,y))


        if x==target or y==target:
            print("Target Reached!")
            return

        queue.append((jug1,y))

        queue.append((x,jug2))

        queue.append((0,y))

        queue.append((x,0))

        pourtojug2=min(x,jug2-y)
        queue.append((x-pourtojug2,y+pourtojug2))

        pourtojug1=min(y,jug1-x)
        queue.append((x+pourtojug1,y-pourtojug1))

    print("No solution found")

waterjug(4,3,2)
