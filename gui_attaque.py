# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 01:39:38 2019

@author: Nessim
"""
import tkinter as tk

def gui_attaque(panel,joueur):
    
    
    attaque_var = tk.StringVar()
    attaque_display = tk.Label(panel,textvariable = attaque_var)
    attaque_var.set(joueur.dsp_att())
    attaque_display.grid(row=1,column=1)
    