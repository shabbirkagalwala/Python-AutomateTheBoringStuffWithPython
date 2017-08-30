#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 20:41:17 2017

@author: shabbirkagalwala
"""

import random


capitals = {'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix','Arkansas':'LittleRock',
            'California':'Sacramento','Colorado':'Denver','Connecticut':'Hartford','Delaware':'Dover',
            'Florida':'Tallahassee','Georgia':'Atlanta','Hawaii':'Honolulu','Idaho':'Boise',
            'Illinois':'Springfield','Indiana':'Indianapolis','Iowa':'DesMoines','Kansas':'Topeka',
            'Kentucky':'Frankfort','Louisiana':'BatonRouge','Maine':'Augusta','Maryland':'Annapolis',
            'Massachusetts':'Boston','Michigan':'Lansing','Minnesota':'SaintPaul',
            'Mississippi':'Jackson','Missouri':'JeffersonCity','Montana':'Helena','Nebraska':'Lincoln',
            'Nevada':'CarsonCity','NewHampshire':'Concord','NewJersey':'Trenton','NewMexico':'SantaFe',
            'NewYork':'Albany','NorthCarolina':'Raleigh','NorthDakota':'Bismarck','Ohio':'Columbus',
            'Oklahoma':'OklahomaCity','Oregon':'Salem','Pennsylvania':'Harrisburg',
            'RhodeIsland':'Providence','SouthCarolina':'Columbia','SouthDakota':'Pierre',
            'Tennessee':'Nashville','Texas':'Austin','Utah':'SaltLakeCity','Vermont':'Montpelier',
            'Virginia':'Richmond','Washington':'Olympia','WestVirginia':'Charleston',
            'Wisconsin':'Madison','Wyoming':'Cheyenne'}

#since we want to create 35 files
for quizNum in range(35):
    #we now want to create answer key files and question files
    quizFile = open('capitalquiz%s.txt' %(quizNum+1),'w')
    answerKeyFile = open('capitalquiz_answers%s.txt' %(quizNum+1),'w')
    
    #write the header to each file
    quizFile.write('Name\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20)+'State Capital Quiz (Form %s)' %(quizNum +1))
    quizFile.write('\n\n')
    
    #shuffle the order of states in the dict by making a list with the keys i.e state names
    states=list(capitals.keys())
    random.shuffle(states) #will randomly shuffle the states
    

    #Loop through all 50 states
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        #duplicating all values in the dict
        wrongAnswer = list(capitals.values()) 
        #deleting the correct answer from the wrong answer list
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        #since all correct answers have been deleted we can take a random sample of 3
        wrongAnswer = random.sample(wrongAnswer,3)
        
        answerOptions = wrongAnswer + [correctAnswer]
        
        #Randomize the answer options so its not always the last option D
        random.shuffle(answerOptions)
        
        quizFile.write('%s. What is the capital of %s?\n' %(questionNum+1,states[questionNum]))
        
        for i in range(4):
            quizFile.write('   %s. %s\n' %('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')
        
        answerKeyFile.write('%d. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
        
quizFile.close()
answerKeyFile.close()