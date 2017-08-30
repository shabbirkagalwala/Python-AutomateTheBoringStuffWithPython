#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:16:07 2017

@author: shabbirkagalwala
"""
import shutil,os,send2trash,zipfile
'''
#here each source and destination is given as a string
shutil.copy('source','destination') #copy files
shutil.copytree('source','destination')
shutil.move('source','destination')

#now deleting files be careful while using these
os.unlink('path') #removes a file
os.rmdir('path')#removes an empty directory
shutil.rmtree('path')#deletes everything in a directory

#using this is more helpful than shutil.rmtree(path)
file = open('test.txt','a')
file.write('this is a test')
file.close()
send2trash.send2trash('test.txt')

#os.walk()
for folderName,subFolders,fileNames in os.walk('/Users/shabbirkagalwala/downloads/Docker Images'):
    print('The current folder is ' + folderName)
    for sub in subFolders:
        print('Subfolder of ' + folderName + ':' + sub)
    for filename in fileNames:
        print('File of ' + folderName + ':' + filename)
    print('')

exampleZip = zipfile.ZipFile('/Users/shabbirkagalwala/Desktop/ShabbirKagalwala.zip')
print(exampleZip.namelist())
info = exampleZip.getinfo('ShabbirKagalwala/data_mung.py')
print(info.file_size)
print(info.compress_size)
print('Compressed size is %sx smaller!' % (round(info.file_size/info.compress_size,2)))

#the ZipFile object has a namelist() method that returns a list of strings, 
#these strings can be passed to getinfo() method

exampleZip.extractall('/Users/shabbirkagalwala/Desktop/test')
exampleZip.extract('ShabbirKagalwala/data_mung.py')

newZip = zipfile.ZipFile('new.zip','w')#or use 'a'
newZip.write('bacon.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

'''