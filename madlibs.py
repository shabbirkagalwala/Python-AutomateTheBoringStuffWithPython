#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 23:17:20 2017

@author: shabbirkagalwala
"""
import re



libsFile = open('madlibs.txt').read().split()
output = open('output.txt','w')


for word in libsFile:
    if bool(re.search(r'NOUN',word)) == True :
        print('Enter an Noun:')
        noun = input()
        output.write(re.sub(r'NOUN',noun,word,count=1,flags=0)+" ")
    elif bool(re.search(r'ADJECTIVE',word)) == True :
        print('Enter an Adjective:')
        adjective = input()
        output.write(re.sub(r'ADJECTIVE',adjective,word,count=1,flags=0)+" ")
    elif bool(re.search(r'VERB',word)) == True :
        print('Enter a Verb:')
        verb = input()
        output.write(re.sub(r'VERB',verb,word,count=1,flags=0)+" ")
    elif bool(re.search(r'ADVERB',word)) == True :
        print('Enter a Verb:')
        adverb = input()
        output.write(re.sub(r'ADVERB',adverb,word,count=1,flags=0)+" ")
    else:
        output.write(word+" ")


output.close()

print('The file was written ' + open('output.txt').read())