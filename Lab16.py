#!/usr/bin/env python3

########
#cels_list is the LIST of the Celsius temperature
#fahr_list is the LIST of Fahrenheit temperatures
#####

cels_list = [-2,0,5,10,15,25,32,38,40]
fahr_list = [] #Empty list

######
#Use a FOR look to access each item in the list and find the cooresponding F temp
#Append it to the fahr_list
#####

for c in cels_list:
    f_temp = c * 1.8 +32.0
    fahr_list.append(f_temp)

print("The Celsius list:",cels_list)
print("The Fahrenheit list:", fahr_list)
print ()

####
# pop is a mothod to remove an item from a list
#Save the popped item as myItem.
###
myItem=cels_list.pop()
print("The item popped from the list is ",myItem)
print()

print("After popping one item from the pop_list...")
print("The Celsius list:',cels_list",cels_list)


