#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 20:42:24 2017

@author: shabbirkagalwala
"""

while True:
    print('Enter your age')
    age = input()
    if age.isdecimal():
        break
    print('Enter a valid age number')

while True:
    print("Enter a password ('Password can contain only numbers and letters')")
    password = input()
    if password.isalnum():
        break
    print('Enter a valid password')