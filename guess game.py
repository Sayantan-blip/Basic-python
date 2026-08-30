import random

while True:
    jackpot = random.randint(1, 10)

    for counter in range(1, 20):
        guess = int(input("guess the number: "))
        if guess < jackpot:
            print("too low,try again")
        elif guess > jackpot:
            print("too high,try again")
        else:
            print("you guessed it!")
            print("it took you", counter, "tries")
            break
    else:
        print("you ran out of tries!")

    again = str(input("do you want to go again? (y/n): "))
    if again == "N" or again == "n":
        print("aww i thought you were having fun, but ok")
        break
