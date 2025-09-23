
def toStr(num,base):
    convertedString = '0123456789ABCDEF'
    if num <base:
        return convertedString[num]
    else:
        return toStr(num//base,base) + convertedString[num%base]
    

print(toStr(1453,16))

