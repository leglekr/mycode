#!/usr/bin/env python3

#####
# Function name: get_uer_age
# This prompts the user for the age
########

def get_user_age():
    #Initialize your prompt sting
    prompt_age_msg = "Please enter your age:"

    #########
    ## Prompt the user for their age
    #######
    user_str = input(prompt_age_msg)


    # The string function isdigit returns TRUE if all digits are numeric
    if(user_str.isdigit()):
        user_age = int(user_str)
    else:
        #If they entered a string value, then set the age to 0
        #This will eventually flag our error condition
        user_age = 0
    print (user_age)
    #Returns user_age
    return user_age

#END of the function get_user_age

#########
# Function Name: print_age_output
# Input Value: myage
# This will print out a message, based on the user's age
######

#Pricess the user's age
def print_age_output(myage):
    if myage <13:
        print ("Wow you can still buy a kid's meal!")
    elif myage >=13 and myage <20:
        print("Wow! You are a teenager! Get a job you hippie")
    elif myage >=20 and myage <24:
        print("Welcome to the wonderufl adult world, get me a kids meal!!!")
    elif myage >64:
        print("Congratulations! You are retirement age!")
    else:
        #Calcualte how many years the user has to work!
        i = 65 - myage
        print("Sorry! You have to work",i,"more years before retiring.")

###
# Get_user_name, enter q or Q to quit
##

def get_user_name():
    #Initalize your prompt string
    prompt_name_msg = "Please enter your name. Enter Q to quit:"
    user_name = input(prompt_name_msg)

    while (user_name.upper() !="Q"):
        if user_name.isnumeric():
            user_name = input(prompt_name_msg)
        elif user_name.count('-'):
            user_name = input(prompt_name_msg)
        elif user_name.upper()=="":
            user_name = input(prompt_name_msg)
        else:
            print("Now porcessing user name...",user_name)
            myage = get_user_age()

        while (myage <=0):
            myage = get_user_age()

        print_age_output(myage)
        print()

        user_name = input(prompt_name_msg)
        print()

my_user_name = get_user_name()
