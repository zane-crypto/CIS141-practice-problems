'''
4. Prompt the user for: a word, a first index, and a last index.
Slice the word at the indexes provided by the user and print to the screen.
'''

wrd1 = input("Please enter a word: ")
indx1 = int(input("Please enter a starting number(index): "))
indx2 = int(input("Please enter a ending number(index): "))

print(wrd1[indx1:indx2])
