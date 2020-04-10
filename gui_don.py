# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:37:25 2019

@author: Nessim
"""
from don import list_don
import tkinter as tk
import tkinter.ttk as ttk

def don_select(index_var,widget,list_index,joueur,panel):
    
    total_don = [[],[],[]]
    
    for i in range(len(widget)):
        index_var[i].set(list_index[widget[i].current()])
        don = list_don[list_index[widget[i].current()]]
        total_don[don.categorie].append(don)  
    
    #apply modification
#    joueur.switch_don()
#    joueur.don_static = total_don[0]
#    joueur.don_arme = total_don[1]
#    joueur.don_tactique = total_don[2]
#    joueur.switch_don()
#    print(joueur.don_static)
    return True

def gui_don(panel,joueur):
    
    #liste des dons accessibles
    local_list_don = []
    for j in range(len(list_don)):
        if list_don[j].check(joueur):
            local_list_don += [j]
            
    #nombre de don
    nb_don = int(joueur.level/3)+1
    
    #liste des variables de controles et des wigets
    var_output = []
    widget_list = []
    total_list_don = []
    for i in range(nb_don):
        
        total_list_don.append(local_list_don)
        
        
        #génère variable de control et l'ajoute à la liste 
        control = tk.IntVar()
        var_output.append(control)
        
        #création de la combobox, qui déclenche don_select si modifié
        don_choix = ttk.Combobox(panel,width=15,height=1,values = \
                        [list_don[k].nom for k in local_list_don],\
                        validate = 'focusout',state='readonly',\
                        validatecommand = lambda: don_select(var_output,\
                        widget_list,local_list_don,joueur,panel))
        #une seule option sélectionnée
        don_choix.selectmode ='single'
        #ajout à la liste des widgets
        widget_list.append(don_choix)
        #affichage
        don_choix.grid(row=i+1,column=1)
        
    actuel_don = joueur.don
    for j in range(len(widget_list)):
        if j<len(actuel_don):
            widget_list[j].current(local_list_don.index(actuel_don[j].id)) 
        else:
            widget_list[j].current(0)
    don_select(var_output,widget_list,local_list_don,joueur,panel)

    return [widget_list,total_list_don]

#gui_carac = tk.Tk()
#gui_don(gui_carac,HobJason2)
#gui_carac.mainloop()