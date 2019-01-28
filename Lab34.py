#!/usr/bin/env python3

########
# Calculating Fibonacci numbers
# this is a famous mathamatical series.
#
# 1 1 2 3 58 13 21 34
#
# The first two nubers in the series are 1
##############

######
# The traditional way to program the fibonacci series
########

def trad_fib(n):
    a = 1  # The first number in the series
    b = 1  # The second number in the series

    while b < n:
        print(a, end="")
        old_b = b  # Keep the original value of b
        b = a + b  # The new value of b
        a = old_b  # the new value of a

    print(a, end="")
    print()
    return a

# Call the function, to display the Fibonacci numbers less then 400
x = trad_fib(400)
print ("The Fibonacci number that is less then 400....",x)

print()

# call the function, to display the Fibonacci numbers less than 2000
x = trad_fib(2000)
print("The Fibonacci numbers that is less than 2000..",x)

