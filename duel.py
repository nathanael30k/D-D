# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:23:08 2019

@author: Nessim
"""

from joueur import *

class Attaque:
    
    def __init__(self,arme, attaquant,defenseur):
        self.arme = arme
        self.attaquant = attaquant
        self.defenseur = defenseur
    
    def p_touche(self):
        # Cette fonction renvoie la probabilité de toucher un ennemi
        # CA = classe d'armure de l'ennemi
        # att = bonus au jet d'attaque
        
        #NB: borné par l'échec automatique '1' et la réussite automatique '20'
        att = self.arme.bonus_att + self.attaquant.bonus_att
        return max(1/20,min(19/20,1-(self.defenseur.CA-att-1)/20))
    
    def esperance_att(self):
        # Cette fonction renvoie l'esperance de dégat d'une attaque
        # cf fonction précedentes pour les variables
        # crit_mult = multiplicateur de critique
        return self.p_touche() * (1 + self.arme.p_crit()*\
                             (self.arme.crit_mult-1)) * (self.arme.dé_arme+\
                             self.attaquant.bonus_dégat).expected()
    def att_distrib(self):
        bonus_degat = self.attaquant.bonus_dégat
        distrib_touche = bernouilli(self.p_touche())
        distrib_crit = ((self.arme.crit_mult-1)*bernouilli(self.arme.p_crit()))+1
        return (distrib_crit*distrib_touche*(d10+bonus_degat).dice_distrib())
    
    def roll(self):
        dégat = self.att_distrib().roll()
        self.defenseur.pv -= dégat
        print(self.attaquant.name + " a infligé "+str(dégat)+" dégats à "\
              +self.defenseur.name)
        print("PV restants: "+str(self.defenseur.pv))
        
    def expected_roll(self):
        dégat = self.att_distrib().expected()
        self.defenseur.pv -= dégat
        print(self.attaquant.name + " a infligé "+str(dégat)+" dégats à "\
              +self.defenseur.name)
        print("PV restants: "+str(self.defenseur.pv))
        
    def silent_roll(self):
        dégat = self.att_distrib().roll()
        self.defenseur.pv -= dégat

def duel(list_joueur):
    init=[0]*len(list_joueur)
    survie = True
    while survie:
        init = [i.roll_initiative() for i in list_joueur]
        print(init)
        first = list_joueur[np.argmax(init)]
        second = list_joueur[np.argmin(init)]
        Attaque(first.arme,first,second).roll()
        if second.isAlive():
            Attaque(second.arme,second,first).roll()
        else:
            survie = False
        survie = first.isAlive() and second.isAlive()
    [i.pv_reset() for i in list_joueur]
    name = [j.name for j in list_joueur]
    pv =  [k.pv for k in list_joueur]
    print(name[np.argmax(pv)]+" a triomphé de "+name[np.argmin(pv)])

def expected_duel(list_joueur):
    init=[0]*len(list_joueur)
    survie = True
    while survie:
        init = [i.expected_initiative() for i in list_joueur]
        print(init)
        first = list_joueur[np.argmax(init)]
        second = list_joueur[np.argmin(init)]
        Attaque(first.arme,first,second).expected_roll()
        if second.isAlive():
            Attaque(second.arme,second,first).expected_roll()
        else:
            survie = False
        survie = first.isAlive() and second.isAlive()
    name = [j.name for j in list_joueur]
    pv =  [k.pv for k in list_joueur]
    [i.pv_reset() for i in list_joueur]
    print(name[np.argmax(pv)]+" a triomphé de "+name[np.argmin(pv)])
   
def silent_duel(list_joueur):
    init=[0]*len(list_joueur)
    survie = True
    while survie:
        init = [i.roll_initiative() for i in list_joueur]
        first = list_joueur[np.argmax(init)]
        second = list_joueur[np.argmin(init)]
        Attaque(first.arme,first,second).silent_roll()
        if second.isAlive():
            Attaque(second.arme,second,first).silent_roll()
        else:
            survie = False
        survie = first.isAlive() and second.isAlive()
    name = [j.name for j in list_joueur]
    pv =  [k.pv for k in list_joueur]
    [i.pv_reset() for i in list_joueur]
    return np.argmax(pv)

def stat(list_joueur,N):
    score = [0,0]
    for i in range(N):
        #print(silent_duel(list_joueur))
        v = silent_duel(list_joueur)
        #print(v)
        score[v] = score[v]+1
    score = [100*j/N for j in score]
    print(score)
    
    
#duel([HobJason,HobJason2])
N = 100
stat([HobJason,HobJason2],N)
#print(silent_duel([HobJason,Ogre]))
#stat([HobJason,Ogre],N)
#squouik = Attaque(épéeBatarde,HobJason,Ogre)
#print(squouik.esperance_att())
#squouik.att_distrib().show()