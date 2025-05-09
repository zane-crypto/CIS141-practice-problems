'''
1. Prompt the user for a positive integer n. Use a while loop to
sum all the integers from 1 up to n. Print the final sum.
'''

# Takes the input of n given by the user
n = int(input("Enter a number: "))

# Initialize the variables 'count' and 'total'
count = n
total = 0

while count > 0:
    total += count
    count -= 1

# Prints the sum of N natural numbers.
print(f"The sum of the first {n} numbers is: {total}")
