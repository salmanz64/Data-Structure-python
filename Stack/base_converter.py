from Stack import Stack

def baseConverter(decimalNum,base):
    
    s = Stack()
    decimal = '0123456789ABCDEF'
    while decimalNum > 0:
        rem = decimalNum % base
        s.push(rem)
        decimalNum = decimalNum // base
    
    newString = ""
    while not s.isEmpty():
        newString = newString + decimal[s.pop()]
        
    return newString

print(baseConverter(26,26))
print(baseConverter(256,16))  