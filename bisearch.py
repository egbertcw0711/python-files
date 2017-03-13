# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 18:16:46 2017

@author: egbertcw
"""
high = 100
low = 0
guess = (high + low)/2

print('Please think of a number between 0 and 100!')
while True:
    print('Is your secret number'+str(guess) + '?', end = '')
    c = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to incicate I guessed correctly.")
    if(c == 'h'):
        high = guess
        guess = int((high + low)/2)
    elif(c == 'l'):
        low = guess
        guess = int((high + low)/2)
    elif(c == 'c'):
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
        
        