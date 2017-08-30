#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 21:56:57 2017

@author: shabbirkagalwala
"""

passwords = {'email':'xyz',
             'email2':'abc'}

import sys,pyperclip

#check if there are 2 args given to the command, first name of program, second account name
if len(sys.argv) < 2:
    print('Usage: python password.py [account] - copy account password')
    sys.exit()

#2nd arg passed to the cmd take it as the account    
account= sys.argv[1]

#if account is present in our passwords dict
if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for  ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)