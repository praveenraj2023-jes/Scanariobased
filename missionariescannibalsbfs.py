def issafe(state):
    mleft, cleft, boat = state
    mright = 3 - mleft
    cright = 3 - cleft
    if mleft < 0 or mright < 0 or cleft < 0 or cright < 0:
        return False
    if mleft > 0 and cleft > mleft:
        return False
    if mright > 0 and cright > mright:
        return False
    return True
def getlegalmoves(state):
    mleft, cleft, boatposition = state
    legalmoves = []
    boatoptions = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]
    for minboat, cinboat in boatoptions:
        if boatposition == 'Left':
            newstate = (mleft - minboat, cleft - cinboat, 'Right')
            action = f"L->R: {minboat}M {cinboat}C"
        else:
            newstate = (mleft + minboat, cleft + cinboat, 'Left')
            action = f"R->L: {minboat}M {cinboat}C"
        if issafe(newstate):
            legalmoves.append((action, newstate))
    return legalmoves
def solvewithbfs(startstate):
    queue = [(startstate, [])]
    visitedstates = set()
    visitedstates.add(startstate)
    while queue:
        currentstate, actionhistory = queue.pop(0)
        if currentstate == (0, 0, 'Right'):
            return actionhistory
        futuremoves = getlegalmoves(currentstate)
        for action, nextstate in futuremoves:
            if nextstate not in visitedstates:
                visitedstates.add(nextstate)
                queue.append((nextstate, actionhistory + [action]))
    return None
if __name__ == "__main__":
    initialstate = (3, 3, 'Left')

    solution = solvewithbfs(initialstate)
    if solution:
        print("Solution:")
        for step, move in enumerate(solution, 1):
            print(f"{step}: {move}")
    else:
        print("No solution")
