# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:23:09 2019

@author: Nessim
"""

from dice import *

# Class

class Arme:
    def __init__(self,dé_degat,crit_size,crit_mult,bonus_att,bonus_dégat,
                 IsTwoHanded):
        self.dé_arme = dé_degat+bonus_dégat
        self.crit_size = crit_size
        self.crit_mult = crit_mult
        self.bonus_att = bonus_att
        self.IsTwoHanded = IsTwoHanded
        
    def p_crit(self):
        # Cette fonction renvoie la probabilité qu'une attaque réussie soit un
        #critique
        # crit_size = taille de la zone de critique
        #ex: critique en 19-20 => crit_size = 2
        return self.crit_size/20

# Base de données
    
épéeBatarde = Arme(d10,2,2,1,0,False)   
massue = Arme(2*d8,1,2,0,0,True)


