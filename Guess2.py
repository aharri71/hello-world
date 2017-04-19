import random

guessesTaken=0

print("Hello, what's your name?")
myname=input()

number=random.randint(0,20)
print("Well, " + myname + ", Can you guess my number between 0 and 20 in six turns or less?")

while guessesTaken<6:
    print("Take a guess.")
    guess=int(input())

    guessesTaken=guessesTaken + 1

    if guess < number:
        print("Too low! Try again.")

    if guess > number:
        print("Too high! Try again.")

    if guess == number:
        break

if guess == number:
    guessesTaken=str(guessesTaken)
    print("You guessed my number! Great job!")

if guess != number:
    number = str(number)
    print("Nope! The number I was thinking of was " + number)
