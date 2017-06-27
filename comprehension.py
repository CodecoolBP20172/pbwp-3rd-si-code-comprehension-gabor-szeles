# The program asks the user's name, then assigns a random number, which the user has to guess in 6 tries.
import random  # import the module called random

guessesTaken = 0  # assign 0 to a variable counting the user's guesses

print('Hello! What is your name?')  # prints a message
myName = input()  # assigns the input value to a variable

number = random.randint(1, 20)  # assigns a random integer (using the random module) between 1 and 20 to the variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # prints a message with a reference to a variable

while guessesTaken < 6:  # initiates a while loop with a condition
    print('Take a guess.')  # prints yet another message
    guess = input()  # assigns input value to a variable
    guess = int(guess)  # casts the previously assigned variable into an integer and assigns it back to the variable

    guessesTaken += 1  # adds one to the value of the variable

    if guess < number:  # sets an if statement with a boolean expression (if the value of guess is lower than the value of number)
        print('Your guess is too low.')  # prints a message if the previous expression is True

    if guess > number:  # sets an if statement with a boolean expression (if the value of guess is higher than the value of number)
        print('Your guess is too high.')  # prints a message if the previous expression is True

    if guess == number:  # sets an if statement with a boolean expression (the value of guess is the value of number)
        break  # breaks the while loop if the previous expression is true

if guess == number:  # sets an if statement with a boolean expression ( the value of guess is the value of number)
    guessesTaken = str(guessesTaken)  # casts the value of the variable into string and assigns it back to the same variable
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # prints a "victory message" referencing two variables

if guess != number:  # sets an if statement with a boolean expression ( the value of guess is not the value of number)
    number = str(number)  # casts the value of the variable into string and assigns it back to the same variable
    print('Nope. The number I was thinking of was ' + number)  # prints a "game over message" referencing the previous variable
