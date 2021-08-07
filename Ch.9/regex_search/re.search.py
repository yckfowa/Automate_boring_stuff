"""
open all the txt.file in the directory and searching for matches through regex, then display the results
"""
import os
import re

folder = os.listdir(os.getcwd()) # change to your own path 
txt_files = []


#find files that are ending with .txt
txt_regex = re.compile(r'.txt$')

for file in folder:
    if txt_regex.search(file) is not None:
        txt_files.append(file)


search_input = input("Enter your search term:")
search_regex = re.compile(search_input)

# print the found word and from which txt.
for file in txt_files:
    open_file = open(file)
    contents = open_file.read()
    found = search_regex.findall(contents) # findall return all matched string in list
    found_str = ' '.join(found)
    if found_str:
        print(found_str, file.ljust(len(file)))
    else:
        print("Not Found", file.ljust(len(file)))