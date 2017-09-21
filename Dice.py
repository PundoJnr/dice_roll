from random import *
b = input("Enter 1 to role dice: ")
if b == "1":
    die1 = randint(1,6)
    die2 = randint (1,6)
    x = (die1 + die2)
    print (x)
    if x > 5:
        print("You're doing great")
    else :
        print("oh! bad luck Try again")

else:
    print("invalid choice")


