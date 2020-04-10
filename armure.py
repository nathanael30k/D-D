# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 01:09:30 2019

@author: Nessim
"""

from numpy import inf
from copy import deepcopy

# =============================================================================
#  Class
# =============================================================================

class Armure:
    def __init__(self,nom,id,bonus_CA,modif_dex_max,bonus_magique,\
                 effet_magique,prix_base):
        
        self.nom = nom
        
        self.id = id
        
        self.bonus_CA = bonus_CA+bonus_magique
        self.modif_dex_max = modif_dex_max
        
        self.bonus_magique = bonus_magique
        self.effet_magique = effet_magique
        
        self.modif_magie = bonus_magique 
        for i in range(len(effet_magique)):
            effet_magique[i](self)
            
        self.prix_base = prix_base 
    

    
    def set_magic(self,name,bonus_magique,effet_magique):
        
        output = deepcopy(self)
        
        output.nom = self.nom
        
        output.bonus_magique = bonus_magique
        output.effet_magique = effet_magique
        
        output.bonus_CA = self.bonus_CA+bonus_magique
        output.modif_magie = bonus_magique 
        for i in range(len(effet_magique)):
            effet_magique[i](output)
        
        return output
    
    def __str__(self):
        output = self.nom+"\n"
        if self.bonus_magique != 0 :
            output += " +"+str(self.bonus_magique)
        output += "CA: +"+str(self.bonus_CA)+"\n"
        output += "prix: "+str(self.prix_achat())+"po\n"
        return output
    
    
    def prix_achat(self):
        prix_magie = [0,1,4,9,12,25,36,49,64,81,100]
        return self.prix_base + 1000*prix_magie[self.modif_magie]

