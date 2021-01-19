print("Welcome to the TeslaAI. Input commands for your car. To see options type 'help'")
Command = ""
started = False
stopped = False
while True:
    Command = input("> ").lower()
    if Command == "start":
        if started:
            print("The car has already been started!")
        else:
            started = True
            print("The car engine ignition has started. Awaiting further command.")
    elif Command == "stop":
        if stopped:
            print("You already have stopped the car!")
        else:
            stopped = True
            print("The ignition was stopped. Awaiting further command.")
    elif Command == "help":
        print("""List of commands for your car are here:
        Start - To START the car.
        Stop - To STOP the car.
        Quit - To QUIT the car.
        """)
        #"""""" or '''''' can be used to write bigger and longer text in the code.
        #When entering new line after the first text the space is executed in the output as is.

    elif Command == "quit":
        break
    else:
        print("Sorry. We cannot understand you. Please try again.")