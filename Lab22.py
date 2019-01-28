#!/usr/bin/env python3

phone_dict = {
    'Don Hill': ['1112221111', 'IN'],
    'Amy Allen': ['1113331111', 'IL'],
    'Dan Martin': ['1114441111', 'NJ'],
    'Eric Forbes': ['1115551111', 'FL'],
    'Victoria Hill': ['1117771111', 'IN'],

}

print()
print("The Phone Directory")
print(phone_dict)

for full_name, phone_info in phone_dict.items():
    print("The phone numer for", full_name, "is", phone_info[0])
    print("the Phone location is", phone_info[1])
    print()

mykey = "Eric Forbes" #This is a match in the phone dictionary
#mykey = "d hill" #This is not a match in the phone dictionary
myvalue = phone_dict.get(mykey)

if myvalue:  #if my value is not None (the value, mykey, was found in the dictionary
    print("The phone number for ",mykey, "is",phone_dict[mykey][0])
    print("The state for", mykey, "is", phone_dict[mykey][1])
    print ()
else:
    print(mykey,'not in the phone directory')

#k = "victoria hill"
#k - "Don Hill"
k = "Amy Allen"

if k in phone_dict.keys():
    print(k,'has the phone number',phone_dict[k][0])
else:
    print(k,'not in the phone dictionary')




