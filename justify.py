#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 21:08:56 2017

@author: shabbirkagalwala
"""

dict = {'sandwiches':4,'apples':10,'cups':20,'cookies':40}

def string(dictin,lwidth,rwidth):
    print('PICNIC ITEMS'.center(lwidth+rwidth,'-'))
    for k, v in dictin.items():
        print(k.ljust(lwidth,'.')+str(v).rjust(rwidth))
        
string(dict,12,5)