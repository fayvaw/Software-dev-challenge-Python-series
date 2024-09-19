# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 00:20:08 2024

@author: Favour
"""

'''
TASK:
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate message to the user. Hint: how does an even / odd
    number react differently when divided by 2?
Extras:
    1. If the number is a multiple of 4, print out a different message.
    2. Ask the user for two numbers: one number to check (call it num) and one
    number to divide by (check). If check divides evenly into num, tell that
    to the user. If not, print a different appropriate message. 
    
    '''

number = int(input('Enter a number: '))
    
if number % 4 == 0:
    print("You've got a multiple of 4!")
elif number % 2 == 0:
    print(f'Yipee! {number} is an even number.')
else:
    print("Oops! That's an odd number")

#EXTRAS 2
num = int(input("Enter your favorite number: "))
check = int(input("Enter a check number: "))

if num % check == 0:
    print(f"Hello User, {num} divides evenly into {check}!")
else:
    print(f"You'll need to add {check - (num % check)} to {num} so that it can divide evenly into {check}.")