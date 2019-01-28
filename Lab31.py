#!/usr/bin/env python3

# Import the operating system module
import os

#open the input file for reading
in_file = open('infile_001.txt','r')

#Count the number of lines in the file
line_count = 0

#######
# Loop though each line in the input file.. print out the file
########
for a_line in in_file:       #Using the OS module eliminates having to execute a read line
    print(a_line,end="")   #Using the end parameter, extra line feeds not added
    line_count +=1  #This is the same as line_count = line_count

###
#Important! Don't forget to Close the file
###
in_file.close()

print()
print("The number of lines contained in this file were: ",line_count)
print()

############
#This is just demonstrating another way to increment a counter variable
# .. Other languages typically do something like "i=i+1"
#tmp_lc is a "temporary" line count
############
tmp_lc = line_count
tmp_lc = tmp_lc + 1  # This is the typical way other programming languages increment, here it just added a line
print ("The value of the variable tmp_lc:",tmp_lc)