#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 17:17:12 2017

@author: shabbirkagalwala
"""

import re

text = '''
42
1,234
6,368,745
12,34,567
1234
1,234,567,789
'''

mo = re.compile(r'^\d{1,3}(?:,\d{3})*$',re.MULTILINE) 
t = mo.findall(text)
print(t)