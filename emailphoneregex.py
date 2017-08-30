#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 16:43:17 2017

@author: shabbirkagalwala
"""

import pyperclip,re
phoneRegex = re.compile(r'''(
                         (\d{3} | \(\d{3}\))?  #areacode
                         (\s|-|\.)?            #seperator
                         (\d{3})               #3 digits
                         (\s|-|\.)             #seperator
                         (\d{4})               #4 digits
                         (\s*(ext|x|ext.)\s&(\d{2,5}))?  #extension
                         )''',re.VERBOSE)


emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+  #username
                        @                  #@
                        [a-zA-Z0-9.-]+     #domain
                        (\.[a-zA-Z]{2,4})  #.com,.net
                        )''',re.VERBOSE)


text = str(pyperclip.paste())


matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]]) #standardize the phone number by getting the area code,number 
    if groups[8] != '':
        phoneNum += ' X' +groups[8]
    matches.append(phoneNum)
    
for groups in emailRegex.findall(text):
    matches.append(groups[0])
    
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied')
    print('\n'.join(matches))
else:
    print('Nothing found nothing copied')

