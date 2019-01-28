#!/usr/bin/env python3

####
#a_list is the ORIGINAL LIST
####

a_list=[1,2,3,4]

print("The original list...")
print(a_list)
print ()   #This simply prints an empty line

#############
#Use the FOR loop, with enumerate to navigate the entire list
############

for i, item in enumerate(a_list):
    a_list[i]=100    #this changes the value in the list
    #end FOR Loop

    # print the list, should now be 100

print(a_list)
