#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 22:57:32 2017

@author: shabbirkagalwala
"""

import copy

spam = [1,2,3,4]
junk = copy.copy(spam)
junk.append('10')

print(spam)
print(junk)