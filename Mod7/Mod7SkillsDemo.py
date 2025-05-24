#function that takes input and returns a formated string. note classs is intentionally misspelled as class is special in python.
def char_stats(name, classs, level, health):
    formatted_stats = f"{name} - Class: {classs}, Level: {level}, Health: {health}"
    return formatted_stats

#Uses list to pass data through function and then print warrior
warrior = ["Thorin", "Warrior", 10, 150]
formatted_stats = char_stats(warrior[0], warrior[1], warrior[2], warrior[3])
print(formatted_stats)

#Uses list to pass data through function and then print mage
mage = ["Merlin", "Mage", 12, 120]
formatted_stats = char_stats(mage[0], mage[1], mage[2], mage[3])
print(formatted_stats)

#Uses list to pass data through function and then print rogue
rogue = ["Ezio", "Rogue", 8, 100]
formatted_stats = char_stats(rogue[0], rogue[1], rogue[2], rogue[3])
print(formatted_stats)
