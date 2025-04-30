# Mod 3 Skills Demo
str1 = "Code never lies, comments sometimes do"

# Calculate the length of the string & display it
print(len(str1))

# Add a new line after the comma & display it
str1 = str1.replace(", " , ",\n")
print(str1)

# Make every character in the string capitalized & display it
print(str1.upper())

#Use slicing to grab just "Code never lies" out of the string.
str2 = str1[0:str1.find(",")]

#Then, calculate the length of the substring and concatenate it onto the end of the substring. Display this.
num1 = len(str2)
num1 = str(num1)
print(num1)
print(str2 + " " + num1)
