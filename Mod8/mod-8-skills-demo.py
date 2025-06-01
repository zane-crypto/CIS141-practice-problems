'''
Create a new file called mod-8-skills-demo.py. This is the file you'll write your code in for your Skills Demonstration.

When you've set up your files, start recording:

In your mod-8-skills-demo.py, import the shop module. Write function calls to demonstrate the following:

    Viewing the shop's inventory.
    Buying at least 2 different items.
    Restocking an item.
    Viewing the updated shop's inventory.

While writing your function calls:

    Trace the function calls back to the module, and describe how each function in the module works, emphasizing when dictionaries are being used to organize & retrieve data.
    Test your code to demonstrate that it is functional.
'''

import shop

print(shop.view_inventory())

shop.buy_item("Turnip Seeds", 5)
shop.buy_item("Tomato Seeds", 6)

print(shop.view_inventory())

shop.restock_item("Turnip Seeds", 5)
shop.restock_item("Tomato Seeds", 6)

print(shop.view_inventory())
