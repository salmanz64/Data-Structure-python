from Stack import Stack

def divideByTwo(decimalNum):
    
    s = Stack()
    while decimalNum > 0:
        rem = decimalNum % 2
        s.push(rem)
        decimalNum = decimalNum // 2
    
    binary = ""
    while not s.isEmpty():
        binary = binary + str(s.pop())
        
    return binary

print(divideByTwo(42)) 