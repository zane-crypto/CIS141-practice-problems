'''
4. Create a program that prompts the user for their
birth year and displays a message that says
"You are ___ old". Use an f-string in your solution
to this problem.
'''

birth_year = int(input("When was your birth year? ")) #gets birthyear from user
current_year = int(input("What is the current year? ")) #gets current year from user
age = int((current_year-birth_year)) #does math
print(f"You are {age} years old!") #uses format print to print the value of age varible
