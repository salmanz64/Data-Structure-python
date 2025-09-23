def isPalindrome(word):
    if word[0] != word[-1]:
        return False
    else:
        if len(word)==1:
            return True
        else:
            return isPalindrome(word[1:-1])
            
print(isPalindrome("madami'madam"))



# import string

# def is_palindrome_recursive(text):
#     # normalize: lowercase + keep only letters/numbers
#     cleaned = "".join(ch.lower() for ch in text if ch.isalnum())

#     def helper(s, left, right):
#         # base case: crossed pointers -> palindrome
#         if left >= right:
#             return True
#         # mismatch -> not palindrome
#         if s[left] != s[right]:
#             return False
#         # move inward
#         return helper(s, left + 1, right - 1)

#     return helper(cleaned, 0, len(cleaned) - 1)


# # Examples
# print(is_palindrome_recursive("radar"))                       # True
# print(is_palindrome_recursive("madam i’m adam"))              # True
# print(is_palindrome_recursive("Live not on evil"))            # True
# print(is_palindrome_recursive("Reviled did I live, said I, as evil I did deliver"))  # True
# print(is_palindrome_recursive("Go hang a salami; I’m a lasagna hog."))               # True
# print(is_palindrome_recursive("Able was I ere I saw Elba"))   # True
# print(is_palindrome_recursive("Kanakanak"))                   # True
# print(is_palindrome_recursive("Wassamassaw"))                 # True
# print(is_palindrome_recursive("hello"))                       # False
