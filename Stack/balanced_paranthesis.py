from Stack import Stack



def parChecker(para):
    s = Stack()
    balanced = True
    i =0
    while i < len(para) and balanced:
        if para[i] == "(":
            s.push("(")
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        i+=1
    if balanced and s.isEmpty():
        return True
    else:
        return False
        
print(parChecker('((()))'))
print(parChecker('(()'))    
    
    
