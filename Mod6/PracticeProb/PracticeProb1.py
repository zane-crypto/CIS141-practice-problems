'''
1. Create a list of integers (you get to pick!).
Write code to iterate through the list and calculate
the sum of all even numbers. Print the resulting sum.
'''
sum = 0
num = [1, 2, 3, 4, 5]
for x in num:
    if (x % 2) == 0:
        sum += x
print(sum)
