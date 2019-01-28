#!/usr/bin/env python3

s1 = "%to,two,too"

########
# Strip various characters from the the string
# NOTE this applies to only LEADING and TRAILING characters
##########

s2 = s1.strip('%!')  #Strip just the % and ! Characters
s3 = s1.strip(",")   #Strip only the comma

print("s1:",s1)
print("s2:",s2)
print("s3:",s3) # the commas are inside the string so it doesn't find them!

s4 = ",,,,,,,,anot,,erstring,,,,,,,,,,,,,,,"
s5 = s4.strip(',')
print("s4:",s4)
print("s5:",s5)

s6 = "     Leading spaces at the beginning and the end         "
s7 = s6.strip(' ')
print("s6:",s6)
print("s7:",s7) # now there are no leading spaces at the beginning and end
