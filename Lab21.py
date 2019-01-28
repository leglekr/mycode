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
