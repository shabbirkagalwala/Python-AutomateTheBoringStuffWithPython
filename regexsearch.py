#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 18:44:36 2017

@author: shabbirkagalwala
"""

import re,os

dir = os.listdir('/Users/shabbirkagalwala/Desktop/python')

for file in dir:
    if file.endswith(".txt"):
        files = open(file).read()
        #print(files)
        #for i in files:
        print('What text do you want to search for in '+ open(file).name + '?')#open(file).name gives the name of the file
        userReg = str(input('\n'))
        stringRegex = re.compile(userReg)
        found = stringRegex.search(files)
        if bool(found) == True:
           # for i in range(len(found)):
               print('\nText found:\n'+found.group()) #Used to print sre.SRE_Match object from re
        
