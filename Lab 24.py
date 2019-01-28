#!/usr/bin/env python3

########
# Prompt the user to enter their age.
####

myage = int(input('Enter your age:'))

if myage < 13:
    print("Wow! You can still buy a kids meal!!")
elif myage >= 13 and myage < 20:
    print("Wow your a teenage Enjoy those french fries")

elif myage >= 20 and myage < 24:
    print("Get a job you bum!!")

elif myage > 64:
    print("Congrats no go retire!!")

else:
    # Calculate how many years the user has to work!
    i = 65 - myage
    print("Sorry! you have to work",i, "more years before retiring.")


# Outside of the IF-ELSE block

