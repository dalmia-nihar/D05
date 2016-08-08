#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body


def infinite_stairway_room(count=0):
    print("You walk through the door to see a dimly lit hallway.")
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print('You take the stairs')
        if (count > 0):
            print("but you're not happy about it")
        infinite_stairway_room(count + 1)
    option_2 = "go back"
    if next == option_2:
        main()


def gold_room():
    print("This room is full of gold.  How much do you take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy goose!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    bear_moved = False
    
    while True:
        next = input("> ")
        
        if next == "take" or next == "honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" or next == "taunt" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" or next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open" or next == "door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    print("Welcome, please enter your name.. ")
    user_name = input("> ")
    print(user_name + " is in a dark room.")
    print("There is a door to " +  user_name + "'s right, left and straight.")
    print("Which one does " + user_name +  " take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    elif next == "straight":
        infinite_stairway_room()
    else:
        dead(user_name + " stumbles around the room until "+ user_name + "  starves.")

if __name__ == '__main__':
    main()
