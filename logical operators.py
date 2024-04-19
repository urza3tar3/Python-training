name = input("what's your name?")
name_length = len(name)
if name_length >= 3 and name_length <= 50:
    print("name looks good!")
else:
    print("invalid name, must be less than 50 and longer that 3")