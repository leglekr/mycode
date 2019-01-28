#!/usr/bin/env python3

# initialize your prompt screen
prompt_name_msg = "Please enter your full name:"

##use the imput function to get the users name
user_name = input(prompt_name_msg)

##Check the user name is not empty
while (user_name == ''):  # either use two single quotes or two double quotes

    ######prompt user again for name
    user_name = input(prompt_name_msg)

print()
print("Welcome to the wonderful wolrd of Python, ", user_name)
print()
f