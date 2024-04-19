import math
list = [2,56,7,8,56,4,7,3,5,67,9]
print(max(list))
max = list[0]
for i in list:
    if i > max:
        max = i
print(max)