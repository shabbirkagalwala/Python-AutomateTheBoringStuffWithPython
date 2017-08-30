#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 22:24:37 2017

@author: shabbirkagalwala
"""

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
    ]


def colWidth(tableData):
    colWidths = [0] * len(tableData)
    for col in range(len(tableData)):#for range(length) of the outer lists - 0,1,2
        for item in tableData[col]:#for each outer list, iterate through inner values
            if len(item) > colWidths[col]:
                colWidths[col] = len(item)
    y = max(colWidths)
    
    ys = list(map(list, zip(*tableData)))
    for xs in range(len(ys)):
        for xd in ys[xs]:
            print(str(xd).rjust(y), end ='',flush=True)
        print('\t')

colWidth(tableData)        
