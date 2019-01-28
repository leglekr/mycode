#!/usr/bin/env python3

import random
import time


def intro():
    print("=========Adventures in the NRB========")
    time.sleep(2)
    user = input("'Hello, can I get your name again?:'")
    print("'Welcome to the NRB", user,"!'")
    print()
    user = input("'You report to Mark Williams right?'")
    print("'I knew it!  Well don't worry your going to do great here'")
    print()



def bobcall():
    path =""
    while path != "1" and path != "2":
        print("'I need you to watch Mark's phone for a moment..I'll be right back.'")
        time.sleep(2)
        print()
        print("You sit at your new desk and look around nervously.")
        time.sleep(2)
        print("Suddenly the phone rings.  You answer the phone and say hello....")
        time.sleep(2)
        print("The voice says...")
        print("'Mark this is Bob.  I got 3 things for you...'")
        time.sleep(5)
        print()
        print("You politely listen as your new Director gives a list of requests.")
        time.sleep(3)
        print("He thinks you are someone else.  Possibly Mark Williams.")
        time.sleep(3)
        print("Before you can respond Bob says 'Please have it to me by noon, thanks Mark'")
        time.sleep(3)
        print()
        time.sleep(2)
        user= input("'Thanks for watching my phone did anyone call? Yes??'")
        time.sleep(1)
        print("You reply that someone named Bob called")
        time.sleep(2)
        print("'What did he say?'")
        time.sleep(2)
        print()
        time.sleep(2)
        print("You desperately try to remember the instructions given....")
        print("It is either...")
        time.sleep(1)
        print()
        print("1. Ninjas have invaded the NOC. Speak to security, send back-up, and then join SEER bridge. OR...")
        print("2. Tell maintenance about potential killer wasp nest near the back door entrance.")


        path = input('Which will you say? (1 or 2):')

    return path



def checkpath(correct):
    print()
    print('You say the first thing that comes to your mind')
    time.sleep(2)

    goodpath = (1)

    if correct == str(goodpath):
        print("'Bob, said there are Ninjas in the NOC and to alert security.  He expects them cleared out by noon'")
        time.sleep(2)
        print("'Ninjas again huh?  OK I'll tell Mark.  Thanks!'")

    else:
        print("'Bob said there is a killer was nest near the building that needs to be taken out by Noon'")
        print()
        time.sleep(2)
        print("There is a brief pause before you hear a reply...")
        print("'We have not had Killer Wasp warning since 2009.  You just made that up...'")
        time.sleep(2)
        print("'Hand me your badge your done here!'")
        print("Your journey has ended.")
        print()



def ninjanoc():
    path2 = ""
    while path2 != "1" and path2 != "2":
        print()
        print("Moments later a man approaches you.")
        time.sleep(2)
        print("'Hi My name is Mark!' Thanks for the heads up about the Ninjas.'")
        time.sleep(2)
        print("'Come on down with me to the NOC. We can clear out the ninjas and I can give you a tour'")
        print()
        print("You head down to the NOC with Mark")
        time.sleep(2)
        print("As you both enter the NOC you see a group of Ninjas.")
        print("The leader approaches you.")
        time.sleep(2)
        print("Do you..")
        print("1. Say nothing and let Mark do all the talking.")
        print("2. Scold the leader of the Ninjas for not being in proper attire.")
        path2 = input('What will you do? (1 or 2):')

    return path2

def ninjachoice(correct2):

    goodpath1 = (1)

    if correct2 == str(goodpath1):
        print("You quickly regret saying nothing as the leader of the Ninjas throws a shruiken at your head.")
        print("Bad way to end day 1.")
    else:
        print("'Hey, it's Monday. You should be wearing business casual.' You say.")
        print("'Ninja attire is not permitted until Friday.'")
        time.sleep(2)
        print()
        print("The ninja leader hangs his head down low realizing his mistake.")
        print("He motions for his fellow Ninjas to exit the building.")

def vzlearn():
    path3 = ""
    while path3 != "1" and path3 != "2":
        print()
        print("'Quick thinking!' says Mark")
        time.sleep(2)
        print("'Let me show you around the NOC!'")
        time.sleep(2)
        print('Mark gives you a quick tour.  You then head back upstairs to the NRB')
        time.sleep(2)
        print('Mark advises he has a meeting and for you to work on a VZ Learn training from your desk')
        time.sleep(2)
        print()
        print("You sit at your desk and begin to take a VZ Learn test.")
        print("Suddenly you see an Instant Message appear on your screen")
        time.sleep(2)
        print("'Hello there!  My name is Bret!  Is this the greatest game ever?'")
        path3 = input('Press 1 for yes or 2 for no')

    return path3

def endchoice(correct3):

    goodpath1 = (1)

    if correct3 == str(goodpath1):
        print("You hear a slow clap begin from nearby personnel.")
        print("You know that you have had a successful first day at the NRB")
        time.sleep(2)
        print("THE END!")
    else:
        print("You advise that it was not the greatest game ever.")
        print("'Thank you for your honesty. Good bye,' comes the reply'")
        time.sleep(2)
        print("You feel a sense of dread as the floor underneath your desk opens up...")
        print("You fall on a metal slide which then shoots you out the building...")
        print("..and into your car.")
        time.sleep(2)
        print("Somehow you get the feeling you won't be let back into the building.")




playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    intro()
    path = bobcall()
    checkpath(path)
    if path == "1":
        path2 = ninjanoc()
        ninjachoice(path2)
        if path2 == "2":
          path3 = vzlearn()
          endchoice(path3)
    print('Do you want to play again? (yes or no)')
    playAgain = input()