'''
Write a small Python program that asks the user for 
their name, the total bill amount at a restaurant, 
and the number of people splitting the bill. 
The program will then calculate how much each 
person should pay and display the result with 
a friendly message.
'''

#Ask for users name.
usr_name = input("What is your name? ")
print("Hello,", usr_name)

#Request total bill.
total_bill = int(input("What is the total bill? $"))

#Request number of people splitting bill.
total_guests = int(input("How many people are in your party? "))

#Calculation: how much each person owes
per_guest = total_bill/total_guests

#Display friendly message w/ how much each person owes
print(f"The cost of the meal is: ${per_guest:.2f} per person.")
