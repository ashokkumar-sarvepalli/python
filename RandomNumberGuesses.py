import random
guessesTaken = 1
print("Hello! What's your name?")
myName = input()
number = random.randint(1,100)
print(myName + " , Guess a number between 1 and 100.")
guess = int(input())

while guess != number:
   
    guessesTaken = guessesTaken + 1
    if guess < number:
        print("Your guess of:",guess," is too low")

    if guess > number:
        print("Your guess of:",guess," is too high")


    if guess == number:
        break
    guess = input()
    guess = int(guess)
    
print("The random number was: " ,number)
print ("The number of guesses taken is:" , guessesTaken)
print(guess)
