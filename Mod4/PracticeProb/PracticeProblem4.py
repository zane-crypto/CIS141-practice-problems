'''
4. A theater wants to enforce age restrictions for movie tickets.
Ask the user for their age, and tell them whether they can see G
(appropriate for under 13), PG-13 (appropriate for 13 to 17), or
R (appropriate for over 18) rated movies.
'''

age = int(input("Please enter your age: "))

if age >= 18:
    print("You can watch any movie you want!")
elif ((age <= 17) and (age >= 13)):
    print("You can watch G and PG-13 movies.")
else:
    print("You can only watch G movies.")
