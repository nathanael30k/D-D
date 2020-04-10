# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 01:52:51 2019

@author: Nessim
"""

from dice import d6

# =============================================================================
# Class
# =============================================================================

class Effet_arme:
    def __init__(self,nom,id,effet,description):
        
        self.nom = nom
        
        self.id = id #numero dans la liste des dons 
        
        self.effet = effet
        #effet est une fonction prenant comme argument une arme et y applique \
        #l'effet magique
        
        self.description = description

# =============================================================================
# Database
# =============================================================================

def feu_effet(arme):
    arme.dé_arme += d6
    arme.modif_magie += 1
    
feu = Effet_arme("de feu",0,feu_effet,"ajoute 1d6 de feu")
    
def acérée_effet(arme):
    arme.crit_size = arme.crit_size*2
    arme.modif_magie += 1
    
acérée = Effet_arme("acérée",1,acérée_effet,"double la zone de critque")


list_effet_arme = [feu,acérée]