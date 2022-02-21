'''
This was one of those challenging ones.
There were a few ways I could have done this...
The hard way would have been to recreate my own Regex
This would have been excessive menial work.
In the remarks it mentioned regex so I had decided to
create all possibilities and regex only the relavent ones.
This way you can get your list of a regex that's already
created. In addition I found 3rd party libraries that already
do this challenge.

However, as I implented this I found the longer the questioned string
the longer the brute force list is exponenitally. This meant only 1-4
characters are allowed to be generated without taking a lot of RAM.
'''

R = 'p[aA@4]\d'

import string
from itertools import product
import regex as re

def removeSyntax(stringArg : str):
    stringArg = list(stringArg)
    while '[' in stringArg:
        start_index = stringArg.index('[')
        end_index = stringArg.index(']')
        del stringArg[start_index:end_index]
    while '{' in stringArg:
        start_index = stringArg.index('{')
        end_index = stringArg.index('}')
        del stringArg[start_index:end_index]
    stringArg = "".join(stringArg)
    return stringArg.replace("\\", "")

alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

brute_force_List = list(map(''.join, product(alphabet, repeat=len(removeSyntax(R)))))
R = '(^'+R+'$)'
regex = re.compile(R)

answer_list = []
for word in brute_force_List:
    if regex.match(word):
        answer_list.append(word)
print(answer_list)
