#!usr/bin/env python3

#Original tuple
chicago_zoo_tuple = ('Kangaroo', 'Leopard', 'Moose', 'Polar Bear', 'Bobcat')
sandiego_zoo_tuple = ('Kangaroo', 'Lion','Grizzly Bear', 'Wildcat','Antelope')

print("TUPLES...")
print('Chicago Zoo:', chicago_zoo_tuple)
print ('San Diego Zoo:', sandiego_zoo_tuple)
print()

########
#you can unpack a tuple but you can't change it
########

a1,a2,a3,a4,a5 = chicago_zoo_tuple

print("LOOKING at the Chicago Zoo..")
print("Animal 1:", a1)
print("Animal 2:", a2)
print("Animal 3:", a3)
print("Animal 4:", a4)
print("Animal 5:", a5)

print()
print('Chicago Zoo Tuple Length:',len(chicago_zoo_tuple))

##########
#NOTE that you cannot add items to a tuple
#NOTE that you will get an error if you uncomment the below line
#######

#chicago_zoo_tuple.add('Penguin')

