def baseline(command):

    if command == 'start':
        print("Car started.")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""
            start - start the car
            stop - stop the car
            quit - exit the application
        """)
    else:
        print("Command not found. Retry...")

while True:
    command = input("> ").lower()
    if command == "exit":
        print('Goodbye!')
        break
    else:
        baseline(command)
