import random
while True:
    guess = int(input("Enter a number 1-10: "))
    if(random(10,1) == guess):
        print("You Made it")
    else:
        print("Better luck next time")

