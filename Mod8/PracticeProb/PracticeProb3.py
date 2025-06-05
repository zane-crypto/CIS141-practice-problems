'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''

import string

word_list = []
word_count = {}
count = 0
punc = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + '"'

while count < 5:
        user_input = input("Please enter a word to count: ").lower()
        word_list.append(user_input)
        count += 1
        
with open("song_lyrics.txt", "r") as song:
    song_string = song.read()
    for c in punc:
        song_string= song_string.replace(c,"")
    song_list = song_string.lower().split()

    for word in song_list:
        if word in word_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
            
print(word_count)
