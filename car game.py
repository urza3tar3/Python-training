cmd = ""
while cmd.lower() != "quit":
        cmd = input(">")
        if cmd.lower() == 'help':
            print('''
        start = to start the car
        stop - to stop the car
        quit - to exit''')
        if cmd.lower() == 'start':
            print("car has started, ready to go!")
        elif cmd.lower() == "stop":
            print("car has stopped")

        elif cmd.lower() == "quit":
            break
        else:
            ("invalid input command")