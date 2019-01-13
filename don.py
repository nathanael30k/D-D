# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:48:58 2019

@author: Nessim
"""

def science_de_l_initiative(joueur):
    joueur.init += 4 
    
def robustesse(joueur):
    joueur.pv_max += 3
    joueur.pv += 3    

def arme_de_predilection(joueur):
    joueur.bonus_att += 1

def spé_martiale(joueur):
    joueur.bonus_dégat += 2
    
list_don_static = [science_de_l_initiative,robustesse]
list_don_arme = [arme_de_predilection,spé_martiale]
list_don_nom = ["Science de l'initiative","Robustesse","Arme de prédilection",\
                "Spécialisation martiale"]