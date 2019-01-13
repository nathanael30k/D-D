# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 01:45:56 2019

@author: Nessim
"""

from dice import *
from copy import *

class Bouclier:
    def __init__(self,name,id,bonus_CA,bonus_magique,effet_magique,prix_base):
        
        self.name = name
        self.id = id
        self.bonus_CA = bonus_CA+bonus_magique
        
        self.bonus_magique = bonus_magique
        self.effet_magique = effet_magique
        
        self.prix_base = prix_base  
        
        self.modif_magie = bonus_magique 
        for i in range(len(effet_magique)):
            effet_magique[i](self)
    
    def __str__(self):
        output = self.name+"\n"
        if self.bonus_magique != 0 :
            output += " +"+str(self.bonus_magique)
        output += "CA: +"+str(self.bonus_CA)+"\n"
        output += "prix: "+str(self.prix_achat())+"po\n"
        return output
    
    def add_magic(self,name,bonus_magique,effet_magique):
        output = deepcopy(self)
        output.name = name
        output.bonus_magique = bonus_magique
        output.effet_magique = effet_magique
        
        self.bonus_CA = bonus_CA+bonus_magique
        self.modif_magie = bonus_magique 
        for i in range(len(effet_magique)):
            effet_magique[i](output)
        
        return output
    
    def prix_achat(self):
        prix_magie = [0,1,4,9,12,25,36,49,64,81,100]
        return self.prix_base + 1000*prix_magie[self.modif_magie]

# Base de données
        

écu_acier = Bouclier("Ecu en acier",1,2,0,[],20)
aucun = Bouclier("aucun",0,0,0,[],0)
list_bouclier = [aucun,écu_acier]

# test

#print(écu_acier)
