import random
jackpot = random.randint(1,100)

guess = int(input("guess the number: "))
counter=1

while guess != jackpot:
    if guess < jackpot:
        print("too low,try again")
    else:
        print("too high,try again")
    guess = int(input("guess the number: "))
    counter += 1
    
print("you guessed it!")
print("it took you", counter,"tries")
        
        

    
            
