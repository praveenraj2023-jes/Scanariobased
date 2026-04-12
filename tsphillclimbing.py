import random
def calculatetotaldistance(route, distances):
    total = 0
    for i in range(len(route) - 1):
        currentcity = route[i]
        nextcity = route[i + 1]
        total += distances[currentcity][nextcity]
    lastcity = route[-1]
    firstcity = route[0]
    total += distances[lastcity][firstcity]
    return total
def getneighbors(route):
    neighbors = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            neighbor = route.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors
def solvetsphillclimbing(cities, distances):
    currentroute = list(cities)
    random.shuffle(currentroute)
    currentdistance = calculatetotaldistance(currentroute, distances)
    print(f"Start: {' -> '.join(currentroute)} -> {currentroute[0]}, Dist: {currentdistance}")
    step = 1
    while True:
        neighbors = getneighbors(currentroute)
        bestneighbor = None
        bestneighbordistance = float('inf')
        for neighbor in neighbors:
            neighbordistance = calculatetotaldistance(neighbor, distances)
            if neighbordistance < bestneighbordistance:
                bestneighbor = neighbor
                bestneighbordistance = neighbordistance
        if bestneighbordistance >= currentdistance:
            print("Local minimum reached.")
            break
        print(f"Step {step}: {' -> '.join(bestneighbor)}, Dist: {bestneighbordistance}")
        currentroute = bestneighbor
        currentdistance = bestneighbordistance
        step += 1
    return currentroute, currentdistance
if __name__ == "__main__":
    locations = ['Chennai', 'Bangalore', 'Hyderabad', 'Mumbai']
    mapdistances = {
        'Chennai':   {'Chennai': 0, 'Bangalore': 350, 'Hyderabad': 630, 'Mumbai': 1300},
        'Bangalore': {'Chennai': 350, 'Bangalore': 0, 'Hyderabad': 570, 'Mumbai': 980},
        'Hyderabad': {'Chennai': 630, 'Bangalore': 570, 'Hyderabad': 0, 'Mumbai': 700},
        'Mumbai':    {'Chennai': 1300, 'Bangalore': 980, 'Hyderabad': 700, 'Mumbai': 0}
    }
    finalroute, finaldistance = solvetsphillclimbing(locations, mapdistances)
    print(f"Route: {' -> '.join(finalroute)} -> {finalroute[0]}")
    print(f"Distance: {finaldistance}")
