'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to
other types. For example, water is very effective to fight fire.
Write a function called type_advantage(attacker, defender) that takes
two Pokémon types as strings and returns "Super Effective",
"Not Very Effective", or "Neutral" based on simple type effectiveness
rules. Your solution only needs to work for these three sets of input:

print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not Very Effective"
print(type_advantage("Electric", "Grass")) # "Neutral"
'''

def type_advantage(attacker, defender):
    if attacker == "water" and defender == "fire":
        return "Super Effective"
    elif attacker == "fire" and defender == "water":
        return "Not Very Effective"
    elif attacker == "water" and defender == "water":
        return "Neutral"
    elif attacker == "fire" and defender == "fire":
        return "Neutral"
    elif attacker == "fire" and defender == "grass":
        return "Super Effective"
    elif attacker == "grass" and defender == "fire":
        return "Not Very Effective"
    elif attacker == "grass" and defender == "water":
        return "Super Effective"
    elif attacker == "water" and defender == "grass":
        return "Not Very Effective"
    elif attacker == "grass" and defender == "grass":
        return "Neutral"
    elif attacker == "electric" and defender == "grass":
        return "Neutral"
    else:
        return "Please enter valid pokemon types"

print("Available types are fire, water, grass, and electric.")
attacker1 = input("Please enter an attacker pokemon type: ")
defender1 = input("Please enter a defender pokemon type: ")

print(type_advantage(attacker1.lower(),defender1.lower()))
