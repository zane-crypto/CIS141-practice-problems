'''
3. Create a list of strings. Write code to create a new
list that includes only the strings longer than three characters.
Print the resulting filtered list.
'''

words = ["cat", "bird", "dog", "snake"]
word3 = []
for word in words:
    if len(word) <= 3:
        word3.append(word)

for x in word3:
    print(x)
