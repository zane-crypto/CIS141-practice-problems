'''
4.  Create a list of integers. Write code that counts how many
numbers are positive and how many are negative, then print both counts.
'''

int = [3,7,-1,9,-4,-6,5,8,-2,0]
pos = 0
neg = 0
for num in int:
    if num >= 0:
        pos += 1
    else:
        neg += 1
print(f"there are {pos} positive numbers.")
print(f"there are {neg} negative numbers.")
