#!/usr/bin/env python3

import os

outFile = open('admin.rc', 'a')             # this specifies the output filename we'll write to in this script

print("What is the OS_AUTH_URL?")
osAUTH = input()
print("export OS_AUTH_URL=", osAUTH, file=outFile)
print("export OS_IDENTITY_API_VERSION=3", file=outFile)

print()
print("What is the OS_PROJECT_NAME?")
osPROJ = input()
print("export OS_PROJECT_NAME=", osPROJ, file=outFile)

print()
print("What is the OS_PROJECT_DOMAIN_NAME?")
osPROJDOM = input()
print("export OS_PROJECT_DOMAIN_NAME=", osPROJDOM, file=outFile)

print()
print("What is the OS_USERNAME?")
osUSER = input()
print("export OS_USERNAME=", osUSER, file=outFile)

print()
print("What is the OS_USER_DOMAIN_NAME?")
osUSERDOM = input()
print("export OS_USER_DOMAIN_NAME=", osUSERDOM, file=outFile)

print()
print("What is the OS_PASSWORD?")
osPASS = input()
print("export OS_PASSWORD=", osPASS, file=outFile)

outFile.close()                             # remember to close the file

infile = open('admin.rc', 'r')              # now re-opening the file in read-only mode
data = infile.readlines()                   # reading all lines

print("Successfully written to file named 'admin.rc':")
for line in data:
    print(line)                             # printing each line from the file


infile.close()                              # close the file again since it was reopened
os.remove('admin.rc')                       # delete the file since we don't need it anymore

# if we didn't delete the file, each script run would add to the same file because we've specified
# the write mode as 'a' for append