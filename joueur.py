# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:21:59 2019

@author: Nessim
"""

from dice import d20
import numpy as np

def modif(n):
    return int(np.floor((n-10)/2))

# =============================================================================
# Class Joueur
# =============================================================================

class Joueur:
    
    def __init__(self,name,classe,level,force,dex,con,intel,sag,char,armure,\
                arme,bouclier,don_static,don_arme,don_tactique,inventory_arme,\
                inventory_armure,inventory_bouclier,inventory_other):
        
# =============================================================================
#   Informations générales
# =============================================================================
        
        self.name = name
        self.classe = classe
        self.level = level
        
# =============================================================================
#   Caractéristiques        
# =============================================================================
        
        self.force = force
        self.dex = dex
        self.con = con
        self.intel = intel
        self.sag = sag
        self.char = char
       
# =============================================================================
#   Equipements
# =============================================================================
        
        self.armure = armure
        self.arme = arme
        self.bouclier = bouclier
        
# =============================================================================
#   Inventaire
# =============================================================================
        
        self.inventory_arme = inventory_arme
        self.inventory_armure = inventory_armure
        self.inventory_bouclier = inventory_bouclier
        self.inventory_other = inventory_other

# =============================================================================
#   Computation
# =============================================================================
        
        self.init = modif(dex)
        
        self.pv_max = int(np.floor( classe.DV.max() + \
                                   (level-1)*classe.DV.expected() + \
                                   level*modif(con)))
        self.pv = self.pv_max
        
        self.nb_don = int(self.level/3)+1
        self.bba = int(float(classe.bba_mult)*float(level))
        
        self.bonus_att = self.bba + modif(force) + self.arme.bonus_att

        self.bonus_dégat = (int(1+self.arme.IsTwoHanded/2))*modif(force)
        
        
        self.CA = 10+armure.bonus_CA+modif(self.dex)+\
        int(not(self.arme.IsTwoHanded))*bouclier.bonus_CA
        
# =============================================================================
#   Dons
# =============================================================================
        
        self.don_static = don_static
        self.don_arme = don_arme
        self.don_tactique = don_tactique
        
        self.don = don_static+self.don_arme+don_tactique

        self.don_actif = False
        self.switch_don()

# =============================================================================
#   Methods
# =============================================================================

    def switch_don(self):
        sens = -2*int(self.don_actif)+1
        for i in range(len(self.don_static)):
            self.don_static[i].effet(self,sens)
        
        for i in range(len(self.don_arme)):
            if self.arme.id == self.don_arme[i][1].id:
                self.don_arme[i][0].effet(self,sens)
        self.don_actif = not(self.don_actif)
        
        self.don = self.don_static+self.don_arme+self.don_tactique
    
    def reset_don(self):
        self.switch_don()
        if self.don_actif == False:
            self.switch_don()
            
    def changer_arme(self,index):
        if self.don_actif:
            self.switch_don()
        self.arme = self.inventory_arme[index]
        self.bonus_att = self.bba + modif(self.force) + self.arme.bonus_att
        self.bonus_dégat = (int(1+self.arme.IsTwoHanded/2))*modif(self.force)
        self.switch_don
        
        
    def expected_initiative(self):
        return 10.5+self.init
    
    def roll_initiative(self):
        return (d20+self.init).roll()+self.init/100
    
    def isAlive(self):
        return self.pv>0
    def pv_reset(self):
        self.pv = self.pv_max
    
    def dsp_att(self):
        output = "att: +"+str(self.bonus_att)
        output += " ("+ str(self.arme.dé_arme+self.bonus_dégat)+"/"
        output += str(20-self.arme.crit_size+1)+ "-20 x"
        output += str(self.arme.crit_mult)  +")"
        return output
    
    def __str__(self):
        output = self.name + "\n"
        output += self.classe.name + " de niveau "+str(self.level)+".\n"
        output += "PV: "+str(self.pv)+"/"+str(self.pv_max)+"\n"
        output += "CA: "+str(self.CA)+"\n"
        output += "Init: +"+str(self.init)+"\n"
        output += "bba: +"+str(self.bba)+"\n"
        output += self.dsp_att()        
        return output