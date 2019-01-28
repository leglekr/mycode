#!/usr/bin/env python3

########
# Calculating Fibonacci numbers
# this is a famous mathamatical series.
#
# 1 1 2 3 58 13 21 34
#
# The first two nubers in the series are 1
# The third number is assigned the sum of the previous two numbers
##############


########
# Note that the function returns the value of a
# This is the last number displayed, as "new a value = "b"
#
# If changed to b, then it displays the "new b value, a+b"
###########

def fib(n):
    a,b = 0,1
    while b <n:
        print(b,end="")
        a,b=b,a+b  ## See the meaning below!!
    print()     # print an empty line
    return a     # Return the last number displayed

##########
#MEANING of 'a,b=,a+b'
####

# Call the function, to display the Fibonacci numbers less then 100
x = fib(100)
print("The fibonacci numbers that is less then 100.....",x)
print ()

# Call the function, to display the Fibonacci numbers less then 500
x = fib(500)
print("The Fibonacci numbers that is les then 500...",x)
print()

#Call the function, to display the Fibonacci numbers less than 2000
x = fib(2000)
print("The Fibonacci numbers that is less than 2000..",x)
