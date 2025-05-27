'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.
'''

def ferry_fare(age, vehicle):
    if age >= 19 and age <= 64 and vehicle == True:
        return "$20"
    elif age >= 19 and age <= 64:
        return "$10"
    elif age >= 65 and vehicle == True:
        return "$15"
    elif age >= 65:
        return "$5"

def yes_no_question(question):
    while True:
        answer = input(question + " (yes/no): ").lower()
        if answer in ["yes", "no"]:
            true_false = {
                "yes": True,
                "no": False
            }
            return true_false[answer]
        else:
            print("Please answer 'yes' or 'no'.")

age1 = int(input("How old are you: "))
if age1 > 18:
    has_car = "Do you have a car?"
    print("Your fare is", ferry_fare(age1, yes_no_question(has_car)))
else:
    print("Your fare is free!")
    
