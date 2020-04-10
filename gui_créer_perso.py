# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 15:20:54 2019

@author: Nessim
"""

import tkinter as tk
import tkinter.ttk as ttk

from gui_perso_general import gui_perso_general
from gui_pointbuy import gui_pointbuy
from gui_don import gui_don
from gui_attaque import gui_attaque

from classe import list_classe
from don import list_don
from database import *
pyjama = list_armure[0]
main_nues = list_arme[0]
from joueur import Joueur   


def generate_perso(general_input,carac_input,total_don):
    
    name = general_input[0].get()
    level = int(general_input[1].get())
    classe = list_classe[general_input[2].get()]
    
    force = int(carac_input[0].get())
    dex = int(carac_input[1].get())
    con = int(carac_input[2].get())
    intel = int(carac_input[3].get())
    sag = int(carac_input[4].get())
    char = int(carac_input[5].get())

    dons_static = total_don[0]
    dons_arme = total_don[1]
    dons_tactique = total_don[2]

    return Joueur(name,classe,level,force,dex,con,intel,sag,char,pyjama,\
                 main_nues,aucun,dons_static,dons_arme,dons_tactique,[],[],[],[])
    


def global_update(input,panel_don,temp_perso):
    general_input = input[0]
    carac_input = input[1]
    widget = input[2][0]
    list_index = input[2][1]
    total_don = [[],[],[]]
    
    for i in range(len(widget)):
        don = list_don[list_index[i][widget[i].current()]]
        if don.categorie==1:
            total_don[don.categorie].append([don,main_nues])
        else:
            total_don[don.categorie].append(don)  
    perso_temp = generate_perso(general_input,carac_input,total_don)
    
    local_list_don = []
    for j in range(len(list_don)):
        if list_don[j].check(perso_temp):
            local_list_don += [j]
        
            
            
    for i in range(perso_temp.nb_don):
        if i < len(widget):
            if widget[i].current() == 0:
                print(i)
                widget[i].config(values = [list_don[k].nom for k in local_list_don])
                list_index[i] = local_list_don
        else:
            don_choix = ttk.Combobox(panel_don,width=15,height=1,values = \
                        [list_don[k].nom for k in local_list_don],\
                        validate = 'focusout',state='readonly',validatecommand=\
                        lambda: global_update(input,panel_don,temp_perso))
            don_choix.current(0)
            don_choix.grid(row=len(widget)+1,column =1) 
            widget.append(don_choix)
            list_index.append(local_list_don)
    
    while perso_temp.nb_don != len(widget):
        if len(widget)<perso_temp.nb_don:            
            don_choix = ttk.Combobox(panel_don,width=15,height=1,values = \
                        [list_don[k].nom for k in list_index],\
                        validate = 'focusout',state='readonly',validatecommand=\
                        lambda: global_update(input,panel_don,temp_perso))
            don_choix.current(0)
            don_choix.grid(row=len(widget)+1,column =1) 
            widget.append(don_choix)
        else:
            widget[len(widget)-1].destroy()
            del widget[len(widget)-1]
    return True   


def gui_perso():
    
    #initialisation de la fenetre
    gui = tk.Tk()
    
    #panneau general (nom, classe et level)
    general=tk.Frame(gui)   
    general_input = gui_perso_general(general)    
    general.grid(row=1,column=1,columnspan=2)
    
    #panneau carac    
    point_buy = tk.LabelFrame(gui,text="Caractéristique")
    carac_input = gui_pointbuy(point_buy)
    point_buy.grid(row=2,column=1)  
    
    temp_perso = generate_perso(general_input,carac_input,[[],[],[]])
    
    #panneau don
    panel_don = tk.LabelFrame(gui,text="dons")
    don_input = gui_don(panel_don,temp_perso)
    panel_don.grid(row=2,column=2,sticky ='n') 
          
    #tracking et update
    total_input = [general_input,carac_input]
    test = lambda a,b,c: global_update(total_input,panel_don,temp_perso)
    for i in range(len(total_input)):
        for k in range(len(total_input[i])):    
            total_input[i][k].trace("w",test) 
            
    for i in don_input[0]:
        i.config(validatecommand = lambda: global_update(total_input,panel_don,temp_perso))
    
    total_input.append(don_input)
   
    
    
    gui.mainloop()
    #panneau attaque
    panel_att = tk.LabelFrame(gui,text="attaque")
    gui_attaque(panel_att,temp_perso)
    panel_att.grid(row=3,column=1,columnspan=2)
    
    gui.mainloop()

gui_perso()
    