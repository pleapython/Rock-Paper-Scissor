# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 04:45:01 2020

@author: achal
"""
import Options as op
import random as rand
import sys
class Game:
    
    def __init__(self,input_string):
        self.input_string=input_string
    
    def check_for_correctness(self):
        my_score,comp_score=0,0
        try:
            my_choice=int(self.input_string)
            if type(my_choice)==int:
                if my_choice==1:
                    print ("So you choose Rock")
                elif my_choice==2:
                    print ("So you choose Paper")
                elif my_choice==3:
                    print ("So you choose Scissor")
                else:
                    raise ValueError("Incorrect value chosen")
            else:
                raise ValueError
        except(ValueError,)as msg:
            print("Your choice of option is wrong :",msg) 
            sys.exit(0)               
        print(" _____________________________________________________________________________")
        computer_choice=rand.choice([1,2,3])
        if my_choice==1:
            if computer_choice==1:
                my_score,comp_score=0.5,0.5
                print(op.Options.rock_rock)
                print("|                                   ITS A DRAW                                |")       
            elif computer_choice==2:
                my_score,comp_score=0,1
                print(op.Options.rock_paper)
                print("|                                    YOU LOST                                 |")
            else:
                my_score,comp_score=1,0
                print(op.Options.rock_scissors)
                print("|                                    YOU WIN                                  |")
        elif my_choice==2:
            if computer_choice==1:
                my_score,comp_score=1,0
                print(op.Options.paper_rock)
                print("|                                    YOU WIN                                  |")
            elif computer_choice==2:
                my_score,comp_score=0.5,0.5
                print(op.Options.paper_paper)
                print("|                                   ITS A DRAW                                |")       
            else:
                my_score,comp_score=0,1
                print(op.Options.paper_scissors)
                print("|                                    YOU LOST                                 |")
        else:
            if computer_choice==1:
                my_score,comp_score=0,1
                print(op.Options.scissors_rock)
                print("|                                    YOU LOST                                 |")
            elif computer_choice==2:
                my_score,comp_score=1,0
                print(op.Options.scissors_paper)
                print("|                                    YOU WIN                                  |")
            else:
                my_score,comp_score=0.5,0.5
                print(op.Options.scissors_scissors)
                print("|                                   ITS A DRAW                                |")       
        print("|_____________________________________________________________________________|")
        return my_score,comp_score


#print(my_choice,computer_choice)

