secretNumber = 9
guessLimit = 3
guessCount = 0
while guessCount < guessLimit:
    guess = int(input("enter your guess"))
    guessCount += 1
    if guess == secretNumber:
        print("You won")
        break
else:
    print("sorry you have failed")
