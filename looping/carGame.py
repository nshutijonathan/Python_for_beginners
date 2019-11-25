command = ""
started = False
stopped = False
quit = False
while True:
    command = input(">").lower()
    if command == "help":
        print("""write start to start a car
         write stop to stop a car
         write quit to exit""")
    elif command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("car started ")
    elif command == "stop":
        if stopped:
            print("car has already stopped")
        else:
            stopped = True
            print("car stopped ")
    elif command == "quit":
        if quit:
            print("terminated alreadye")
        else:
            quit = True
            break
    else:
        print("I don't understand the command")
