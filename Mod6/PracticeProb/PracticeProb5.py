'''
5. Create a list of integers. Use a loop to build a new list
where each element is the square of the corresponding element
in the original list. Print the new list.
'''

int = [3,7,1,9,4,6,5,8,2,0]
square = []
for x in int:
    square.append(x*x)
print(square)
