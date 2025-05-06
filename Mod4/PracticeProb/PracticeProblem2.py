'''
The headlights of a car should only automatically
turn on when the daylight outside is below a certain
threshold. If a sensor threshold is below the number
8, print "Headlights On"; otherwise,
print "Headlights Off".
'''

sensor = int(input("Please enter a number between 1 and 10: "))
if sensor < 8:
    print("The lights are on!")
else:
    print("The lights are off.")
