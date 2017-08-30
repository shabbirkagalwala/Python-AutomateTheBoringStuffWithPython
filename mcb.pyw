#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:26:21 2017

@author: shabbirkagalwala
"""
#python mcb.pyw save <keyword> - saves clipboard to keyword
#python mcb.pyw list - loads all keywords to clipboard
#python mcb.pyw <keyword> - loads keyword content to clipboard

import shelve,sys,pyperclip

mcbShelf = shelve.open('mcb')

#check how many sys argv we give
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    #if 3 arg is save then save the copied text to the keyword given in the arg
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
#if there are 2 args
elif len(sys.argv) == 2 and sys.argv[1].lower() != 'delete':
    #if the arg is list, then copy all the keys from the mcb file
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    #else consider the keyword is given and copy the keyword value from the mcb file
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
    mcbShelf.clear()
   

mcbShelf.close()