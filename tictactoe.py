#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 20:18:08 2017

@author: shabbirkagalwala
"""
board = {7:' ',8:' ',9:' ',
         4:' ',5:' ',6:' ',
         1:' ',2:' ',3:' '}

def tictac(board):
     print('   |   |')
     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
     print('   |   |')

turn = 'x' 
win = False
for i in range(9):        
    tictac(board)
    print('Turn for ' + turn + '. Move on which space?')    
    move = int(input())

    if board[move] != ' ':
        print('Already taken, Enter another cell value')
    else:
        board[move] = turn

    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
    
tictac(board)