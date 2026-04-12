def getpossiblemoves(state):
    moves = []
    roomlocations = ['door', 'window', 'middle', 'underBananas']
    if state['monkeyLocation'] == 'underBananas' and state['monkeyHeight'] == 'onBox' and state['hasBanana'] == False:
        newstate = dict(state)
        newstate['hasBanana'] = True
        moves.append(("Grab the bananas!", newstate))
    if state['monkeyLocation'] == state['boxLocation'] and state['monkeyHeight'] == 'floor':
        newstate = dict(state)
        newstate['monkeyHeight'] = 'onBox'
        moves.append(("Climb onto the box", newstate))
    if state['monkeyLocation'] == state['boxLocation'] and state['monkeyHeight'] == 'floor':
        for destination in roomlocations:
            if destination != state['monkeyLocation']:
                newstate = dict(state)
                newstate['monkeyLocation'] = destination
                newstate['boxLocation'] = destination
                moves.append((f"Push the box to the '{destination}'", newstate))
    if state['monkeyHeight'] == 'floor':
        for destination in roomlocations:
            if destination != state['monkeyLocation']:
                newstate = dict(state)
                newstate['monkeyLocation'] = destination
                moves.append((f"Walk to the '{destination}'", newstate))
    return moves
def monkeyplanner(startstate):
    queue = [(startstate, [])]
    visited = set()
    visited.add(str(startstate))
    while queue:
        currentstate, actionhistory = queue.pop(0)
        if currentstate['hasBanana'] == True:
            return actionhistory
        futuremoves = getpossiblemoves(currentstate)
        for actionname, futurestate in futuremoves:
            statestring = str(futurestate)
            if statestring not in visited:
                visited.add(statestring)
                queue.append((futurestate, actionhistory + [actionname]))
    return None
if __name__ == "__main__":
    initialstate = {
        'monkeyLocation': 'door',
        'monkeyHeight': 'floor',
        'boxLocation': 'window',
        'hasBanana': False
    }

    winningplan = monkeyplanner(initialstate)
    if winningplan:
        print("Plan:")
        for step, instruction in enumerate(winningplan, 1):
            print(f"Step {step}: {instruction}")
    else:
        print("No plan found.")
