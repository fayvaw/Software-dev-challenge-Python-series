# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 06:11:57 2024

@author: Favour
"""

user_name = input('Enter your name: ')
age = 1000

# while not(age >= 0 and age <= 100):
while not(0 <= age <= 100):
    age = int(input("Enter your age: "))
    if not(age >= 0 and age <= 100):
        print('Error! Age must be between 0-100')
        
times = int(input("How many times do you want to get a message? "))

birth_yr = 2024 - age
age100 = birth_yr + 100

print((f" Hello, {user_name}!\n You will turn 100 by year {age100}.\n")*times)