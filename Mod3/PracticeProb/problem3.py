'''
3. Prompt the user for a sentence and a word to try
to find in that sentence. Have the program print out
whether the word was found in the sentence.
(i.e. True or False)
'''

str1 = input("Type in a sentence: ")
wrd1 = input("Type in a word to search for: ")
bool = str(wrd1 in str1)
print("Is the word '" + wrd1 + "' found in the given sentence? " + bool)
