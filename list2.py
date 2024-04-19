list = [2,56,7,8,56,4,7,3,5,67,9]
duplicate_numbers =0
duplicate = []
for i in list:
    if i not in duplicate:
        duplicate.append(i)
print(duplicate)
