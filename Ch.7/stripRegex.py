import re

def strip(string, a=''):

    if a != '':
        return re.sub(a, '', string)
    else:
        return re.sub(r'\s', '', string)


print(strip("abcdabcabcd", "abcd"))
print(strip("    111abc111      "))