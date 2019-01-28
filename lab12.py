#!/user/bin/env python3

global prompt_age_msg
prompt_age_msg = "Please enter your age: "

# Function name: get_user_age
def get_user_age():
    #Prompt string has been changed to a global variable
    # initalize your prompt screen
    ## prompt_age_msg = "Please enter your age"

    ##Prompt user for age, will convert string value to an integer value

    user_str = input(prompt_age_msg)

    if (user_str.isdigit()):
        user_age = int(user_str)
    else:
        ##if they entered a sting value, then set the age to 0
        ##this will eventually flag our error condition
        user_age = 0

        # Returns the users age
    return user_age


#########
# Begin the main program
#########

# Call the function, get user age
my_user_age = get_user_age()

############
# Error Checking
##########

while (my_user_age <= 0):
       prompt_age_msg = "Wrong format entered. Enter an integer value for your age!!!"
       my_user_age = get_user_age()

####
# Print out a statement using the user age variable
######
print()
print("Your age is:", my_user_age, "Years Old")
print()
