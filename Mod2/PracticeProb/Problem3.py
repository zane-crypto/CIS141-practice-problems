'''
# 3. Create a program that prompts for the side lengths
of a triangle and computes the area using Heron's formula.
(https://en.wikipedia.org/wiki/Heron%27s_formula)
'''
import math #imports math library

#greets user and asks for input
print("This program calculates the area of a triangle using Heron's formula.")
numA = int(input("Please enter side A of the triangle: "))
numB = int(input("Please enter side B of the triangle: "))
numC = int(input("Please enter side C of the triangle: "))

#calculates and displays semiperimeter
numS = (numA + numB + numC) /2
print("The semiperimeter of your triangle is: ", numS)

#calculates(using math library) and displays area
numX = numS*(numS-numA)*(numS-numB)*(numS-numC)
Area = math.sqrt(numX)
print("The area of your triangle is: ", Area)
#end program
