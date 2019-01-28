#!/usr/bin/env python3

import os

file_name=input("Please eneter a file name to read from:")

while not os.path.exists(file_name):
    print("The Following file does not exist:",file_name)
    file_name = input("Please enter a file name to read from:")

print("This input file exists:",file_name)

#open the input file for reading
in_file = open(file_name, 'r')

#Count the number of lines in the file
line_count = 0

##########
#Loop through each line in the input file ... print out the file
#######

for a_line in in_file:
    print(a_line,end='')  #using the end parameter, extra line feeds not added
    line_count +=1   #this is the same as line_count = line_count +1

    #####
    ## IMPORTANT! Don't forget to close the file
    ####

in_file.close()
