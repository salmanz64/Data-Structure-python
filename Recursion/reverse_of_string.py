def reverseString(word):
    if len(word) == 1:
        return word
    else:
        return word[-1] + reverseString(word[0:-1])
    
    
print(reverseString('hello'))