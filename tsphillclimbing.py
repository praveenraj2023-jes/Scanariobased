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
    numcities = int(input("Enter the number of cities: "))
    locations = []
    print(f"Enter the names of the {numcities} cities (one per line):")
    for i in range(numcities):
        locations.append(input().strip())

    mapdistances = {}
    print("Enter the distances between the cities.")
    for city1 in locations:
        mapdistances[city1] = {}
        for city2 in locations:
            if city1 == city2:
                mapdistances[city1][city2] = 0
            else:
                dist = int(input(f"Enter distance from {city1} to {city2}: "))
                mapdistances[city1][city2] = dist

    print("\nStarting search...")
    finalroute, finaldistance = solvetsphillclimbing(locations, mapdistances)
    print(f"\nFinal Route: {' -> '.join(finalroute)} -> {finalroute[0]}")
    print(f"Final Distance: {finaldistance}")
