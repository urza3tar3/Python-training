try:
    name = int(input("enter a number: "))
    print(name)
except SyntaxError:
    print("invalid")
except ValueError:
    print("invalid")
    
