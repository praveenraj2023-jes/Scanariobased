
regions = ['A', 'B', 'C', 'D']
colors = ['Red', 'Green', 'Blue']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}



def isValid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def backtrack(assignment):
    
    
    if len(assignment) == len(regions):
        return assignment
    
    
    for region in regions:
        if region not in assignment:
            break
    
    
    for color in colors:
        if isValid(region, color, assignment):
            
            assignment[region] = color  
            
            result = backtrack(assignment)
            
            if result:
                return result
            
            del assignment[region]  
    
    return None



solution = backtrack({})

print("Map Coloring Solution:")
print(solution)