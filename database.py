# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 01:37:37 2019

@author: Nessim
"""

from dice import d10,d8,d6,d4,d3
from numpy import inf

from arme import Arme
from effet_arme import list_effet_arme

from armure import Armure

from bouclier import Bouclier

from don import list_don

from classe import guerrier

from joueur import Joueur

# =============================================================================
# Armes (nom,id,dé_degat,crit_size,crit_mult,IsTwoHanded,IsLight,maitre,\
#                bonus_magique,effet_magique,prix_base)
# =============================================================================

main_nues = Arme("main nue",0,d3,1,2,False,True,False,0,[],0)
dague = Arme("dague",1,d4,1,2,False,True,False,0,[],2)    
épée_batarde = Arme("épée batarde",2,d10,2,2,False,False,False,0,[],35)
épée_courte = Arme("épée courte",3,d6,2,2,False,True,False,0,[],10)
épée_longue = Arme("épée longue",4,d8,2,2,False,False,False,0,[],15)

arme_de_base = [main_nues,dague,épée_batarde,épée_courte,épée_longue]

hobJason_sword = épée_batarde.de_maitre()
fire_sword = épée_batarde.set_magic("firesword",3,[list_effet_arme[0]])

arme_speciale = [hobJason_sword,fire_sword]

list_arme = arme_de_base + arme_speciale

# =============================================================================
# Armure (nom,id,bonus_CA,modif_dex_max,bonus_magique,\
#                 effet_magique,prix_base)
# =============================================================================

pyjama = Armure("Pyjama",0,0,inf,0,[],0)
matelassée = Armure("Armure matelassée",1,1,8,0,[],5)
cotte_de_mailles = Armure("Cotte de mailles",2,5,2,0,[],150)
harnois = Armure("Harnois",3,8,1,0,[],1500)

list_armure = [pyjama,matelassée,cotte_de_mailles,harnois]

# =============================================================================
# Bouclier (nom,id,bonus_CA,bonus_magique,effet_magique,prix_base)
# =============================================================================

aucun = Bouclier("aucun",0,0,0,[],0)
rondache_acier = Bouclier("Rondache en acier",1,1,0,[],9)
écu_acier = Bouclier("Ecu en acier",1,2,0,[],20)

list_bouclier = [aucun,rondache_acier,écu_acier]

# =============================================================================
# Joueur (name,classe,level,force,dex,con,intel,sag,char,armure,\
#               arme,bouclier,don_static,don_arme,don_tactique,inventory_arme,\
#                inventory_armure,inventory_bouclier,inventory_other)
# =============================================================================

HobJason = Joueur("HobJason",guerrier,5,16,15,16,10,12,8,harnois,hobJason_sword,\
                  écu_acier,[list_don[1]],[[list_don[3],épée_batarde],\
                   [list_don[4],épée_batarde]],[],[],[],[],[])
HobJason2 = Joueur("HobJason2",guerrier,5,16,15,16,10,12,8,harnois,hobJason_sword,\
                  écu_acier,[list_don[1]],[[list_don[3],épée_batarde],\
                   [list_don[4],épée_batarde]],[],[],[],[],[])

SuperiorHobJason = Joueur("Super HobJason2",guerrier,15,16,15,16,10,12,8,harnois,hobJason_sword,\
                  écu_acier,[list_don[2],list_don[1]],[],[],[dague,hobJason_sword],[],[],[])
    
list_joueur = [HobJason,HobJason2,SuperiorHobJason]