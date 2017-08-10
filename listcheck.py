#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 20:15:52 2017

@author: shabbirkagalwala
"""

pets = ['cat','dog','fish','parrot']

print('Enter a pet name:')
name = input()

if name not in pets:
    print('Sorry! We do not have ' + name)
else:
    print('Yay! We do have a ' + name)