#!usr/bin/env python3

# This program requests user input and then processes that text input to generate a nickname
# Nickname is based on the first character and last character of the name inputted

import time     # this imports the time function so that we can do things like create pauses in the program 'sleep()'
from operator import itemgetter

nicknames = ['Troublenator', 'Code Master', 'Delightful Debugger', 'Python Prime', 'Super Scripter',
             'Bash Boss', 'Viceroy of Variables', 'Ambassador of Automation', 'Infinite Loop']

print("Hello, and welcome to NICKNAME.GENERATOR.3000")
time.sleep(1)
print("Tell us your first name and we'll create your coding superhero nickname!")
time.sleep(1)
print('...now loading')
time.sleep(1)
print()
print('Please input your first name, using A-z characters only:')
name = str(input())

print()
print('...processing...')
time.sleep(2)
print('...you are...')
time.sleep(2)

def getOrd():
    firstLetter = (name[0])
    lastLetter = (name[-1])
    # print(ord(firstLetter))
    # print(ord(lastLetter))
    combo = ord(firstLetter) + ord(lastLetter)
    #print(combo)
    initials = [int(d) for d in str(combo)]
    #print(initials)
    x = int(sum(initials))
    # print(x)
    while x > 10:
        x = [int(d) for d in str(x)]
        x = int(sum(x))
        x = x - 1           # since we only have 9 nicknames, we don't want to exceed 9 in our final number
    while x > 8:
        x = x - 1           # since a result of 10 may have skipped our WHILE loop, we're ensuring it's 8 or less here
    # print(x)


    ##################################
    # We now have a guaranteed integer between 2 and 9, a total of 9 possible results (matching our # of nicknames)
    ##################################
    print()
    result = itemgetter(x)(nicknames)
    print("The", result+"!")


getOrd()

