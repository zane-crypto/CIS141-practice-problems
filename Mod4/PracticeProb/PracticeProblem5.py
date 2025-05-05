'''
5. A store charges $5 for shipping on any order under $50.
If the order amount is $50 or more, shipping is free.
Ask the user for the order total and print the total cost,
including shipping.
'''

cost = int(input("Please enter the order total: "))

if (cost < 50):
    cost = (cost+5)
    print("Your cost including shipping ", cost)
else:
    print("You get free shipping! Total cost is : ", cost)
  
