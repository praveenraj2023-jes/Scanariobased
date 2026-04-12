
letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']


def isValid(assign):
    
    
    if len(set(assign.values())) < len(assign):
        return False
    
    
    if 'S' in assign and assign['S'] == 0:
        return False
    if 'M' in assign and assign['M'] == 0:
        return False
    
    
    if len(assign) == len(letters):
        S,E,N,D = assign['S'], assign['E'], assign['N'], assign['D']
        M,O,R,Y = assign['M'], assign['O'], assign['R'], assign['Y']
        
        send  = 1000*S + 100*E + 10*N + D
        more  = 1000*M + 100*O + 10*R + E
        money = 10000*M + 1000*O + 100*N + 10*E + Y
        
        return send + more == money
    
    return True



def backtrack(assign):
    
    
    if len(assign) == len(letters):
        return assign
    
    
    for letter in letters:
        if letter not in assign:
            break
    
    
    for digit in range(10):
        
        assign[letter] = digit 
        
        
        if isValid(assign):
            
            result = backtrack(assign)
            
           
            if result:
                return result
        
        
        del assign[letter]
    
    return None



solution = backtrack({})

print("Solution:")
print(solution)


if solution:
    S,E,N,D = solution['S'], solution['E'], solution['N'], solution['D']
    M,O,R,Y = solution['M'], solution['O'], solution['R'], solution['Y']
    
    send  = 1000*S + 100*E + 10*N + D
    more  = 1000*M + 100*O + 10*R + E
    money = 10000*M + 1000*O + 100*N + 10*E + Y
    
    print("\nVerification:")
    print(send, "+", more, "=", money)