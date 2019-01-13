# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 15:40:05 2019

@author: Nessim
"""

class Classe:
    def __init__(self,name,bba_mult,DV):
        self.bba_mult = bba_mult
        self.DV = DV
        self.name = name
        
guerrier = Classe("Guerrier",1,10)
roublard = Classe("Roublard",0.75,6)

list_classe = [guerrier,roublard]