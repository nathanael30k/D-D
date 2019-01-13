# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 18:26:27 2019

@author: Nessim
"""

from tkinter import *
from classe import list_classe
from armure import list_armure
from arme import list_arme
from bouclier import list_bouclier
from joueur import *
from duel import duel_screen
import time as time
from don import *

list_don = list_don_static + list_don_arme

def menu():
    fenetre = Tk()
        
    label = Label(fenetre, text="Donjon & Dragon")
    label.pack()
    bouton=Button(fenetre, text="Création de Perso", command=création_perso)
    bouton.pack()
    bouton2=Button(fenetre, text="Combat", command=gui_choix_player)
    bouton2.pack()
    
    fenetre.mainloop()

def gui_choix_player():
    fenetre = Tk()    
    # J1
    J1=Listbox(fenetre, width=15,height=10,exportselection=0)
    for i in range(len(list_joueur)):
        J1.insert(END,list_joueur[i].name)
    J1.selectmode ='single'
    J1.selection_set(0)
    J1.grid(row=1,column=1)
    
    # J2
    J2=Listbox(fenetre, width=15,height=10,exportselection=0)
    for i in range(len(list_joueur)):
        J2.insert(END,list_joueur[i].name)
    J2.selectmode ='single'
    J2.selection_set(0)
    J2.grid(row=1,column=2)
    
    bouton2=Button(fenetre, text="Combat", command=\
                   lambda: gui_fight(J1,J2))
    bouton2.grid(row=2,column=2)
    
    
def gui_fight(J1,J2):
    gui_fight = Tk()
    J1 = list_joueur[list(J1.curselection())[0]]
    J2 = list_joueur[list(J2.curselection())[0]]
    label = Label(gui_fight, text="Donjon & Dragon",width=50)
    label.grid(row=1,column=2)
    
    
    labelJ1=Label(gui_fight, text=str(J1),width=20)
    labelJ1.grid(row=2,column=1)
    pv1_max = Canvas(gui_fight, width=100, height=15, background='red')
    pv1_max.grid(row=3,column=1,sticky='w')
    pv1 = Canvas(gui_fight, width=100, height=15, background='green')
    pv1.grid(row=3,column=1,sticky='w')
    
    
    labelJ2=Label(gui_fight, text=str(J2),width=20)
    labelJ2.grid(row=2,column=3)
    pv2_max = Canvas(gui_fight, width=100, height=15, background='red')
    pv2_max.grid(row=3,column=3,sticky='e')
    pv2 = Canvas(gui_fight, width=100, height=15, background='green')
    pv2.grid(row=3,column=3,sticky='e')
    go = Fight(gui_fight,J1,J2)
    screen = Label(gui_fight, text = "",height=15)
    screen.grid(row=2,column=2,sticky='n')
    bouton2=Button(gui_fight, text="Combat!", command=\
                   lambda: duel_screen([J1,J2],[screen,pv1,pv2]))
    bouton2.grid(row=3,column=2)


class Fight:
    def __init__(self,fenetre,J1,J2):
        self.fenetre = fenetre
        self.J1 = J1
        self.J2 = J2
        
    def initiative(self):
        
        init=[0]*len(list_joueur)
        
        screen = Label(self.fenetre, text = "Initiative!")
        screen.grid(row=2,column=2,sticky='n')
        
        time.sleep(0.5)
        
        screen.config(text=J)

    
    
def création_perso():
    fenetre = Tk()
    label = Label(fenetre, text="Création de perso").grid(row=1,column=2)
    
    # name
    Label(fenetre, text="Nom:").grid(row=2,column=1)
    name=Entry(fenetre, width=15)
    name.insert(END,"Nom")
    name.grid(row=2,column=2)
    
    # level
    Label(fenetre, text="Level:").grid(row=3,column=1)
    level=Entry(fenetre, width=15)
    level.insert(END,"1")
    level.grid(row=3,column=2)
    
    # class
    Label(fenetre, text="Classe:").grid(row=4,column=1)
    choix_classe=Listbox(fenetre, width=15,height=1,exportselection=0)
    for i in range(len(list_classe)):
        choix_classe.insert(END,list_classe[i].name)
    choix_classe.selectmode ='single'
    choix_classe.selection_set(0)
    choix_classe.grid(row=4,column=2)

    # force
    Label(fenetre, text="Force:").grid(row=5,column=1)
    force=Entry(fenetre, width=15)
    force.insert(END,"10")
    force.grid(row=5,column=2)
    
    # dex
    Label(fenetre, text="Dex:").grid(row=6,column=1)
    dex=Entry(fenetre, width=15)
    dex.insert(END,"10")
    dex.grid(row=6,column=2)
    
    # con
    Label(fenetre, text="Con:").grid(row=7,column=1)
    con=Entry(fenetre, width=15)
    con.insert(END,"10")
    con.grid(row=7,column=2)
    
    # intel
    Label(fenetre, text="Intel:").grid(row=8,column=1)
    intel=Entry(fenetre, width=15)
    intel.insert(END,"10")
    intel.grid(row=8,column=2)
    
    # sag
    Label(fenetre, text="Sag:").grid(row=9,column=1)
    sag=Entry(fenetre, width=15)
    sag.insert(END,"10")
    sag.grid(row=9,column=2)
    
    # char
    Label(fenetre, text="Char:").grid(row=10,column=1)
    char=Entry(fenetre, width=15)
    char.insert(END,"10")
    char.grid(row=10,column=2)

    # arme
    Label(fenetre, text="Arme:").grid(row=11,column=1)
    choix_arme=Listbox(fenetre, width=15,height=1,exportselection=0)
    for i in range(len(list_arme)):
        choix_arme.insert(END,list_arme[i].name)
    choix_arme.selectmode ='single'
    choix_arme.selection_set(0)
    choix_arme.grid(row=11,column=2)
    
    # armure
    Label(fenetre, text="Armure:").grid(row=12,column=1)
    choix_armure=Listbox(fenetre, width=15,height=1,exportselection=0)
    for i in range(len(list_armure)):
        choix_armure.insert(END,list_armure[i].name)
    choix_armure.selectmode ='single'
    choix_armure.selection_set(0)
    choix_armure.grid(row=12,column=2)

    # bouclier
    Label(fenetre, text="bouclier:").grid(row=13,column=1)
    choix_bouclier=Listbox(fenetre, width=15,height=1,exportselection=0)
    for i in range(len(list_bouclier)):
        choix_bouclier.insert(END,list_bouclier[i].name)
    choix_bouclier.selectmode ='single'
    choix_bouclier.selection_set(0)
    choix_bouclier.grid(row=13,column=2)
    
    #don
    choix_don=Listbox(fenetre, width=20,height=15,selectmode='multiple',exportselection=0)
    for i in range(len(list_don)):
        choix_don.insert(END,list_don_nom[i])
    choix_don.grid(row=2,column=3,rowspan=12)
    
    list_widget = [name,choix_classe,level,force,dex,con,intel,sag,char,choix_arme,\
                   choix_armure,choix_bouclier,choix_don]
    
    #final
    bouton=Button(fenetre, text="Générer perso", \
                  command=lambda: générer_perso(list_widget))
    bouton.grid(row=14,column=2)
    fenetre.mainloop()
    
def générer_perso(list_widget):
    name = list_widget[0].get()
    classe = list_classe[list(list_widget[1].curselection())[0]]
    level = int(list_widget[2].get())
    force = int(list_widget[3].get())
    dex = int(list_widget[4].get())    
    con = int(list_widget[5].get())
    intel = int(list_widget[6].get())        
    sag = int(list_widget[7].get())
    char = int(list_widget[8].get())

    arme = list_arme[list(list_widget[9].curselection())[0]]    
    armure = list_armure[list(list_widget[10].curselection())[0]]
    bouclier = list_bouclier[list(list_widget[11].curselection())[0]]
    
    don_static = []
    don_arme =  []

    don = list(list_widget[12].curselection())


    for i in range(len(don)):
            if don[i]<len(list_don_static):
                don_static += [list_don[don[i]]]
            else:
                don_arme += [don[i]]


#def choix_arme_don(index_don):
    pop_up = Tk()
    choix_arme_don = []
    output = []
    for i in range(len(don_arme)):
        Label(pop_up, text=list_don_nom[don_arme[i]]+"(").grid(row=i,column=1)
        Label(pop_up, text=")").grid(row=i,column=3)
        choix_arme_don+=[Listbox(pop_up, width=15,height=1,exportselection=0)]
        for k in range(len(list_arme)):
            choix_arme_don[i].insert(END,list_arme[k].name)
        choix_arme_don[i].selectmode ='single'
        choix_arme_don[i].selection_set(0)
        choix_arme_don[i].grid(row=i,column=2)
        
    bouton=Button(pop_up, text="valider", \
                  command=lambda:valider_choix(choix_arme_don,don_arme,pop_up,\
                                               name,classe,level,force,dex,con\
                                               ,intel,sag,char,armure,\
                                               arme,bouclier,don_static))
    bouton.grid(row=2,column=2)
    pop_up.mainloop()
    
def valider_choix(listbox,index,fenetre,name,classe,level,force,dex,con,intel,sag,char,armure,\
                                               arme,bouclier,don_static):
    output=[]
    for i in range(len(listbox)):
        output +=[[list_don[index[i]],list_arme[list(listbox[i].curselection())[0]]]]
        
    fenetre.destroy()   
    joueur = Joueur(name,classe,level,force,dex,con,intel,sag,char,armure,\
                 arme,bouclier,don_static,output)
    fenetre = Tk()
    Label(fenetre, text=str(joueur)).pack()
    bouton=Button(fenetre, text="Ajouter à la liste", command=\
                  lambda: ajouter_liste(fenetre,joueur))
    bouton.pack()
    
def ajouter_liste(fenetre,joueur):
    list_joueur.append(joueur)
    fenetre.destroy()
    
        
menu()