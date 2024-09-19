# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 09:42:52 2024

@author: Favour
"""

'''TASK:
    create a program that asks a user to enter their name and their age.
    print ut a message addressed to them that tells them the year they will turn
    100 years old. 
    NOTE:
        for this exercise, the expectation is that you explicitly write out the year
        and therefore, be out of date the next year.
    
    EXTRAS:
        1. Add on to the previous program by asking the user for another number and 
        printing out that many copies of the previous message.
        (hint: the order of operations exists in python)
        2. Print out that many copies of the previous message on separate lines.
        (hint: the string "\n" is the same as pressing the ENTER button)'''

user_name = input('Enter your name: ')
age = int(input("Enter your age: "))
times = int(input("How many times do you want to get a message? "))

birth_yr = 2024 - age
age100 = birth_yr + 100

print((f" Hello, {user_name}!\n You will turn 100 by year {age100}.\n")*times)