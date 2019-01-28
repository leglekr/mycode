#!/usr/bin/env python3

s1 = "%to,two,too!"
print(s1)

#This illustrates more string slicing

#This shows the first character in the string
print(s1[0])

#This shows the last character in the string
print(s1[-1])

#This gets the first three characters in the string
#This includes indexes 0 to 2. It does not include index 3
print(s1[:3])

#This starts at index 7 and goes to the end of the string
print(s1[7:]) #This should print out the string ',too!'

# This starts at index 3 and goes to index 7 (does NOT include index 8)
print(s1[3:8]) # This should print out the string ',two,'