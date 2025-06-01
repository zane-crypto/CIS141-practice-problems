'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
by commas. Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.
'''

import string
translator = str.maketrans('', '', string.punctuation)
votes = {'yea': 0, 'nay': 0}

with open("poll.txt", "r") as poll:
    poll_str = poll.read()
    clean_text = poll_str.translate(translator)
    word_count = clean_text.strip().split()

for vote in word_count:
    if vote == 'yea':
        votes['yea'] += 1
    elif vote == 'nay':
        votes['nay'] +=1

print(votes)
