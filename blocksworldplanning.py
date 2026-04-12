import copy
def getpossiblemoves(currentstate):
    legalmoves = []
    for i in range(len(currentstate)):
        if len(currentstate[i]) == 0:
            continue
        blockweareholding = currentstate[i][-1]
        for j in range(len(currentstate)):
            if i != j:
                newstate = [list(stack) for stack in currentstate]
                pickedup = newstate[i].pop()
                targetblock = newstate[j][-1]
                newstate[j].append(pickedup)
                actionname = f"Move {pickedup} onto {targetblock}"
                newstate = [stack for stack in newstate if stack]
                legalmoves.append((actionname, sorted(newstate)))
        if len(currentstate[i]) > 1:
            newstate = [list(stack) for stack in currentstate]
            pickedup = newstate[i].pop()
            newstate.append([pickedup])
            actionname = f"Unstack {pickedup} to Table"
            newstate = [stack for stack in newstate if stack]
            legalmoves.append((actionname, sorted(newstate)))
    return legalmoves
def planner(startstate, goalstate):
    queue = [(sorted(startstate), [])]
    visited = set()
    visited.add(str(sorted(startstate)))
    while queue:
        currentstate, actionhistory = queue.pop(0)
        if currentstate == sorted(goalstate):
            return actionhistory
        futuremoves = getpossiblemoves(currentstate)
        for actionname, futurestate in futuremoves:
            statestring = str(futurestate)
            if statestring not in visited:
                visited.add(statestring)
                queue.append((futurestate, actionhistory + [actionname]))
    return None
if __name__ == "__main__":
    initial = [
        ['A', 'B'],
        ['C']
    ]
    goal = [
        ['C', 'B', 'A']
    ]
    print(f"Init: {initial}")
    print(f"Goal: {goal}")
    plan = planner(initial, goal)
    if plan:
        print("Plan:")
        for step, instruction in enumerate(plan, 1):
            print(f"Step {step}: {instruction}")
    else:
        print("No plan")
