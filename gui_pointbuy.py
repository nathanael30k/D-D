# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 21:05:45 2019

@author: Nessim
"""
from joueur import modif
import tkinter as tk
    
def update_modif(controlVar,modifVar):
    #dani was here too :)
    point_price = [0,1,2,3,4,5,6,8,10,13,16]
    point = 0
    for i in range(len(modifVar)):
        carac = controlVar[i].get()
        if carac.isdigit():
            carac = int(controlVar[i].get())
            if carac<8:
                controlVar[i].set("8")
            elif carac>18:
                controlVar[i].set("18")
        else:
            controlVar[i].set("8")
        carac = int(controlVar[i].get())
        point += point_price[carac-8]
        modifVar[i].set(modif(carac))
    controlVar[6].set(str(point))
    return True

def gui_pointbuy(gui_carac):

    nom_variable = ["Force","Dext: ","Const","Intel","Sages","Charis"]
    widgetvar_list = []
    modif_list = []
    
    for i in range(len(nom_variable)):
        
        controlVar=tk.StringVar()
        modifVar = tk.IntVar()
        
        widgetvar_list.append(controlVar)
        modif_list.append(modifVar)
        
        tk.Label(gui_carac,text=nom_variable[i]).grid(row=i+1,column=1)
        
        label_modif = tk.Label(gui_carac,textvariable=modifVar,width=5)
        label_modif.grid(row=i+1,column=3)
        #dani was here :)
        entry = tk.Entry(gui_carac,name=str(i),width=15,textvariable=controlVar,\
                         validate = 'focusout',validatecommand=\
                         lambda: update_modif(widgetvar_list,modif_list))
        entry.grid(row=i+1,column=2)
    
    tk.Label(gui_carac,text="Point:").grid(row=7,column=2)
    point_var = tk.StringVar()
    point_label = tk.Label(gui_carac,textvariable = point_var)
    point_label.grid(row = 7,column=3)
    
    widgetvar_list.append(point_var)
    
    update_modif(widgetvar_list,modif_list)
    
    return(widgetvar_list[:6])