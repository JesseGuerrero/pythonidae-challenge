import re

long_text = "123 56789 013"
reg = "((( )|(^))\d{3}(( )|($)))"

# looping regex exp
i = 0
nums = []
while(True):
    long_text = long_text[i:]
    num = re.search(reg, long_text)
    if num is None:
        break
    else:
        nums.append(num)
        i = num.span()[1]


if len(nums) == 0:
    print("No num found in string")
else:
    print("Nums in string are:")
    for num in nums:
        print("  -" + num.group().strip(" "))