#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 18:34:39 2017

@author: shabbirkagalwala
"""
import re

def password(text):
    password = re.compile(r'^[a-zA-Z]*([0-9])*.{8}$')
    mo = password.search(text)
    if mo != None:
        print('Password Matches criteria')
    else:
        print('Password must containe one lower case, one upper case letter, one number and must be atleast 8 character')
        

password('Alkanes123')