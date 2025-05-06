'''
5. A store charges $5 for shipping on any order under $50.
If the order amount is $50 or more, shipping is free.
Ask the user for the order total and print the total cost,
including shipping.
'''

cost = float(input("Please enter the order total: "))

if (cost < 50):
    cost = (cost+5)
    print(f"Your cost including shipping: {cost:.2f}")
else:
    print(f"You get free shipping! Total cost is: {cost:.2f}")
