import re

'''
Super basic example, attributes are separated by spaces...
'''

long_text = """
<html>
  <head>
  </head>
  <body>
    <a href='google.com'>link</a>
    <img src="example.jpg" alt="example" width="104" height="142">
    <p align='left'>This is a paragraph</p>
  </body>
  <footer>
  </footer>
</html>"""
reg = "(?<=<)([^>]{0,})(?=>)"

#This can be upgraded to have some more scalable attribute seperation
def getAttr(tag : re.Match)->list:
    return tag.group().split(" ")

i = 0
nums = []
tags = []
while(True):
    long_text = long_text[i:]
    tag = re.search(reg, long_text)
    if tag is None:
        break
    else:
        if "/" not in tag.group():
            tags.append(tag)
        i = tag.span()[1]

if len(tags) == 0:
    print("No tags found in string")
else:
    print("Tags & attribute in string are:")
    for tag in tags:
        tag = getAttr(tag)
        tagPrinted = False
        for attribute in tag:
            if tagPrinted:
                print("   " + attribute)
            else:
                print("Tag: " + attribute)
                tagPrinted = True
        print("---")