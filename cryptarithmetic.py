
letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']


def isvalid(assign):
    
    
    if len(set(assign.values())) < len(assign):
        return False
    
    
    if 'S' in assign and assign['S'] == 0:
        return False
    if 'M' in assign and assign['M'] == 0:
        return False
    
    
    if len(assign) == len(letters):
        s,e,n,d = assign['S'], assign['E'], assign['N'], assign['D']
        m,o,r,y = assign['M'], assign['O'], assign['R'], assign['Y']
        
        send  = 1000*s + 100*e + 10*n + d
        more  = 1000*m + 100*o + 10*r + e
        money = 10000*m + 1000*o + 100*n + 10*e + y
        
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
        
        
        if isvalid(assign):
            
            result = backtrack(assign)
            
           
            if result:
                return result
        
        
        del assign[letter]
    
    return None



solution = backtrack({})

print("Solution:")
print(solution)


if solution:
    s,e,n,d = solution['S'], solution['E'], solution['N'], solution['D']
    m,o,r,y = solution['M'], solution['O'], solution['R'], solution['Y']
    
    send  = 1000*s + 100*e + 10*n + d
    more  = 1000*m + 100*o + 10*r + e
    money = 10000*m + 1000*o + 100*n + 10*e + y
    
    print("\nVerification:")
    print(send, "+", more, "=", money)