# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:08:12 2019

@author: Nessim
"""

import tkinter as tk
import tkinter.ttk as ttk
from classe import list_classe

def classe_select(index_var,widget):
    index_var.set(widget.current())
    return True

def valid_level(input):
    return input == "" or input.isdigit()

def gui_perso_general(general):
    
    general_input = []
    
    # name
    tk.Label(general, text="Nom:").grid(row=2,column=1)
    control = tk.StringVar()
    name=tk.Entry(general, width=15,textvariable= control)
    name.insert(tk.END,"Nom")
    name.grid(row=2,column=2)
    general_input.append(control)
    
    # level
    tk.Label(general, text="Level:").grid(row=3,column=1)
    control = tk.StringVar()
    valid = general.register(valid_level)
    level=tk.Entry(general, width=15,textvariable = control,\
                   validate = 'key',validatecommand = (valid,'%P'))
    level.insert(tk.END,"1")
    control.set(1)
    level.grid(row=3,column=2)
    general_input.append(control)
    
    # class
    control = tk.IntVar()
    tk.Label(general, text="Classe:").grid(row=4,column=1)
    liste_nom_classe = [i.name for i in list_classe]
    choix_classe = ttk.Combobox(general, width=15,height=1,values=liste_nom_classe,\
                                validate = 'focusout',state='readonly',\
                                validatecommand = lambda: classe_select(control,choix_classe))
    choix_classe.selectmode ='single'
    choix_classe.current(1)
    choix_classe.grid(row=4,column=2)
    general_input.append(control)
    return general_input    
    
    
    
    
    