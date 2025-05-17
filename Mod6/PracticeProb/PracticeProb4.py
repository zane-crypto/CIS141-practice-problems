'''
4.  Create a list of integers. Write code that counts how many
numbers are positive and how many are negative, then print both counts.
'''

int = [3,7,1,9,4,6,5,8,2,0]
even = 0
odd = 0
for num in int:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"there are {even} even numbers.")
print(f"there are {odd} odd numbers.")
