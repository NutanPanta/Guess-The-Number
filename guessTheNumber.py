import random

guessNumber = random.randrange(0, 21)
print(guessNumber)

guessedNumber = int(input("Enter Your Guess Number: "))
range = abs(guessNumber - guessedNumber)

if guessNumber == guessedNumber:
    print("Your Guess is correct.")

elif guessedNumber > 20:
    print(guessNumber)
    guessedNumber = int(input("The number is greater than 20. Please enter a number between 1 and 20,\nEnter Your Guess Number: "))
    if guessNumber == guessedNumber:
        print("Your Guess is correct.")
    elif range <= 3 | range >= 3:
        print("You were very close, just within the range. Better luck next time.")
    else:
        print("Your guessed number if below the actual number. Try again")

elif guessedNumber < 0:
    print(guessNumber)
    guessedNumber = int(input("The number is less than 0. Please enter a number between 1 and 20,\nEnter Your Guess Number: "))
    if guessNumber == guessedNumber:
        print("Your Guess is correct.")
    elif range <= 3 | range >= 3:
        print("You were very close, just within the range. Better luck next time.")
    else:
        print("Your guessed number if below the actual number. Try again")

elif range <= 3 | range >= 3:
    print("You were very close, just within the range. Better luck next time.")

else:
    print("Your guessed number if below the actual number. Try again")
