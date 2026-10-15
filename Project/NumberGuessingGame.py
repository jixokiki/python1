import random
import math

#Taking Inputs
lower = int(input("Enter Lower Bound : - "))

#Taking Inputs
upper = int(input("Enter Upper Bound : - "))

#generating random number between
#the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")

#Initializing the number of guesses.
count = 0

#for calculating of minimum number of guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1

    #taking guessing number as input
    guess = int(input("Guess a number : - "))

    #Condition testing
    if x == guess:
        print("Congratulations you did it in ", count, " try")

        #Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x > guess:
        print("You guessed too high!")

#If Guessing is more than required guesses, shows this output
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next Time!")