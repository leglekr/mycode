choice = (input('Would you like to eat out tonight? Enter In or Out: '))
choice.lower()
if choice == "in":
    print('we will eat the same boring food')
else:
    print("Would you like \n1 - mexican\n2 - BBQ\n3 - Italian\n")
    food = int(input())
    if food == 1:
        print('We will get Mexican.')
    if food == 2:
        print('We will get BBQ.')
    if food == 3:
        print('We will get Italian.')
