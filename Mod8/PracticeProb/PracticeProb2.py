'''
#2. Write a Python program that allows users to log their hiking trips.
The program should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

while True:
    hike_name = input("Enter a hike name: ")
    if hike_name == "0":
        break
    hike_distance = input("Enter the distance of the hike: ")
    if hike_distance == "0":
        break
    with open("hiking_log.txt", "a") as file:
        file.write(hike_name)
        file.write("\t")
        file.write(hike_distance)
        file.write("\n")

file = open("hiking_log.txt", "r")
for line in file:
        print(line.strip())
file.close()
