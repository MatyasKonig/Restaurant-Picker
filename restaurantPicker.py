#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:02:54 2018

@author: matyask
"""

import random

restaurantsList = ['boloco', 'clover', 'sweetgreens', 'dig inn']

def pickRestaurant():
    print(restaurantsList[random.randint(0,len(restaurantsList)-1)])

def addRestaurant(name):
    restaurantsList.append(name)
    
def removeRestaurant(name):
    restaurantsList.remove(name)
    
def listRestaurant():
    for restaurant in restaurantsList:
        print(restaurant)
    
while True:
    print('''
          
          [1] - List restaurant
          [2] - Add restaurant
          [3] - Remove restaurant
          [4] - Pick restaurant
          [5] - Exit
          
          ''')
    selection = input('Please select an option: ')
    
    if selection == '1':
        print('')
        listRestaurant()
    elif selection == '2':
        inName = input('Type name of the restaurant that you want to add: ')
        addRestaurant(inName)
    elif selection == '3':
        inName = input('Type name of the restaurant that you want to remove: ')
        removeRestaurant(inName)
    elif selection == '4':
        pickRestaurant()
    elif selection == '5':
        break
    else:
        print('\nError: Please select one of the options above.')