#Guess the number Game(while loop)
randN = 3
while True:
    userGuess = int(input("Enter number to guess"))
    if userGuess == randN:
        print("Hoorah! You Guessed the Number")
        break
    else:
        if userGuess < randN:
            print("Too low")
        else:
            print("Too High")
    