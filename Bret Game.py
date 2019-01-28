#!/usr/bin/env python3

import time

intro = "The beginning of the journey"


def choosepath():
    "You see two paths in front of you."
    "One leads up the mountain and the other"
    "leads into the forest."
    "Which way will you go?"


print(intro)
time.sleep(1)
user = input("What is your name?:")
print("Welcome", user)
print()
user = input("Are you a Paladin, Wizard, or Warrior?")
print("I knew it!  You look like a", user)
print()
time.sleep(1)
print(choosepath)
