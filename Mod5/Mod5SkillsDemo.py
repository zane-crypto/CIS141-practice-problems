'''
Write a program that solves this problem:

    Use a loop (for or while) to go through numbers from 1 to 20.
    If a number is a multiple of 3, use continue to skip printing it.
    Otherwise, print the number.

When you've finished creating your program, start recording:

    Explain your code at a high-level, scrolling through all the code, if it isn't visible on the screen all at once. (No need to read through every word.)
    Test your code to demonstrate that it is functional.
    Explain how the loop your wrote works, as if you were explaining it to a student who was learning about this for the first time. Discuss what is happening in your program for at least 4 iterations of the loop.
'''
i = 0
while i <= 20:
    i+=1
    if i % 3 == 0:
        continue
    print(i)
else: print("Ta Da!")
