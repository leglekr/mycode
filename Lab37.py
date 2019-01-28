#!/usr/bin/env python3
# Import the operating system module
import os

#Open the input file for reading
in_file = open('infile_002','r')
line_count = 0
total_glucose = 0
total_insulin_dose = 0

#############
# Read the input file.. it is stored in a list
######
sugar_levels_list = in_file.readlines()

print("====SUGAR LEVELS LIST below ===========")
print (sugar_levels_list)
print()

print("---First element in the SUGAR LEVELS LIST----")
print(sugar_levels_list[0])
print()

#########
# Loop through each line in the input file.. print out the file
##########
for a_line in sugar_levels_list:
    print(a_line,end='')  #Using the end parameter, extra line feeds not addded

# Save the glucose value at the end of this string, located at index 2
# The format is: DATE, TIME, GLUCOSE-VALUE, INSULIN-DOSE
tmp_list = a_line.split(',')
glucose_value = tmp_list[2]
insulin_dose = tmp_list[3]
print("...glucose value=",glucose_value)
total_glucose += int(glucose_value)
total_insulin_dose +=int(insulin_dose)
line_count+=1

print()
print("DONE READING THIS FILE...")
print(".....Total Glucose = ",total_glucose)
print("...Total Count =",line_count)
print("...Average Glucose =", total_glucose/line_count)
print("...Average Insulin Dose =", total_insulin_dose/line_count)

in_file.close()#IMPORTANT! do not forget to close the file
