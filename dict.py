#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:13:01 2017

@author: shabbirkagalwala
"""

birthday = {'Shabbir':'Feb 14','Hatim':'April 5'}

while True:
    print('Enter the name : (Blank to exit))')
    name = input()
    if name == '':
        break
    
    if name in birthday.keys():
        print(name + '\'s birthday is on ' + birthday[name])
    else:
        print('I don\'t have their birthday stored')
        print('What is their birthday?:')
        bday = input()
        birthday[name] = bday
        print('Database updated!')