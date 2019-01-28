#!/usr/bin/env python3
# a_list is the original list

a_list=[1,2,3,4]
print("The original list...")
print(a_list)
print()   #This simply prints an empty line (more below)


#Print out the elements in the original list

print("Item 1 in the list is:",a_list[0])  #Stored at index 0
print("Item 2 in the list is:",a_list[1])  #Stored at index 1
print("Item 3 in the list is:",a_list[2])  #Stored at index 2
print("Item 4 in the list is:",a_list[3])  #Stored at index 3

print()

###Reverse the list##

reversed_list=a_list[-1::-1]
print("The reversed list...")
print(reversed_list)
print()

print("Now using the FOR loop to maneuver the entire list")
for x in reversed_list:   #Name the variable anything you want
    print(x,"",end="")



