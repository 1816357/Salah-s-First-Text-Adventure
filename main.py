
"""
def CheckInput(optionList):
    while True:
        user_input = input("Enter a number (1 - {}): ".format(len(optionList)))
        for item in optionList:
            if int(user_input) == item:
                return item
        print("Invalid entry", "\n")
"""

inventory = []

stats = {"Name": "John", "MaxHealth": 100, "Level": 1, "EXP": 0}
gameState = 0

while gameState == 0:
    stats['Name'] = user_input = input('Enter Player Name: ')
    print('your name is ' + user_input)

    print("You are stuck in a prison. You see a dimly lit corridor, it seems there's no hope of escape.")
    gameState = 1

while gameState == 1:
    user_input = input("What are you going to do?\n1. Look Around\n2. Yell\n3. Shake Bars\n4. Open Door\n")

    if user_input.lower() == "look around":
        print("You have found a rock")
        inventory.append("rock")
        stats["EXP"] += 15
    elif user_input.lower() == "yell":
        print("There is no response")
    elif user_input.lower() == "shake bars":
        print("The bars have collapsed")
        print("You collect a loose bar")
        gameState = 2
        stats["EXP"] += 15
        inventory.append("Bar")
    elif user_input.lower() == "open door":
        print("Nothing happens")
    else:
        print("sorry you can't do this")

while gameState == 2:
    print(stats["EXP"])
    user_input = input("You have escaped the prison cell and have entered the corridor, there are two doors. Which door do you enter \n1. Door 1\n2. Door 2\n")

    if user_input.lower() == "door 1":
        print("you've found another inmate")
        gameState = 3.1
    elif user_input.lower() == "door 2":
        print("you've found the ladder to the guard tower")
        gameState = 3.2
    else:
        print("sorry you can't do this")

while gameState == 3.1:
    user_input = input("The man is half-staved, shaking and terrified of you. He is in clear need of help but you're in a hurry to escape, what should you do?\n1. Help\n2. Leave Him\n")

    if user_input.lower() == "help":
        print("You try to free the man, and are unsuccessful. The bars are too tight.")
    elif user_input.lower() == "help" and "rock" in inventory:
        print("Using the rock break the bars of the inmates cell, and allow him to follow you on your escape.")
        print("The rock breaks. Sadness emanates from the shattered remains.")
        gameState = 4.1
    elif user_input.lower() == "leave him":
        print("You decided to not help the man and continue down the corridor to the exit")
        gameState = 4.2
    else:
        print("sorry you can't do this")

while gameState == -1:
    print("You have died. How sad.")
    break
