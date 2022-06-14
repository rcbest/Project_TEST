import random
exitChoice = "Nothing"
while exitChoice != "EXIT":
    print("You are in a dark room in a misterious castle.")
    print("In front of you are four doors. You mast choose one.")
    lose = "GAME OVER. YOU LOSE!"
    win = "game over, you win!"
    playerChoice = input("Choose 1, 2, 3 or 4...")
    if playerChoice == "1":
        print("You find a room full of treasure.\nYou're rich!")
        print(win.upper())
    elif playerChoice == "2":
        print("The door opens and an angry ogre hits you with his club")
        print(lose.title())
    elif playerChoice == "3":
        print("You go into the room and find slipping dragon.")
        print("You can either:\n\t1) Try to steal some of dragon's gold\n\t2) Try to sneak around the dragon to the exit.")
        dragonChoice = input("Type 1 or 2   ")
        if dragonChoice == "1":
            print("The dragon wakes up and eats you")
            print("GAME OVER. YOU LOSE!")
        elif dragonChoice == "2":
            print("You sneak around the dragon and escape the castle")
            print("GAME OVER, YOU WIN!")
    elif playerChoice == "4":
        print("You enter a room with a sphinx.")
        print("It ask you to guess what number it is thinking of, between 1 and 10")
        number = int(input("What number do you choose?  "))
        if number == random.randint(1,10):
            print("The sphinx hisses in disappointment. You gessed correctlly.")
            print("She must let you go free")
            print("GAME OVER, YOU WIN")
        else:
            print("The sphinx tells you that your guess is incorrect")
            print("GAME OVER, YOU LOSE")
    else:
        print("Sorry, you didn't enter 1, 2, 3 or 4")
    exitChoice = input("Press ENTER to play agane or EXIT to leave")
