#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:38:39 2017

@author: shabbirkagalwala
"""

import os,shelve,pprint

path = '/Users/shabbirkagalwala/Desktop/python'

os.path.join('usr','bin','spam')

os.getcwd()

os.chdir('/Users/shabbirkagalwala/Desktop')

os.makedirs('/Users/shabbirkagalwala/Desktop/test/test1/test2')

os.path.abspath('.')

os.path.isabs('.')

os.path.isabs('/Users/shabbirkagalwala/Desktop/python')

os.path.relpath('.','/')

print(os.path.basename(path))

print(os.path.dirname(path))

print(os.path.split(path))

print(os.path.sep) #gives the path seperator

print(path.split(os.path.sep)) 

print(os.path.getsize(path)) #size in bytes

print(os.listdir(path)) #list of filenames

print(os.path.exists(path)) #boolean value if path exists

print(os.path.isfile(os.path.join(path,'total.py'))) #boolean value if file exists

print(os.path.isdir(path)) #boolean value if dir exists

hello = open(os.path.join(path,'hello.txt'))

print(hello.read())

hello1 = open(os.path.join(path,'readline.txt'))

print(hello1.readlines())

baconFile = open(os.path.join(path,'bacon.txt'),'w') #will create a file if it does not exist
baconFile.write('Hello World!\n') #write to the file
baconFile.close() #call this before opening the file again

baconFile = open(os.path.join(path,'bacon.txt'),'a') #will append to the files content instead of over writinf
baconFile.write('Bacon is bae\n')#append
baconFile.close()

baconFile = open(os.path.join(path,'bacon.txt'))#open file
print(baconFile.read())#print contents

shelfFile = shelve.open('mydata') #file called mydata.db will be created
cats = ['Zophie','Pooka','Simon']
shelfFile['cats'] = cats

print(type(shelfFile))
print(shelfFile['cats'])
#just like dicts shelve values have keys and values

print(list(shelfFile.keys()))
print(list(shelfFile.values()))

shelfFile.close()

cats = [{'name':'Zophie','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
print(pprint.pformat(cats))

fileObj = open('cats.py','w')
fileObj.write('cats = ' +pprint.pformat(cats) + '\n')
fileObj.close()

#Since we stored it to a .py file we can close this shell and import it again and used again.
#check pprint.py file to see this used
