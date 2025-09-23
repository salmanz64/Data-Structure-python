from Stack import Stack


def parChecker(para):
    s = Stack()
    balanced = True
    i =0
    while i < len(para) and balanced:
        if para[i] in '({[':
            s.push(para[i])
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not match(top,para[i]):
                    balanced = False
        i+=1
    if balanced and s.isEmpty():
        return True
    else:
        return False
    
def match(open,close):
    opens= '({['
    closes = ')}]'
    return opens.index(open) == closes.index(close)
    
    
        
print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))
    
    
