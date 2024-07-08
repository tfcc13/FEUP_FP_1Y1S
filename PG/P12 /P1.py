#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:58:22 2023

@author: tiago
"""


def intro():
    print("After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.")
    print("A. Grab a nearby rock and throw it at the orc")
    print('B. Lie down and wait to be mauled')
    print('C. Run')
    plc = input()
    
    if plc.lower() == "a":
        rock()
    elif plc.lower() == "b":
        print("Welp, that was quick. You died!")
    elif plc.lower() == "c":
        run()
        
def rock():
    print('The orc is stunned, but regains control. He begins running towards you again.')
    print('A. Run')
    print('B. Throw another rock')
    print('C. Run towards a nearby cave')
    plc = input()
    
    if plc.lower() == "a":
        run()
    elif plc.lower() == "b":
        print("The rock flew well over the orcs head. You missed. You died!")
    elif plc.lower() == "c":
        cave()
        
def cave():
    print("Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?")
    sword = input()
    
    print('What do you do next?')
    print('A. Hide in silence')
    print('B. Fight')
    print('C. Run')
    plc = input()
    
    if plc.lower() == "a":
        print("I think orcs can see very well in the dark, right? You died!")
        
    elif plc.lower() == "b" and sword.lower() == "y":
        print("As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!")
    elif plc.lower() == "b" and sword.lower() == "n":
        print("You're defenseless. You died!")
    elif plc.lower() == "c":
        print("The orc turns around and sees you running.")
        run()
        

def run():
    print('You run as quickly as possible.')
    print('A. Hide behind boulder')
    print('B. Trapped, so you fight')
    print('C. Run towards an abandoned town')
    plc = input()

    if plc.lower() == "a":
        print("You're easily spotted. You died!")
    elif plc.lower() == "b":
        print("You're no match for an orc. You died!")
    elif plc.lower() == "c":
        town()
        
def town():
    print('You notice a purple flower near your foot. Do you pick it up? Y/N')
    flower = input()
    if flower.lower() == "y":
        print('You quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!')
    else:
        print('Maybe you should have picked up the flower. You died!')
    
    
    
'After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.\nA. Grab a nearby rock and throw it at the orc\nB. Lie down and wait to be mauled\nC. Run\nThe orc is stunned, but regains control. He begins running towards you again.\nA. Run\nB. Throw another rock\nC. Run towards a nearby cave\nBefore you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?\nWhat do you do next?\nA. Hide in silence\nB. Fight\nC. Run\nThe orc turns around and sees you running.\nYou run as quickly as possible.\nA. Hide behind boulder\nB. Trapped, so you fight\nC. Run towards an abandoned town\nYou notice a purple flower near your foot. Do you pick it up? Y/N\nYou quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!'

'After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.\nA. Grab a nearby rock and throw it at the orc\nB. Lie down and wait to be mauled\nC. Run\nThe orc is stunned, but regains control. He begins running towards you again.\nA. Run\nB. Throw another rock\nC. Run towards a nearby cave\nBefore you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?\nWhat do you do next?\nA. Hide in silence\nB. Fight\nC. Run\nYou run as quickly as possible.\nA. Hide behind boulder\nB. Trapped, so you fight\nC. Run towards an abandoned town\nYou notice a purple flower near your foot. Do you pick it up? Y/N\nYou quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!'