from secret_number import secretNum

guess_count = 0

while True:
    guess = int(input("Guess a number: "))
    guess_count += 1
    
    if guess < secretNum:
        print("Too low!")
    elif guess > secretNum:
        print("Too high!")
    else:
        print("You guessed it right!")
        break
    if guess_count >= 5:
        while True:
            print("Oh! Noooooo...")
            

