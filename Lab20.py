#!/usr/bin/env python3

#initialize two set objection, using curly brackets

chicago_zoo_set = {'Kangaroo', 'Leopard', 'Moose', 'Polar Bear', 'Bobcat'}
sandiego_zoo_set = {'Kangaroo', 'Lion','Grizzly Bear', 'Wildcat','Antelope'}

print()
print("SET OBJECTS...")
print('Chicago Zoo:', chicago_zoo_set)
print ('San Diego Zoo:', sandiego_zoo_set)
print()

print("COMMON animals to both the Chicago and San Diego Zoo")
print("\t" + "Inersection of Chicago and San Diego Zoo")
print(chicago_zoo_set.intersection(sandiego_zoo_set))
#Only Kangaroo

print()
print("UNIQUE animals at the Chicago Zoo")
print("\t" + "These are items at the Chicago Zoo, but NOT at the San Diego Zoo")
print(chicago_zoo_set.difference(sandiego_zoo_set))
#should include 'Polar Bear', 'Moose', 'Bobcat', 'Leopard'
# May be in a different order

print()
print("UNIQUE animals at the San Diego Zoo")
print("\t" + "These These are items at the San Diego Zoo, but NOT at the Chicago Zoo")
print(sandiego_zoo_set.difference(chicago_zoo_set))
#should include 'Lion', 'Grizzly Bear', 'Wildcat', 'Antelope'
#May be in a different order