# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 06:52:03 2020

@author: achal
"""
import Options as op
import Game 
print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|                   WELCOME TO ROCK PAPER AND SCISSORS GAME                   |")
print("|_____________________________________________________________________________|")
print("|                                                                             |")
print("|                       THESE ARE THE OPTIONS AVAILABLE                       |")
print("|_____________________________________________________________________________|")
print(op.Options.choices)

print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|                   SELECT ANY OTHER VALUE THAN REQUIRED TO EXIT              |")
print("|_____________________________________________________________________________|")

my_cumalative,comp_cumalative=0,0
keep_to_do=True
while keep_to_do:
    if keep_to_do:
        input_data=input("SELECT THE OPTION :")
        g=Game.Game(input_data)
        me,comp=g.check_for_correctness()
        my_cumalative,comp_cumalative=my_cumalative+me,comp_cumalative+comp
        print("\n                          ME {} - {} COMP".format(my_cumalative,comp_cumalative))
        
    