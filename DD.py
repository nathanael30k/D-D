# -*- coding: utf-8/ -*-
"""
Created on Tue Dec 25 19:52:55 2018

@author: Nessim
"""
import numpy as np
import matplotlib.pyplot as plt
from RPG.dice import *
from RPG.distrib import *


def Ptouche(att,CA):
    # Cette fonction renvoie la probabilité de toucher un ennemi
    # CA = classe d'armure de l'ennemi
    # att = bonus au jet d'attaque
    
    #NB: borné par l'échec automatique '1' et la réussite automatique '20'
    return max(1/20,min(19/20,1-(CA-att-1)/20))


def Pcrit(crit_size):
    # Cette fonction renvoie la probabilité qu'une attaque réussie soit un
    #critique
    # crit_size = taille de la zone de critique
    #ex: critique en 19-20 => crit_size = 2
    
    return crit_size/20


def Esp_dégat(dé_arme,bonus_dégat):
    # Cette fonction renvoie l'esperance du jet de dégat
    # dé_arme = dé de dégat utilisé par l'arme
    # bonus_dégat = somme de tous les bonus appliqués aux dégats
    return ((dé_arme+1)/2)+bonus_dégat


def Dégat_max(crit_mult,dé_arme,bonus_dégat):
    # Cette fonction renvoie l'esperance du jet de dégat
    # dé_arme = dé de dégat utilisé par l'arme
    # bonus_dégat = somme de tous les bonus appliqués aux dégats
    return crit_mult*(dé_arme+bonus_dégat)


def esperance_att(att,CA,crit_size,crit_mult,dé_arme,bonus_dégat,):
    # Cette fonction renvoie l'esperance de dégat d'une attaque
    # cf fonction précedentes pour les variables
    # crit_mult = multiplicateur de critique
    return Ptouche(att,CA) * (1 + Pcrit(crit_size)*(crit_mult-1)) * Esp_dégat(\
                  dé_arme,bonus_dégat)


def distrib_att(att,CA,crit_size,crit_mult,dé_arme,bonus_dégat):
    # Cette fonction calcule la distribution de probablité de dégat d'une
    #attaque
    #ex: distrib[x] est le probabilité d'infliger x dégat lors d'une attaque
    # cf fonction précedentes pour les variables
    
    # Calcul de quelques valeurs importantes
    p_touche = Ptouche(att,CA)
    p_crit = Pcrit(crit_size)
    dégat_max = Dégat_max(crit_mult,dé_arme,bonus_dégat)
    
    # Initialisation du tableau de probabilité
    distrib = [0]*(dégat_max+1)
    
    # Zero dégat <=> échec de l'attaque
    distrib[0] = 1-p_touche 
    
    for i in range(dé_arme):
        #le resultat au dé est "i", et je n'ai pas fait de critique
        distrib[i+bonus_dégat+1]=p_touche*(1-p_crit)/dé_arme
        #le resultat au dé est "i", et j'ai fait de critique
        distrib[crit_mult*(i+bonus_dégat+1)]+=p_touche*(p_crit)/dé_arme
    
    #Affiche la somme des probabilités (doit etre égale à 1)
    print(sum(distrib))
    return distrib
    

class Arme:
    def __init__(self,dé_degat,crit_size,crit_mult,bonus_att,bonus_dégat,
                 IsTwoHanded):
        self.dé_arme = dé_arme
        self.crit_size = crit_size
        self.crit_mult = crit_mult
        self.bonus_att = bonus_att
        self.bonus_dégat = bonus_dégat
        self.IsTwoHanded = IsTwoHanded
    

class Guerrier:
    
    def __init__(self,level,force,bba,bonus_att,bonus_dégat,arme):
        self.level = level
        self.force = force
        self.bba = bba
        self.bonus_att = bonus_att
        self.bonus_dégat = bonus_dégat
        self.arme = arme
    
    def opti_attpuiss(self):
        
        #initialise le tableau de CA et de malus optimal
        CA = [10]*31
        malus_opti = [10]*31
        
        
        # Calcules les valeurs pertinentes
        modif_force = np.floor((force-10)/2)
        base_att = bba + modif_force +bonus_att+self.arme.bonus_att
        base_degat = bonus_dégat +self.arme.bonus_dégat+ (1+self.arme.IsTwoHanded/2)*modif_force
        
        # Initialise tableau pou stocker les esperancespour différents malus
        tab_esp = [0]*(level+1)

        for i in range(31):
            #itère sur les CA
            ca = 10+i
            for j in range(level+1):
                #itère sur les malus
                tab_esp[j] = esperance_att(base_att-j,ca,self.arme.crit_size,self.arme.crit_mult,self.arme.dé_arme,base_degat+(1+self.arme.IsTwoHanded)*j)
  
            CA[i] = ca
            #trouve le max
            malus_opti[i] = np.argmax(tab_esp)
        #affiche le graph
        #plt.plot(CA,malus_opti)
                

level = 8
force = 20
bba = 8
bonus_att = 2
dé_arme = 10
crit_size = 1
crit_mult = 3
bonus_dégat = 3
IsTwoHanded = True

Coutille = Arme(10,1,3,0,0,True)
Ezychiel = Guerrier(level,force,bba,bonus_att,bonus_dégat,Coutille)
Ezychiel.opti_attpuiss()


A = distrib_att(16,22,1,3,10,10)
B = distrib_att(11,22,1,3,10,10)
plt.figure()
#plt.plot(Somme_distrib(A,B))


d6 = dice([0,0,1,0,0,0,0,0])
test = distrib(2,4)
test.show()
test+=2*test
test.show()