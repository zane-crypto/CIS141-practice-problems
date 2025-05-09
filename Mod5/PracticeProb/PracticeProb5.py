'''
5. Write a program that continuously asks the user to input a number.
If the user enters 0, immediately stop asking for more numbers.
Otherwise, print the number they entered. Sample interaction:

Enter a number (0 to stop): 4
You entered 4
Enter a number (0 to stop): 7
You entered 7
Enter a number (0 to stop): 0
Exiting...
'''
count = True
while count == True:
    i = int(input("Enter a number (0 to stop)"))
    print(f"you entered {i}")
    if i == 0:
        count = False
else: print("Exiting...")
print("Ta Da!")
