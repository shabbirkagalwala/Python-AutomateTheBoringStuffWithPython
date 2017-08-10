#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 23:00:48 2017

@author: shabbirkagalwala
"""

spam = ['apples','bananas','tofu','cat']

def func(test):
    #will concat the last value of the list with 'and'
    test[-1] = 'and ' + test[-1]
    
    #this will insert and at the -1 index
    #test.insert(-1,'and')
    
    comma = ', '
    print(comma.join(test))
        
        
func(spam)