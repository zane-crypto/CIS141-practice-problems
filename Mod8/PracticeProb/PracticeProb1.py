'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to
it. Write a Python script that reads a file gardening_tips.txt and prints
out each tip one by one.
'''
def read_line(file, mode):
    with open(file, mode) as file2:
        for lines in file2:
            print(lines.strip())
            input("Press enter to continue...")

def write_to_file(file, mode):
    with open(file, mode) as file1:
        count = 0
        while count < 3:
            file1.write(input("Enter a gardening tip: "))
            file1.write("\n")
            count += 1

write_to_file("gardening_tips.txt", "a")

read_line("gardening_tips.txt", "r")
