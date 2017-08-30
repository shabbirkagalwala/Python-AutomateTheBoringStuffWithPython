#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 17:37:11 2017

@author: shabbirkagalwala
"""

import re

text = '''
Satoshi Nakamoto
Mr. Nakamoto
Alice Nakamoto
satoshi nakamoto
'''

regexFind = re.compile(r'^[A-Z][a-z]*\sNakamoto$',re.MULTILINE)
mo = regexFind.findall(text)
print(mo)