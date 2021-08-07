"""
Mad libs program that replace the sentences with the new user inputs in the test.txt file
"""

import re

f = open("Madlibs/test.txt") # change to your own path 
sentence = f.read()
f.close()
regex = re.compile(r'ADJECTIVE|NOUN|VERB')

while True:
    match = regex.search(sentence)
    if match is None:
        break
    elif match.group() == "ADJECTIVE":
        print('Enter an adjective: ')
    elif match.group() == "NOUN":
        print('Enter an noun: ')
    elif match.group() == "VERB":
        print('Enter an verb: ')

    word = input()
    sentence = sentence.replace(match.group(), word, 1)

newFile = open("Madlibs/newMadlib.txt", "w") # change to your own path 
newFile.write(sentence)
newFile.close()
