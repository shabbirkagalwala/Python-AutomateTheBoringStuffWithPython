#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:45:15 2017

@author: shabbirkagalwala
"""
import pprint

print('Enter string:')
stringvalue = input()
count = {}

for i in stringvalue:
    count.setdefault(i,0)
    count[i] = count[i] + 1
    
pprint.pprint(count)
print(pprint.pformat(count))