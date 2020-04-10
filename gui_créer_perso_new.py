# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 23:53:18 2019

@author: Nessim
"""
import tkinter as tk

def gui_perso():
    
    #initialisation de la fenetre
    gui = tk.Tk()
    
    #panneau general (nom, classe et level)
    general=tk.LabelFrame(gui,text="General",width = 300,height=60)      
    general.grid(row=1,column=1,columnspan=2)
    
    #panneau carac    
    point_buy = tk.LabelFrame(gui,text="Caractéristique")
    point_buy.grid(row=2,column=1)  
    
    gui.mainloop()
    
gui_perso()