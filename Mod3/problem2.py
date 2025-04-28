'''
2. Prompt the user for their name and their age. Calculate their age next year.
Use string concatenation to print "Hello, <name>! You are <age1> years old.
Next year, you will be <age2> years old."
'''

name = input("What is your name? ")
age1 = input("How old are you? ")
age1int = int(age1)
age2int = age1int + 1
age2str = str(age2int)
print("Hello, " + name + "! You are " + age1 + " years old. Next year, you will be " + age2str + " years old.")
