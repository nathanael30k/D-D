# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:48:58 2019

@author: Nessim
"""

# =============================================================================
# Class
# =============================================================================

class Don:
    def __init__(self,nom,id,categorie,effet,check,description):
        
        self.nom = nom
        
        self.id = id #numero dans la liste des dons 
        self.categorie = categorie #0 pour static, 1 pour arme, 2 pour tactique
        
        self.effet = effet
        #effet est une fonction prenant comme argument un joueur et un entier \
        #valant 1 (active le don) ou -1 (désactive le don) 
        
        self.check = check
        #check est une fonction prenant comme argument un joueur et renvoyant \
        #True si le don est accessible au joueur
        
        self.description = description
        
# =============================================================================
# Don static
# =============================================================================


def no_condition(joueur):
    return True

def no_effect(joueur,sens=1):
    return True

aucun = Don("aucun",0,0,no_effect,no_condition,"Don non choisi")
        
def science_de_l_initiative_effet(joueur,sens=1):
    joueur.init += sens*4

science_de_l_initiative = Don("Science de l'initative",1,0,\
            science_de_l_initiative_effet,no_condition,\
            "Le personnage bénéficie d’un bonus de +4 au test d’initiative.")


    
def robustesse_effet(joueur,sens=1):
    joueur.pv_max += sens*3
    joueur.pv_reset()
    return True

robustesse = Don("Robustesse",2,0,robustesse_effet,no_condition,\
                 "Le personnage gagne 3 points de vie supplémentaires.")



list_don_static = [aucun,science_de_l_initiative,robustesse]

# =============================================================================
# #Don d'arme
# =============================================================================


def arme_de_predilection_check(joueur):
    if joueur.bba >= 4:
        return True
    return False

def arme_de_predilection_effet(joueur,sens=1):     
    joueur.bonus_att += sens*1

arme_de_predilection = Don("Arme de prédilection",3,1,\
            arme_de_predilection_effet,arme_de_predilection_check,\
            "Le personnage bénéficie d’un bonus de +1 à tous ses jets \
            d’attaque lorsqu’il utilise son arme de prédilection.")



def spé_martiale_check(joueur):
    list_don_joueur =[i[0].id for i in joueur.don_arme]
    if joueur.classe.name == "Guerrier":
        if joueur.level >=4:
            if 3 in list_don_joueur:
                return True
    return False        
    
def spé_martiale_effet(joueur,sens=1):
    joueur.bonus_dégat += sens*2
        
spé_martiale = Don("Spécialisation martiale",4,1,\
            spé_martiale_effet,spé_martiale_check,\
            "Le personnage obtient un bonus de +2 sur les jets de dégâts de \
            l’arme choisie.")
        


list_don_arme = [arme_de_predilection,spé_martiale]

# =============================================================================
# Don tactique
# =============================================================================

def attaque_en_puissance_check(joueur):
    print(joueur.force)
    return joueur.force>=13

def attaque_en_puissance_effet(joueur,n):
    joueur.bonus_att-= n
    if joueur.arme.IsLight == False:
        joueur.bonus_dégat += n*(1+int(joueur.arme.IsTwoHanded))
        
attaque_en_puissance = Don("Attaque en puissance",5,2,\
            attaque_en_puissance_effet,attaque_en_puissance_check,\
            "blablab")

list_don_tactique = [attaque_en_puissance]

# =============================================================================
# Database
# =============================================================================

list_don = list_don_static + list_don_arme + list_don_tactique


