class wumpuslogicagent:
    def __init__(self, gridsize=4):
        self.size = gridsize
        self.visited = set()
        self.safecells = set([(0, 0)])
        self.nowumpushere = set([(0, 0)])
        self.nopithere = set([(0, 0)])
        self.possiblewumpus = set()
        self.possiblepits = set()
        for x in range(gridsize):
            for y in range(gridsize):
                if (x, y) != (0, 0):
                    self.possiblewumpus.add((x, y))
                    self.possiblepits.add((x, y))
    def getadjacentcells(self, x, y):
        neighbors = []
        if x > 0: neighbors.append((x - 1, y))
        if x < self.size - 1: neighbors.append((x + 1, y))
        if y > 0: neighbors.append((x, y - 1))
        if y < self.size - 1: neighbors.append((x, y + 1))
        return neighbors
    def addsensorreadings(self, x, y, hasstench, hasbreeze):
        print(f"({x},{y}) Stench: {hasstench}, Breeze: {hasbreeze}")
        self.visited.add((x, y))
        neighbors = self.getadjacentcells(x, y)
        if not hasstench:
            print("No stench. Neighbors Wumpus-Free.")
            for n in neighbors:
                self.nowumpushere.add(n)
                if n in self.possiblewumpus:
                    self.possiblewumpus.remove(n)
        else:
            possiblehidingspots = set(n for n in neighbors if n not in self.nowumpushere)
            self.possiblewumpus = self.possiblewumpus.intersection(possiblehidingspots)
            print(f"Wumpus possible in: {self.possiblewumpus}")
        if not hasbreeze:
            print("No breeze. Neighbors Pit-Free.")
            for n in neighbors:
                self.nopithere.add(n)
                if n in self.possiblepits:
                    self.possiblepits.remove(n)
        for r in range(self.size):
            for c in range(self.size):
                if (r, c) in self.nowumpushere and (r, c) in self.nopithere:
                    self.safecells.add((r, c))
    def getnextsafemoves(self):
        return self.safecells - self.visited
if __name__ == "__main__":

    agent = wumpuslogicagent(gridsize=4)
    agent.addsensorreadings(0, 0, hasstench=False, hasbreeze=False)
    safemoves = agent.getnextsafemoves()
    print(f"Safe moves: {safemoves}")
    agent.addsensorreadings(0, 1, hasstench=False, hasbreeze=True)
    safemoves = agent.getnextsafemoves()
    print(f"Safe moves: {safemoves}")
    agent.addsensorreadings(1, 0, hasstench=True, hasbreeze=True)
    print(f"Wumpus at: {agent.possiblewumpus}")
