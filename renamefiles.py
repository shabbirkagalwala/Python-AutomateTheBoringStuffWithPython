#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 21:58:16 2017

@author: shabbirkagalwala
"""
import re,os

datePattern = re.compile(r'''^(.*?)         #all text before date
                         ((0|1)?\d)-        #MM part of the date
                         ((0|1|2|3)?\d)-    #DD part of date
                         ((19|20)\d\d)     #YYYY part of date
                         (.*?)$
                         ''',re.VERBOSE)       

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    
    if mo == None: #skip files without a date
        continue
    
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    
    euroFilename = beforePart + dayPart + '-'+ monthPart + '-' + yearPart + afterPart
    
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    
    print('Renaming "%s" to "%s" ...'% (amerFilename,euroFilename))
    #shutil.move(amerFilename,euroFilename)