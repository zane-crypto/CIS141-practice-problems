'''
#5. Write a function called level_up(experience) that takes a player's experience
points and returns their new level based on these rules:
* 0-99 XP → Level 1
* 100-199 XP → Level 2
* 200+ XP → Level 3
'''

def level_up(experience):
    if experience <= 99:
        return "Level 1"
    elif experience >= 100 and experience <= 199:
        return "Level 2"
    elif experience >= 200:
        return "Level 3"

exp = int(input("Please enter amount of experience: "))

print(level_up(exp))
