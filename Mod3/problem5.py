'''
5. Print 3 words with a | character (called a pipe) in between them.
Use the appropriate keyword argument in print() to do so.
'''

wrd1 = ("American Clearing House")
new_wrd1 = wrd1.split(" ")
print(new_wrd1)

new_wrd2 = "|".join(new_wrd1)
print(new_wrd2)
