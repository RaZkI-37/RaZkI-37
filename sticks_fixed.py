sticks = 0
while sticks <= 0:
    sticks = int(input("How many sticks? "))
user1 = input("Player one? " )
players = 0
while players < 1 or players > 2:
    players = int(input("how many players? "))
if players == 2:
    user2 = input("Player two? ")
else:
    user2 = "CPU"
if players == 1:
    print("Opponent:",user2)
print("sticks:", sticks)
turn = ""
while turn == "":
    t = input((str(user1)) + ", Are you first? y/n " )
    if t == "y":
        turn = True
    elif t == "n":
        turn = False
import random
while sticks > 0:
    if turn == True:
        print(user1 + ",","it is your turn")
    elif turn == False:
        print(user2 + ",","it is your turn")
    if turn == True:
        loss = int(input("1, 2, or 3 sticks? "))
        if sticks <= 3 and sticks > 0:
            if sticks - loss < 0:
                print("try again")
                print("sticks left: ", sticks)
            elif loss > 3 or loss < 1:
                print("try again")
                print("sticks left: ", sticks)
            elif sticks == 2 and loss == 2:
                print("cannot lose on purpose.")
                print("sticks left: ", sticks)
            elif sticks == 3 and loss == 3:
                print("cannot lose on purpose")
                print("sticks left: ", sticks)
            elif loss == 0:
                print("try again")
                print("sticks left: ", sticks)
            else:
                sticks = sticks - loss
                print("sticks left: ", sticks)
                turn = False
        elif loss >=1 and loss <= 3:
            sticks = sticks - loss
            print("sticks left: ", sticks)
            turn = False
        else:
            print("try again")
    elif turn == False and players == 2:
        loss = int(input("1, 2, or 3 sticks? "))
        if sticks <= 3 and sticks > 0:
            if sticks - loss < 0:
                print("try again")
                print("sticks left: ", sticks)
            elif loss > 3 or loss < 1:
                print("try again")
                print("sticks left: ", sticks)
            elif sticks == 2 and loss == 2:
                print("cannot lose on purpose.")
                print("sticks left: ", sticks)
            elif sticks == 3 and loss == 3:
                print("cannot lose on purpose")
                print("sticks left: ", sticks)
            elif loss == 0:
                print("try again")
                print("sticks left: ", sticks)
            else:
                sticks = sticks - loss
                print("sticks left: ", sticks)
                turn = True
        elif loss >=1 and loss <= 3:
            sticks = sticks - loss
            print("sticks left: ", sticks)
            turn = True
        else:
            print("try again")
    elif turn == False and players == 1:
        if sticks % 4 == 0:
            loss = 3
        elif sticks % 4 == 3:
            loss = 2
        elif sticks % 4 == 2:
            loss = 1
        elif sticks == 1:
            sticks = 0
            turn = True
            break
        else:
            loss = random.randint(1, 3)
        sticks = sticks - loss
        print("sticks traken: ",loss)
        print("sticks left: ", sticks)
        turn = True
if sticks == 0 and turn == True:
    print(user1, "is the winner!")
elif sticks == 0 and turn == False:
    print(user2, "is the winner!")

