import heapq
def heuristic(a, b, target):
    if a == target or b == target:
        return 0
    return 1
def solvewaterjugastar(capacitya, capacityb, target):
    openlist = []
    startstate = (0, 0)
    gscore = 0
    fscore = gscore + heuristic(0, 0, target)
    heapq.heappush(openlist, (fscore, gscore, startstate, [startstate]))
    visited = set()
    while openlist:
        f, g, currentstate, path = heapq.heappop(openlist)
        a, b = currentstate
        if a == target or b == target:
            return path
        if currentstate in visited:
            continue
        visited.add(currentstate)
        nextstates = set()
        nextstates.add((capacitya, b))
        nextstates.add((a, capacityb))
        nextstates.add((0, b))
        nextstates.add((a, 0))
        pourtob = min(a, capacityb - b)
        nextstates.add((a - pourtob, b + pourtob))
        pourtoa = min(b, capacitya - a)
        nextstates.add((a + pourtoa, b - pourtoa))
        for state in nextstates:
            if state not in visited:
                nextg = g + 1
                nextf = nextg + heuristic(state[0], state[1], target)
                heapq.heappush(openlist, (nextf, nextg, state, path + [state]))
    return None
if __name__ == "__main__":
    jug1size = 4
    jug2size = 3
    targetamount = 2
    print(f"Goal: {targetamount}L")
    solution = solvewaterjugastar(jug1size, jug2size, targetamount)
    if solution:
        print("Solution:")
        for stepnum, stepstate in enumerate(solution):
            if stepnum == 0:
                print(f"Start: {stepstate[0]}L, {stepstate[1]}L")
            else:
                print(f"Step {stepnum}: {stepstate[0]}L, {stepstate[1]}L")
    else:
        print("No solution")
