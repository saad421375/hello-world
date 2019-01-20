# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 16:22:38 2018

@author: RedX
"""

def find(word,letter):
    idx=0
    count=0
    
    while idx<len(word):
        if word[idx]==letter:
            count+=1
            print('index = ',idx)
        idx+=1
    print('no of '+letter+'=', count)
flag=0
wd=input('Enter String')
ltr=input('letter')
find(wd,ltr)
