phone = input("phone:")
numbers = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five"
}
output = ""
for i in numbers:
    if phone in numbers:
        output += numbers.get(i, "!")
print(output)
#not working well tomorrow's problem