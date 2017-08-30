#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 22:18:25 2017

@author: shabbirkagalwala
"""

from pprint import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

DICT = {}

for char in message.upper():
    DICT[char] = DICT.get(char, 0) + 1
pprint(DICT)