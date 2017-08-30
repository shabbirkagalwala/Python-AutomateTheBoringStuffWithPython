#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 22:07:21 2017

@author: shabbirkagalwala
"""

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i].strip()

text = '\n'.join(lines)
print(text)
pyperclip.copy(text)
print('\nText copied to clipboard')