# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:23:09 2019

@author: Nessim
"""

# ================= V0 ========================
# ==============Completer database=============

from dice import *
from copy import *


# Class

class Arme:
    def __init__(self,name,id,dé_degat,crit_size,crit_mult,IsTwoHanded,maitre,\
                 bonus_magique,effet_magique,prix_base):
        
        self.name = name
        self.id = id
        self.prix_base = prix_base
        self.dé_arme = dé_degat+ bonus_magique
        self.crit_size = crit_size
        self.crit_mult = crit_mult
        self.bonus_att = int(maitre)+ bonus_magique
        self.IsTwoHanded = IsTwoHanded
        self.maitre = maitre
        self.bonus_magique = bonus_magique
        
        self.modif_magie = bonus_magique
        for i in range(len(effet_magique)):
            effet_magique[i](self)
        
    def p_crit(self):
        # Cette fonction renvoie la probabilité qu'une attaque réussie soit un
        #critique
        # crit_size = taille de la zone de critique
        #ex: critique en 19-20 => crit_size = 2
        return self.crit_size/20
    
    def __str__(self):
        output = self.name
        if self.bonus_magique != 0 :
            output += " +"+str(self.bonus_magique)
        elif self.maitre:
            output += " de maitre"
        output += "\n"
        output += str(self.dé_arme)+"/"
        output += str(20-self.crit_size+1)+ "-20 x"
        output += str(self.crit_mult)+"\n"
        output += "prix: "+str(self.prix_achat())+"po\n"
        return output
    
    def add_magic(self,name,bonus_magique,effet_magique):
        output = deepcopy(self)
        output.name = name
        output.bonus_magique = bonus_magique
        output.effet_magique = effet_magique
        output.maitre = False
        
        output.dé_arme = output.dé_arme+ output.bonus_magique
        output.bonus_att = int(output.maitre)+ output.bonus_magique
        
        for i in range(len(effet_magique)):
            effet_magique[i](output)
        return output
    
    def de_maitre(self):
        output = deepcopy(self)
        output.maitre = True
        
        output.bonus_att = int(output.maitre)+ output.bonus_magique
        
        return output
    
    def prix_achat(self):
        prix_magie = [0,2,8,18,32,50,72,98,128,162,200]
        return self.prix_base+self.maitre*300 + 1000*prix_magie[self.modif_magie]
        
    
# Effet magique
        
def feu(arme):
    arme.dé_arme += d6
    arme.modif_magie += 1

# Epee de base
    
épée_batarde = Arme("épée_batarde",1,d10,2,2,False,False,0,[],35)

# Epee unique/magique

hobJason_sword = épée_batarde.de_maitre()
fire_sword = épée_batarde.add_magic("firesword",3,[feu])

list_arme=[épée_batarde,fire_sword]
# Test
#print(épée_batarde.de_maitre())
#print(fire_sword)
#massue = Arme(2*d8,1,2,True,False)

