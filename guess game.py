import random
while True:
    jackpot = random.randint(1, 100)

    for counter in range(1, 101):
        guess = int(input("guess the number: "))
        if guess < jackpot:
            print("too low,try again")
        elif guess > jackpot:
            print("too high,try again")
        else:
            print("you guessed it!")
            print("it took you", counter, "tries")
            break
    

    again = str(input("do you want to go again? (y/n): "))
    if again.lower() == "y":
        continue
    elif again == "N" or again == "n":
        print("aww i thought you were having fun, but ok")
        break
    else:
        print("invalid input, exiting the game")
        break
