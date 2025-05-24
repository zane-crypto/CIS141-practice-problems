'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.
'''

def ferry_fare(age, vehicle):
    if vehicle == True:
        bool = True
    else:
        bool = False


    if age <= 18:
        return "Free"
    elif age >= 19 and age <= 64 and bool == True:
        return "$20"
    elif age >= 19 and age <= 64:
        return "$10"
    elif age >= 65 and bool == True:
        return "$15"
    elif age >= 65:
        return "$5"
    
    
age1 = int(input("Please enter your age: "))
bool1 = False
if age1 > 18:
    bool1 = bool(input("Enter 'Yes' if you have a car: "))

print("Your fare is", ferry_fare(age1, bool1))
