'''
#2. Write a function called is_palindrome(s) that checks whether 
a string is a palindrome (reads the same forward and backward, 
ignoring case). The function should return either True or False.
'''

def is_palindrome(word):
    bool = False
    forwards = word.lower()
    backwards = word.lower() [::-1]
    if forwards == backwards:
        bool = True
    return bool

word1 = input("Please enter a word: ")

print(is_palindrome(word1))
