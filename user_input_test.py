# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 20:34:36 2023

@author: mheldb
"""

choices = ("A", "B", "C", "D")


def user_choice_what_to_plot(choices): 
    for i in range(len(choices)):
        print(i, ": ", choices[i])
    #del i
    print('Make a choice by typing the number of the parameter to print: ')
    chosen_parameter_index = input()
    chosen_parameter_index = int(chosen_parameter_index)
    print('Chosen parameter: ' + choices[chosen_parameter_index])
    return chosen_parameter_index

def ask_to_repeat_plotting(message): 
    print(message)
    repeat_choice = input()
    return repeat_choice

chosen_parameter_index = user_choice_what_to_plot(choices)

message = 'Because this was such a great experience, do you want to do it again? (y/n)'
repeat_choice = ask_to_repeat_plotting(message)

while not repeat_choice == "n":
    if repeat_choice == "y": 
        chosen_parameter_index = user_choice_what_to_plot(choices)
        message = 'Because this was such a great experience, do you want to do it again? (y/n)'
        del repeat_choice
        repeat_choice = ask_to_repeat_plotting(message)
    else:
        message = 'That was neither a "y" or an "n". Do you want to do it again? (y/n)'
        #print(message)        del repeat_choice
        repeat_choice = ask_to_repeat_plotting(message)

message = "Done plotting world domination!"


