def check_brackets(line):
    lefty = '({['
    righty = ')}]'
    
    S = Stack()
    
    for c in line: 
        if c in lefty:
            S.push(c)
        elif c in righty: 
            if S.isEmpty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
                
    return S.isEmpty()