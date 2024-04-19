#for x in range(4):
    #for y in range(3):
        #print(f"({x},{y})")
numbers = [2,2,2,2,5]
for number in numbers:
    print("x"*number)
for number in numbers:
    output = ""
    for number in range(numbers):
        output += "x"
    print(output)
