# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:21:59 2019

@author: Nessim
"""

from dice import *
from arme import *
from armure import *
from bouclier import *
from don import *
from classe import *

def modif(n):
    return int(np.floor((n-10)/2))

# Class

class Joueur:
    
    def new():
        print("hello")
    
    def __init__(self,name,classe,level,force,dex,con,intel,sag,char,armure,\
                 arme,bouclier,don_static,don_arme):
        
        # Caractéristiques de base
        self.name = name
        
        self.classe = classe
        self.level = level
        
        self.force = force
        self.dex = dex
        self.con = con
        self.intel = intel
        self.sag = sag
        self.char = char
        
        self.armure = armure
        self.arme = arme
        self.don_static = don_static
        self.don_arme = don_arme
        
        # To be computed
        self.init = modif(dex)
        
        self.pv_max = int(np.floor( classe.DV+modif(con) +(level-1)*(((classe.DV+1)/2)+modif(con))))
        self.pv = self.pv_max
        
        self.dex = min([self.dex,armure.modif_dex_max*2+10])
        self.CA = 10+armure.bonus_CA+modif(self.dex)+int(not(self.arme.IsTwoHanded))*bouclier.bonus_CA
        self.bba = int(float(classe.bba_mult)*float(level))
        self.bonus_att = self.bba + modif(force) + self.arme.bonus_att
        self.bonus_dégat = (int(1+self.arme.IsTwoHanded/2))*modif(force)
        
        # Dons
        for i in range(len(don_static)):
            don_static[i](self)
        
        for i in range(len(don_arme)):
            if self.arme.id == don_arme[i][1].id:
                don_arme[i][0](self)
        
    def expected_initiative(self):
        return 10.5+self.init
    def roll_initiative(self):
        return (d20+self.init).roll()+self.init/100
    
    def isAlive(self):
        return self.pv>0
    def pv_reset(self):
        self.pv = self.pv_max
    
    def __str__(self):
        output = self.name + "\n"
        output += self.classe.name + " de niveau "+str(self.level)+".\n"
        output += "PV: "+str(self.pv)+"/"+str(self.pv_max)+"\n"
        output += "CA: "+str(self.CA)+"\n"
        output += "Init: +"+str(self.init)+"\n"
        output += "bba: +"+str(self.bba)+"\n"
        output += "att: +"+str(self.bonus_att)+" ("
        output += str(self.arme.dé_arme+self.bonus_dégat)+"/"
        output += str(20-self.arme.crit_size+1)+ "-20 x"
        output += str(self.arme.crit_mult)
        
        return output

# Base de données      
        
HobJason = Joueur("HobJason",guerrier,5,16,15,16,10,12,8,harnois,hobJason_sword,\
                  écu_acier,[science_de_l_initiative],[[arme_de_predilection,épée_batarde],\
                   [spé_martiale,épée_batarde]])
HobJason2= Joueur("HobJason2",guerrier,5,16,15,16,10,12,8,harnois,hobJason_sword,\
                  écu_acier,[science_de_l_initiative],[[arme_de_predilection,épée_batarde],\
                   [spé_martiale,épée_batarde]])
    
list_joueur = [HobJason,HobJason2]

#HobJason2 = Joueur("HobJasons2",guerrier,5,16,15,16,10,12,8,5,21,épéeBatarde,\
                  #[science_de_l_initiative],[[arme_de_predilection,épéeBatarde]])
#print(HobJason)

#♠Ogre = Joueur("L'Ogre",8,8,7,16,29,massue,[])
