#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:24:15 2017

@author: shabbirkagalwala
"""
import re

text = 'eeeHello World   '
char ='e'
char1= ' '

def stringreplace(text):
    splitRegex = re.compile(r'^(?:%s)*(.*?)(?:%s)*$'%(char,char1)) 
    mo = splitRegex.sub(r'\1',text)
    print(mo)
    
stringreplace(text)

'''
(?:...)
This construct is similar to (...), but won't create a capture group.
/(?:he)+/g
heheh he heh
matches 
hehe he he
'''