#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 23:31:44 2017

@author: shabbirkagalwala
"""

inv = {'rope': 1, 'gold coin': 42}

dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']


def addToInventory(inventory, addItems):
    for k in range(len(addItems)):
        if addItems[k] in inventory:
            inventory[addItems[k]] += 1
        else:
            inventory.setdefault(addItems[k], 1)
    return inventory


def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = sum(inventory.values())
        #item_total += v
    print('Total number of items: ' + str(item_total))

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)