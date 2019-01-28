#!/usr/bin/env python3

a=5
#b='6'
b= 6

#Try THIS! Compare what happens when line 5 is commented out, instead of line 4
c = a + b

#python lets you combine integers and floaring point numbers without any problem!
d=2.34
e=a+d

#Hexadecimal values initialized
f=0xB #Equivalent to decimal value of 11
g=0xF #Equivalent to decimal value 15
h=0x10 #Equivalent to decimal value of 16
i=f+g+h

print("a=",a)
print("b=",b)
print("c",c)
print("d=",d)
print("e=",e)
print("f=",f)
print("g=",g)
print("h=",h)
print("i=",i)


print('NOW printing in Hex Format')
print("f=",format(f,'02x'))  # This is in hex format
print("g=",format(g,'02x'))  # This is in hex format
print("h=",format(h,'02x'))  # This is in hex format
print("i=",format(i,'02x'))  # This is in hex format


