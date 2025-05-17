'''
2. Create a list of strings. Write code that counts
how many times the word "Olympic" appears in the list,
and then print the count.
'''
count = 0
strings = ["olympic", "athens", "zeus", "hera", "hades", "olympic"]
for string in strings:
    if string == "olympic":
        count += 1
print(count)
