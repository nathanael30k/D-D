# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:23:09 2019

@author: Nessim
"""


# ==================================V0=========================================
# Ne prend pas en compte les différents types de dégats
# Seulement arme de corps à corps sans allonge
# =============================================================================


from copy import deepcopy


# =============================================================================
# Class
# =============================================================================

class Arme:
    
    def __init__(self,nom,id,dé_degat,crit_size,crit_mult,IsTwoHanded,IsLight,\
                 maitre,bonus_magique,effet_magique,prix_base):
        
        self.nom = nom
        
        self.id = id #id correspondant à l'arme de base
        
        self.dé_arme = dé_degat+ bonus_magique
        
        self.crit_size = crit_size #taille de la zone de critique
        self.crit_mult = crit_mult
        
        self.IsTwoHanded = IsTwoHanded
        self.IsLight = IsLight
        
        self.bonus_att = max(int(maitre),bonus_magique)

        self.maitre = maitre
        self.bonus_magique = bonus_magique    
        self.modif_magie = bonus_magique #modif magique du prix
         
        for i in range(len(effet_magique)): 
            #application de tous les effets magiques
            effet_magique[i].effet(self)
            
        self.prix_base = prix_base
        
        
    def p_crit(self):
        # Cette fonction renvoie la probabilité qu'une attaque réussie soit un
        #critique
        # crit_size = taille de la zone de critique
        #ex: critique en 19-20 => crit_size = 2
        return self.crit_size/20
        
    
    def set_magic(self,nom,bonus_magique,effet_magique):
        # renvoie une NOUVELLE arme, dotée des mêmes caractéristiques que \
        #l'arme de base, mais avec les effets magiques/bonus d'altération en \
        #argument
        
        output = deepcopy(self.de_maitre()) #génération de la nouvelle arme
        
        #ajout des propriétés magiques
        output.nom = nom
        output.bonus_magique = bonus_magique
        output.effet_magique = effet_magique
        
        #recalcul des carac de l'arme
        output.dé_arme = output.dé_arme+ output.bonus_magique
        output.bonus_att = max(int(self.maitre),bonus_magique)
        
        #application des effets magiques
        for i in range(len(effet_magique)):
            effet_magique[i].effet(output)
        return output
    
    def de_maitre(self):
        # renvoie une NOUVELLE arme, dotée des mêmes caractéristiques que \
        #l'arme de base, mais de maitre
        
        output = deepcopy(self) #genere nouvelle arme
        output.maitre = True #ajout de la propriété maitre
        
        #recalcul des carac de l'arme
        output.bonus_att = int(output.maitre)+ output.bonus_magique
        
        return output
    

    def __str__(self):
        #gère l'affichage de l'arme
        output = self.nom
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
    
    
    def prix_achat(self):
        #renvoie le prix d'achat total d'un arme
        prix_magie = [0,2,8,18,32,50,72,98,128,162,200] #prix du modif en kpo
        return self.prix_base+self.maitre*300 + \
                    1000*prix_magie[self.modif_magie]




