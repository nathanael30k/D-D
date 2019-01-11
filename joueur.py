# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:21:59 2019

@author: Nessim
"""

from dice import *
from arme import *

# Class

class Joueur:
    def __init__(self,name,init,bonus_att,bonus_dégat,CA,pv_max,arme):
        self.name = name
        self.init = init
        self.bonus_att = bonus_att
        self.bonus_dégat = bonus_dégat
        self.CA = CA
        self.pv_max=pv_max
        self.pv = pv_max
        self.arme = arme
    def expected_initiative(self):
        return 10.5+self.init
    def roll_initiative(self):
        return (d20+self.init).roll()+self.init/100
    def isAlive(self):
        return self.pv>0
    def pv_reset(self):
        self.pv = self.pv_max
  
# Base de données      
        
HobJason = Joueur("HobJasons",6,10,5,21,47,épéeBatarde)
HobJason2 = Joueur("HobJasons2",6,10,5,21,47,épéeBatarde)
Ogre = Joueur("L'Ogre",-1,8,7,16,29,massue)