#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 00:43:09 2017

@author: shabbirkagalwala
"""

import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 682-936-0111')
print('Phone number found: ' + mo.group())
print('Area code: ' + mo.group(1))
print('Number: ' +mo.group(2))

mo1 = mo.groups()
print(mo1)
areacode,number = mo1
print('areacode ' + areacode + ' number ' + number)

phoneNumRegex1 = re.compile(r'(\(\d{3}\))-(\d{3}-\d{4})')
mo2 = phoneNumRegex1.search('(682)-936-0111')
print(mo2.groups())
area,num = mo2.groups()
print('area ' + area + ' Num ' + num)


batRegex = re.compile(r'Bat(man|mobile|copter)')
mo3 = batRegex.search('Batman lost the Batmobile')
print(mo3.group()) #returns only the first occurence of the matching string
print(mo3.group(1))#returns only man which matches our pipe search

batRegex1 = re.compile(r'Bat(wo)?(man|mobile|copter)')#here (wo)? is the optional group to match
mo4 = batRegex1.search('Batwoman lost the batmobile')
print(mo4.group())


phoneNumRegex3 = re.compile(r'(\(\d{3}\)-)?(\d{3}-\d{4})')#here we say that the area code can be optional
mo5 = phoneNumRegex3.search('My number is without the area code 936-0111')
print(mo5.group())#gives us a matching number


batRegex2 = re.compile(r'Bat(wo)*(man|mobile|copter)')#here (wo)* matches 0 or more occurences of wo
mo6 = batRegex2.search('Batman lost the batmobile')
print(mo6.group())

batRegex3 = re.compile(r'Bat(wo)*(man|mobile|copter)')#here (wo)* matches 0 or more occurences of wo
mo7 = batRegex3.search('Batwowowowowowowoman lost the batmobile')
print(mo7.group())

batRegex4 = re.compile(r'Bat(wo)+(man|mobile|copter)')#here (wo)+ matches 1 or more occurences of wo
mo8 = batRegex4.search('Batwoman lost the batmobile')
print(mo8.group())#when you change it to Batman, will give an error as it matches one or more occurences


greedyHaRegex = re.compile(r'(Ha){3,5}')#this is the greedy regex, matches 5 occurences of the Ha word
ha = greedyHaRegex.search('HaHaHaHaHaHa')#here even though we have more than 5 Ha's
print(ha.group())#this will return the longest matches string

greedyHaRegex1 = re.compile(r'(Ha){3,5}?')#this is the non-greedy regex, matches 3 occurences of the Ha word
ha1 = greedyHaRegex1.search('HaHaHaHaHaHa')#here even though we have more than 5 Ha's
print(ha1.group())#this will return the shortest matching string

phoneNumRegex4 = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo9 = phoneNumRegex4.findall('My number is 682-936-0111 and work number is 111-222-3333')
print('Phone number found: ' + str(mo9))#here findall gives us both the numbers where as if we had search
#we would only get the first number back
#but see the difference, since we have groups in regex we get list of tuples for each group



"""
\d - digits 0-9
\D - any character not digits 0-9
\w - any letter, digit or underscore
\W - not in \w
\s - space, tab newline
\S - not in \s

[aeiouAEIOU]
[a-zA-Z0-9]
[0-5.]
[^aeiouAEIOU] - negative (not in)

"""

beginsWith = re.compile(r'^\d+')
bw = beginsWith.search('123 abc')
print(bw)

endsWith = re.compile(r'\d+$')
ew = endsWith.search('abc abc123')
print(ew)

endbegin = re.compile(r'^\d+$')
eb =endbegin.search('123abc456')
print(eb)#mathces the entire string and not just the begining and end if ^ and $ are used


"""
.at - wildcard will match exactly one character at the dot position
will match cat,hat but for flat it will match only "lat"

.* - will match everything

.* - greedy
.*? non greedy - match the shortest string

Any of the above will not match a new line character

re.DOTALL - pass as an argument to re.compile and it will also match new line characters
"""
atRegex = re.compile(r'.at')
wc = atRegex.findall('the cat in the hat sat on the flat mat')
print(wc)

atRegex1 = re.compile(r'.*')
wc1 = atRegex1.findall('the cat in the hat sat on the flat mat')
print(wc1)

"""
ignore cases with re.I pass as an argument to re.compile
re.compile(r'robocop',re.I)

substitue strings with sub regex
.sub('sub-word','string to search')
"""

subRegex = re.compile(r'Agent \w+',re.I)#exactly one word after agent and ignores case.
sr = subRegex.sub('CENSORED','AgEnT ShAbBir gave the docs to AgenT bOb')
print(sr)

aName = re.compile(r'Agent (\w)\w*')#(\w) is the first word of the name and \w* follows everything after
an = aName.sub(r'\1****','Agent Shabbir told Agent Hatim that Agent Carol Knew Agent Bob was a double agent.')
#\1**** here \1 will be replaced by (\w) match and \w* will be replaced by ****
print(an)


