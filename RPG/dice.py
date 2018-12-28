# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 22:29:54 2018

@author: Nessim
"""

from numpy import array
from random import randint

    
class dice:
    def __init__(self,table):
        self.table = array(table)
        
    def __add__(self,other):
        return dice(self.table+other.table)
    
    def __add__(self,other):
        return dice(self.table+other.table)
    
    def __add__(self,x):
        return dice(self.table+[x,0,0,0,0,0,0,0])
    
    def __mul__(self,x):
        return dice(x*self.table)
    
    def __rmul__(self,x):
        return dice(x*self.table)
    
    def roll(self):
        result = 0
        dice = [1,4,6,8,10,12,20,100]
        for i in range(8):
            for j in range(self.table[i]):
                result += randint(1,dice[i])
        return result
    
    def expected(self):
        expected = self.table[0]
        dice = [1,4,6,8,10,12,20,100]
        for i in range(7):
            expected +=self.table[i+1]*(dice[i+1]+1)/2
        return expected
    

d4 = dice([0,1,0,0,0,0,0,0])
d6 = dice([0,0,1,0,0,0,0,0])
d8 = dice([0,0,0,1,0,0,0,0])
d10 = dice([0,0,0,0,1,0,0,0])
d12 = dice([0,0,0,0,0,1,0,0])
d20  = dice([0,0,0,0,0,0,1,0])
d100  = dice([0,0,0,0,0,0,0,1])